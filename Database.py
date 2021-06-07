from pymongo import MongoClient

class Database:

    def __init__(self):
        self._client = MongoClient(
            "mongodb+srv://rohit:rohit123@cluster0.gjvme.mongodb.net/Dataset?retryWrites=true&w=majority")

        self._db = self._client['Dataset']
        self._collection = self._db['data']

    def insert(self, data):
        res = self._collection.insert_one(data)
        print(res.inserted_id)
