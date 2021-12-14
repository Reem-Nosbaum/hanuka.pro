import sqlite3
from Customer import Customer
from CustomerDataAccess import CustomerDataAccess


def menu():
    return f'1. Get all customers \n2. Get customer by id \n3. Insert customer' +\
           f' \n4. Delete customer \n5. Update customer \n6. Exit \nPlease enter your choose: '


def get_customer():
    id = int(input('Enter id: '))
    customer = con.get_customer_by_id(id)
    if customer is not None:
        print(customer)


def insert():
    _id = int(input('Enter id: '))
    _fname = str(input('Enter first name: '))
    _lname = str(input('Enter last name: '))
    if chek(_fname, _lname) != 'yes':
        return
    _address = str(input('Enter address: '))
    _mobile = str(input('Enter mobile: '))
    customer = Customer(_id, _fname, _lname, _address, _mobile)
    con.insert_customer(customer)
    print('Updated successfully')


def delete():
    id = int(input('Enter id: '))
    if con.get_customer_by_id(id) is not None:
        con.delete_customer(id)
        print('Records updated successfully')


def chek(f_name, l_name):
    if con.get_customer_by_fname_and_lname(f_name, l_name) is not None:
        return str(input('are you sure? '))
    return 'yes'


def update():
    id = int(input('Enter the current id: '))
    if con.get_customer_by_id(id) is None:
        print('customer with the specified id does not exist')
        return
    _id = int(input('Enter the new id:'))
    if con.get_customer_by_id(_id) is not None and _id != id:
        print('customer with the same id already exist')
        return
    f_name = str(input('Enter first name: '))
    l_name = str(input('Enter last name: '))
    _address = str(input('Enter address: '))
    _mobile = str(input('Enter mobile: '))
    customer = Customer(_id, f_name, l_name, _address, _mobile)
    con.update_customer(id, customer)
    print('Updated successfully')


def action_selector(num_choose):
    if num_choose == 1:
        con.print_all_costumers()
    elif num_choose == 2:
        get_customer()
    elif num_choose == 3:
        insert()
    elif num_choose == 4:
        delete()
    elif num_choose == 5:
        update()


def main():
    num_choose = int(input(f'\n{menu()}'))
    while num_choose != 6:
        if 6 < num_choose or num_choose < 1:
            num_choose = int(input(f'\nYour input is not correct \n{menu()}'))
            continue
        else:
            action_selector(num_choose)
        num_choose = int(input(f'\n{menu()}'))
    print('Good bye!')


con = CustomerDataAccess('/Users/reem/PycharmProjects/hanuka/SQL/hanuka.pro.db')
main()
sqlite3.connect('/Users/reem/PycharmProjects/hanuka/SQL/hanuka.pro.db').close()

