import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool
from runner import Run

class Scrape:
    def __init__(self, website_url, n):
        self.all_products = []
        self.website_url = website_url
        self.iteration_time = n
    
    def get_url(self, iterator):
        if iterator > 1:
            return f'{self.website_url}/page/{iterator}'
        return self.website_url
    
    def scrape_page(self, page_number):
        url = self.get_url(page_number)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        product_containers = soup.find_all(class_='product-inner')
        page_products = []

        for container in product_containers:
            product_dict = {}
            
            # Extract product name
            link_tag = container.find('a', class_='button')
            if link_tag and 'data-title' in link_tag.attrs:
                product_dict['productName'] = link_tag['data-title']
            
            # Extract product price
            price_tag = container.find('bdi')
            if price_tag:
                product_dict['productPrice'] = price_tag.get_text(strip=True)
            
            # Extract product image URL
            image_tag = container.find('img')
            if image_tag:
                if 'src' in image_tag.attrs and 'data:image/svg+xml' not in image_tag['src']:
                    product_dict['productImage'] = image_tag['src']
                elif 'data-lazy-src' in image_tag.attrs:
                    product_dict['productImage'] = image_tag['data-lazy-src']
                elif 'srcset' in image_tag.attrs:
                    product_dict['productImage'] = image_tag['srcset'].split(",")[0].strip().split(" ")[0]
            
            if 'productName' in product_dict and 'productPrice' in product_dict and 'productImage' in product_dict:
                page_products.append(product_dict)
        
        return page_products

    def scrape_data(self):
        with Pool(processes=120) as pool: 
            results = pool.map(self.scrape_page, range(1, self.iteration_time + 1))
        
        self.all_products = [item for sublist in results for item in sublist]
    
    def format_data(self):
        self.scrape_data()
        for data in self.all_products:
            data['productPrice'] = float(data['productPrice'].lstrip('₹'))
            Run(data=data).ingest()
            print(data)

Scrape(website_url="https://dentalstall.com/shop/", n=100).format_data()
