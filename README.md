# Unified architecture for different DB Vendors 

- Manage DB Connections using Just Env Files, auto scan Credentials or use default! `db = udb("mongodb")['movies_app']` explain:` #mongodb=engine, movies_app=db name ` thats it. 
- Database Operations using Operators and Native Syntax! `db['all_movies'] += {'name':'Titanic',...}` explain:` #all_movies=collection name` yes it gets added!
- utility print function ` db['all_movies'].print(limit=3, reversed=True)`
- Support Coming soon for : Supabase, Firebase, SQLite, Postgres, ScyllaDB


## Getting Started

To get started with the codebase, follow these steps:

1. Install the necessary dependencies, including `pymongo`, by running the command: `pip install pymongo universaldb`.

2. Import the codebase into your project by including the following import statements:

```python
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

```
## Features

-   **Native Syntax**: Perform database operations using operators and syntax that closely resemble native MongoDB queries. This allows you to leverage your existing knowledge of
    MongoDB to work with the codebase effortlessly.

-   **Customizable Plug n Play**: The codebase provides a set of classes - `_Collection`, `_Database`, and `_Client` - that abstract away the complexities of interacting with MongoDB.
    These classes offer intuitive methods and attributes to access, manipulate, and query your database.

-   **Printing Documents**: Easily print documents from a collection using the `print` method provided by the `_Collection` class. You can specify the number of documents to
    display and even reverse the order if needed.

-   **Insertion Operator Overload**: The `_Collection` class supports the `+=` operator overload, allowing you to insert documents into a collection with a single line of code.
    Simply use the `+=` operator with the document you want to insert.

-   **Selector Modes**: The `_Collection` class supports selector modes - "one" and "many" - to retrieve documents from a collection. This allows you to customize the behavior of
    document retrieval based on your specific needs.

-   **Database Access**: The `_Database` class enables easy access to collections within a MongoDB database. Simply use the square bracket syntax to retrieve a collection by name.



# Contributing

Contributions to this codebase are welcome! If you encounter any issues, have suggestions for improvements, or want to contribute new features, feel free to open an issue or submit
a pull request on GitHub.

# License

This codebase is licensed under the MIT License. Feel free to use it in your projects, modify it, and distribute it.

# Contact

If you have any questions or need further assistance, please don't hesitate to reach out. nikhilswami1@gmail.com

**Important : yet to be published on pypi**
This Package  simplifies and gives developer-friendly interface to interact with a MongoDB/supabase database gives you First Class Support perform database operations using operators and native syntax for MongoDB. otherwise they are simply unused. . With its intuitive syntax and powerful features, it aims to make working with databases a breeze. 
