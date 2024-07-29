from apps.interface import ingest
import json
from validate import ValidateDict

class FileJson(ingest):
    def __init__(self, data):
        self.data_dict = data
        
    def validate(self):
        valid_instance = ValidateDict(self.data_dict)
        if valid_instance:
            self.write()
        else:
            print("invalid dict")  
    
    
    def write(self):
        file_name = "store/dummy.json"
        with open(file_name, 'a') as json_file:
            json.dump(self.data_dict, json_file)
            json_file.write('\n')
