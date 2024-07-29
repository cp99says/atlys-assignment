from apps.writeToJsonFile import FileJson
from apps.writeToMongo import WriteToMongo

curent_data_stores = ["FILE", "MONGO"]

stores_to_class_map = {
    "FILE": FileJson,
    "MONGO": WriteToMongo
}


class Run:
    def __init__(self, data):
        self.data_dict = data
    
    def ingest(self):
        for stores in curent_data_stores:
            class_to_call = stores_to_class_map.get(stores)(self.data_dict)
            class_to_call.validate()
