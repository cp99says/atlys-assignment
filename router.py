from fastapi import FastAPI

app = FastAPI()

@app.get("/data/{page_no}")
def get_items(page_no):
    

