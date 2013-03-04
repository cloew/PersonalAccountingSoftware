from db.database import Database
from db.transactions import Transactions
from ORM.transaction import Transaction

import datetime

def main():
    """ Generate the Database """
    my_transaction = Transaction(description="Dinner", amount=251.00*100, income=False, date=datetime.datetime.now())
    print my_transaction
    print "ID:", str(my_transaction.id)

    Transactions.add(my_transaction)
    session = Database.getSession()
    saved_transaction = session.query(Transaction).filter_by(description="Dinner").first()
    print saved_transaction
    print "ID:", str(saved_transaction.id)

    print "Same?:", saved_transaction is my_transaction

    my_transaction.description = "New Description"
    Transactions.add(my_transaction)

    saved_transaction = session.query(Transaction).filter_by(description="New Description").first()
    print saved_transaction
    print "ID:", str(saved_transaction.id)

    print "Same?:", saved_transaction is my_transaction

if __name__ == "__main__":
    main()