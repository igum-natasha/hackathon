from pymongo import MongoClient
import pandas as pd


class DataBase:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.file = '' #csv file name
        self.data = []

    def write_db(self, child: str):
        db = self.client.test
        if child not in db.list_collection_names():
            data_child = db[child]
            df = pd.read_csv(self.file)
            records_ = df.to_dict(orient='records')
            data_child.insert_many(records_)

    def find_doc(self, child: str):
        db = self.client.test
        if child in db.list_collection_names():
            results = 1
        else:
            results = -1
        for x in db[child].find():
            self.data.append(x)
        if results != -1:
            return self.data
        return 0

