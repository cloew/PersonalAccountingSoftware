from db.accounts import Accounts
from db.categories import Categories
from db.transactions import Transactions

from ORM.account import Account
from ORM.category import Category
from ORM.transaction import Transaction

import datetime

def AddAccount(name="", balance=0):
    my_account = Account(name=name, initial_balance=int(balance*100), initial_balance_date=datetime.date(2013, 8, 1))
    Accounts.add(my_account)
    return my_account

def AddCategory(name=""):
    my_category = Category(name=name)
    Categories.add(my_category)
    return my_category

def AddTransaction(description="", amount=0, income=False, date=datetime.date.today(), cleared=None, account=None):
    my_transaction = Transaction(description=description, amount=amount*100, income=income, date=date, cleared=cleared)
    Transactions.add(my_transaction)
    my_transaction.account = account
    return my_transaction

def main():
    account = AddAccount(name="Checking Account", balance=10000)

    category = AddCategory(name="Gas")
    AddCategory(name="Groceries")
    AddCategory(name="Rent")
    AddCategory(name="Utilities")

    AddTransaction(description="Dinner", amount=251.00, income=False, date=datetime.datetime.now(), account=account)
    transaction = AddTransaction(description="Gas", amount=35.00, income=False, date=datetime.date(2013, 3, 3), account=account)
    AddTransaction(description="Paycheck", amount=1000.00, income=True, date=datetime.date(2013, 3, 4), account=account)

    transaction.category = category
    Transactions.save()
    print transaction.category

    print "\nCategories"
    print Categories.all()
    print "\nTransactions"
    print Transactions.all()

if __name__ == "__main__":
    main()