from db.categories import Categories
from db.transactions import Transactions

from ORM.category import Category
from ORM.transaction import Transaction

import datetime

def AddCategory(name=""):
    my_category = Category(name=name)
    Categories.add(my_category)
    return my_category

def AddTransaction(description="", amount=0, income=False, date=datetime.date.today()):
    my_transaction = Transaction(description=description, amount=amount*100, income=income, date=date)
    Transactions.add(my_transaction)
    return my_transaction

def main():
    category = AddCategory(name="Gas")
    AddCategory(name="Groceries")
    AddCategory(name="Rent")
    AddCategory(name="Utilities")

    AddTransaction(description="Dinner", amount=251.00, income=False, date=datetime.datetime.now())
    transaction = AddTransaction(description="Gas", amount=35.00, income=False, date=datetime.date(2013, 3, 3))
    AddTransaction(description="Paycheck", amount=1000.00, income=True, date=datetime.date(2013, 3, 4))

    transaction.categories.append(category)
    Transactions.save()
    print transaction.categories

    print "\nCategories"
    print Categories.all()
    print "\nTransactions"
    print Transactions.all()

if __name__ == "__main__":
    main()