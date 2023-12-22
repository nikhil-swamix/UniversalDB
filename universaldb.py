import sys
from typing import Any
import pymongo


class _Collection:
    """override read write methods"""

    def __init__(self, collection, selector_mode="one"):
        self.collection = collection
        self.selector_mode = selector_mode

    def print(self, limit=10, reversed=False):
        for item in (
            self.collection.find().limit(limit).sort("_id", pymongo.DESCENDING if reversed else pymongo.ASCENDING)
        ):
            print(item)

    # override += method
    def __iadd__(self, other):
        self.collection.insert_one(other)
        return self

    def __getitem__(self, item):
        if self.selector_mode == "one":
            return self.collection.find_one(item)
        elif self.selector_mode == "many":
            return self.collection.find(item)

    def __getattribute__(self, name):
        if name == "many":
            print('many mode activated')
            return _Collection(self.collection, "many")
        else:
            return object.__getattribute__(self, name)

    def __str__(self):
        return str([*self.collection.find()])


class _Database:
    def __init__(self, db):
        self.db = db

    def __getitem__(self, item):
        return _Collection(self.db[item])

    def __setitem__(self, key, value):
        pass


class _Client:
    def __init__(self, url, db="test", collection="test"):
        self.client = pymongo.MongoClient(url)

    # get subscript as a collection
    def __getitem__(self, item):
        # print("subscripted")
        return _Database(self.client[item])


def init(url):
    return _Client(url)


sys.modules[__name__] = init

if __name__ == "__main__":
    db = init("mongodb://localhost:27017/")
    r = db["test"]['employees']
    print(r)
    # r.print()
