from fastapi import FastAPI, Request
from apps.scraper import Scrape
from models.models import ScrapeRequest
from validate.validate import ValidateRequest
app = FastAPI()
import uvicorn

static_token = "BYCVTUVULVHLVJNCFHCXCBLJXNOUIHGCYUBEIUEGUIYL"
    
@app.post("/v1")
def get_items(scrape: ScrapeRequest, request: Request):
    auth_header = request.headers.get("Authorization").split(' ')[1]
    if auth_header != static_token:
        raise Exception("Invalid auth token")
    valid_instance = ValidateRequest(scrape).validate_dict()
    if valid_instance:
        response = Scrape(website_url=scrape.url, n=scrape.page_no).format_data()
        print(response)
        return response
    else:
        print("invalid dict")  
        return {"status": "Error"}
    
"""
I have spent most of the time in desigining classes to make them more modular and extensive.
I have implemented the Abstract factory, Strategy and Observer design patterns here to implement the functionality. 
2 classes, one is FIleJson and second is WriteToMongo are implemented to write data inside file and mongoDB synchronously, however they could have been made asynchrous.
As per the requirement, if tomorrow we need more types of file to write the data on, then we only need to implement the class and write them down into the map.
If we need only 1 out of 2 write strategies then we can remove one from the list(common/constants.py) and things will work just fine.
Each class has its own set of methods to perform data formating and data validation to make the requiements more modular, currently everything is 
common as per the requirement
"""

"""In this above API, I am making an assumption that we are waiting for n seconds until the request completes, but in prod applications, this will definitely wont be 
the case, there we have to first return the response that scrapping has started, and when the scrapping and data ingestion will be completed, then we can print the entire
summary of how many documents have been inserted and processed for each strategy, write now it first waits until n seconds and at the end it prints how many documents were
scrapped
"""

"""
Due to less time, I am explaining the implementation to update the prices for only those products where the prices is changed, and it will be like a cron job not like a 
function built into this
"""

"""
IMPLEMENTATION OF PRICE UPDATE CHANGE SERVICE
When a data stream is sent to be ingested into different stores (Scrape().format_data()), it will be sent to a redis service as well to be written down.
Now whenever the job will be run, it first checks in the redis if the price in db and the stream is similar, if yes, then it will skip, if no, then observer pattern will
be used again here to update the data into different data stores as well
"""

"""
We can use python3 router.py to start the server
-> curl --location 'http://127.0.0.1:8000/v1' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer BYCVTUVULVHLVJNCFHCXCBLJXNOUIHGCYUBEIUEGUIYL' \
--data '{
    "url": "https://dentalstall.com/shop/",
    "page_no": "1"
}'

this is the curl request to hit and run the API
"""


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)