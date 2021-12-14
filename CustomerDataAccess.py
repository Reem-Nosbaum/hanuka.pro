import sqlite3
from Customer import Customer


class CustomerDataAccess:

    def __init__(self, file_path):
        self.con = sqlite3.connect(file_path)
        self.cur = self.con.cursor()

    def print_all_costumers(self):
        self.cur.execute("SELECT * FROM Customer")
        for row in self.cur:
            print(row)

    def insert_customer(self, customer):
        self.cur.execute(f'INSERT INTO customer VALUES ({customer.id}, "{customer._fname}",' + \
                         f' "{customer._lname}", "{customer.address}", "{customer.mobile}") ')
        self.con.commit()

    def delete_customer(self, id):
        self.cur.execute(f'DELETE FROM customer WHERE id = {id}')
        self.con.commit()

    def get_all_customers(self):
        self.cur.execute(f'SELECT * FROM customer')
        _customers = []
        for person in self.cur:
            _customers.append(person)
        return _customers

    def update_customer(self, id, customer):
        self.cur.execute(f'UPDATE customer SET id = {customer.id}, fname = "{customer._fname}",' + \
                         f' lname = "{customer._lname}", address = "{customer.address}",' + \
                         f' mobile = "{customer.mobile}" WHERE id = {id}')
        self.con.commit()

    def get_customer_by_id(self, id):
        self.cur.execute(f'SELECT * FROM customer WHERE id = {id}')
        customer = None
        for row in self.cur:
            customer = Customer(row[0], row[1], row[2], row[3], row[4])
        return customer

    def get_customer_by_fname_and_lname(self, _fname, _lname):
        self.cur.execute(f'SELECT * FROM customer WHERE fname = "{_fname}" AND lname = "{_lname}"')
        customer = None
        for row in self.cur:
            customer = Customer(row[0], row[1], row[2], row[3], row[4])
        return customer
