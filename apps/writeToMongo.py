from common.db import MongoClient
from interface import ingest
from validate import ValidateDict

class WriteToMongo(ingest):
    def __init__(self, data):
        self.data_dict = data
        db = MongoClient().createClient()
        self.collectionName = "atlys_ingest"
        self.atlys_ingest = db[self.collectionName]
        
    def validate(self):
        valid_instance = ValidateDict(self.data_dict).validate_dict()
        if valid_instance:
            self.write()
        else:
            print("invalid dict")       
    
    def write(self):
        self.atlys_ingest.insert_one(self.data_dict)
