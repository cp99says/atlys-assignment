from apps import writeToJsonFile, writeToMongo

curent_data_stores = ["FILE", "MONGO"]

stores_to_class_map = {
    "FILE": writeToJsonFile,
    "MONGO": writeToMongo
}

