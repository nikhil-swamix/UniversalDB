"""
TITLE: 
    UniversalDB

AUTHOR:
    Nikhil Swami
    
DESCRIPTION:
    In this example we show how to use UniversalDB with Python
"""
import universaldb as udb

if __name__ == "__main__":
    # ---------- INIT
    db = udb("mongodb://localhost:27017/")  # use os.env variable in production!

    # ---------- DB->Collection
    employees = db["test"]['employees']

    # ---------- ADD DOCUMENT
    employees += {"name": "nikhil swami", "age": 23, "gender": "male", "salary": 10}
    print(employees)  # updated

    # ---------- FIND DOCUMENT
    print(employees[{"name": "nikhil swami"}])  # returns cursor object which is a generator, can convert to list
    print(list(employees[{"age": {"$lt": 25}}]))  # conditions supported just pass dict
    print(employees[{"age": {"$lt": 25}}][0])  # slicing supported

    # ---------- ALTERNATIVE PRINT
    employees.print(limit=3, reversed=True)  #  with limit and reverse, new line per doc
