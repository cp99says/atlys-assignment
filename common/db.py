import pymongo

DB = "atlys"
connection_string = f"mongodb+srv://cp99says:cp99says@cluster0.r2paftd.mongodb.net/{DB}?retryWrites=true&w=majority&appName=Cluster0"
class MongoClient:
    def __init__(self):
        self.connection_string = connection_string
    def createClient(self):
        client = pymongo.MongoClient(self.connection_string)
        db = client[DB]
        return db
