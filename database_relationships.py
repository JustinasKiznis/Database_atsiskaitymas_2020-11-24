# with DatabaseContextManager("relationships") as db:
#     db.execute(query, parameters)

# "Foreign key table"
# Table = "Customers"
# Fields = [customer_id,first_name, last_name, age, Foreign Key (compnay_id) References Companies(company_id)]

# Table = "Companies"
# Fields = [company_id,company_name, employee_count]

# JOIN OUTPUT: 1,John,johnathan, 30, 2 , 2 , Google, 500


import sqlite3

class DatabaseContextManager(object):
    """This class exists for us to use less lines of code than necessary for queries.
        __init__: used to set database file name.
        __enter__: opens connection and creates cursor.
        __exit__: commits the changes to database file and closes connection."""

    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()


#Customer CRUD---------------------------------------------------------------------------------

def create_table_customers():
    query = """CREATE TABLE IF NOT EXISTS Customers(
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    age INTEGER,
    comp_id INTEGER,
    FOREIGN KEY (comp_id) REFERENCES Companies(company_id))"""
    with DatabaseContextManager("db") as db:
        db.execute(query)

def create_customers(first_name: str, last_name: str, age: int, comp_id: int):
    query = """INSERT INTO Customers(first_name, last_name, age, comp_id) VALUES(?,?,?,?)"""
    parameters = [first_name, last_name, age, comp_id]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


# Read function
def get_customers():
    query = """SELECT * FROM Customers"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)
    print("------------------------------------------------------")
    # print for convenience in terminal


# Update function
def update_customer_adress(new_company: int, first_name: str, last_name: str):
    query = """UPDATE Customers
                SET comp_id = ?
                WHERE first_name = ? AND last_name= ?"""
    parameters = [new_company, first_name, last_name]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


# Delete function
def delete_customer(id: int):
    query = """DELETE FROM Customers
                WHERE customer_id = ?"""
    parameters = [id]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


#Company CRUD--------------------------------------------------------------------------------------------------

def create_table_companies():
    query = """CREATE TABLE IF NOT EXISTS Companies(
    company_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT,
    employee_count TEXT)"""
    with DatabaseContextManager("db") as db:
        db.execute(query)


def create_Companies(company_name: str, employee_count: int):
    query = """INSERT INTO Companies(company_name, employee_count) VALUES(?,?)"""
    parameters = [company_name, employee_count]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


# Read function
def get_Companies():
    query = """SELECT * FROM Companies"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)
    print("------------------------------------------------------")


# Update function
def update_Companies_employee_count(new_count: int, company_name: str):
    query = """UPDATE Companies
                SET employee_count = ?
                WHERE company_name = ?"""
    parameters = [new_count, company_name]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


# Delete function
def delete_Companies(id: int):
    query = """DELETE FROM Companies
                WHERE company_id = ?"""
    parameters = [id]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)

#---------------------------------------------------------------------------------------------------------

def get_Customers_info():
    query = """SELECT * FROM Customers
                JOIN Companies
                    ON Customers.comp_id = Companies.company_id"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for row in db.fetchall():
            print(row)




create_table_customers()
create_table_companies()

create_customers("Jonas", "Jonaitis",30, 1)
create_Companies("Google", 35000)

get_Customers_info()