import universaldb as udb

if __name__ == "__main__":
    # ---------- INIT
    db = udb("mongodb://localhost:27017/")

    # ---------- DB->Collection
    employees = db["test"]['employees']

    # ---------- ADD DOCUMENT
    employees += {"name": "nikhil swami", "age": 23, "gender": "male", "salary": 10}
    print(employees)  # updated

    # ---------- ALTERNATIVE PRINT
    employees.print(limit=3, reversed=True)  #  with limit and reverse, new line per doc
