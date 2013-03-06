from db.database import Database
from db.transactions import Transactions
from ORM.transaction import Transaction
from Qt.GUI.main_window_controller import MainWindowController

import datetime

def AddTransaction(description="", amount=0, income=False, date=datetime.date.today()):
    my_transaction = Transaction(description=description, amount=amount*100, income=income, date=date)
    Transactions.add(my_transaction)

def main():
    """ Generate the Database """
    # AddTransaction(description="Dinner", amount=251.00, income=False, date=datetime.datetime.now())
    # AddTransaction(description="Gas", amount=35.00, income=False, date=datetime.date(2013, 3, 3))
    # AddTransaction(description="Paycheck", amount=1000.00, income=True, date=datetime.date(2013, 3, 4))

    controller = MainWindowController()
    controller.run()

if __name__ == "__main__":
    main()