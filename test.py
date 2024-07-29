import requests
from bs4 import BeautifulSoup

url = 'https://dentalstall.com/shop/page/7'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

all_products = []

product_containers = soup.find_all(class_='product-inner')

for container in product_containers:
    product_dict = {}
    
    link_tag = container.find('a', class_='button')
    if link_tag and 'data-title' in link_tag.attrs:
        product_dict['productName'] = link_tag['data-title']
    
    price_tag = container.find('bdi')
    if price_tag:
        product_dict['productPrice'] = price_tag.get_text(strip=True)
    
    if 'productName' in product_dict and 'productPrice' in product_dict:
        all_products.append(product_dict)

print("All Products:")
print(all_products)
print(len(all_products))
