from db.database import Database
from ORM.transaction import Transaction

import datetime

def main():
    """ Generate the Database """
    my_transaction = Transaction(description="Dinner", amount=251.00*100, income=False, date=datetime.datetime.now())
    print my_transaction
    print "ID:", str(my_transaction.id)

    session = Database.getSession()

    session.add(my_transaction)
    saved_transaction = session.query(Transaction).filter_by(description="Dinner").first()
    print saved_transaction
    print "ID:", str(saved_transaction.id)

    print "Same?:", saved_transaction is my_transaction

    my_transaction.description = "New Description"

    print session.dirty

    session.commit()

    saved_transaction = session.query(Transaction).filter_by(description="New Description").first()
    print saved_transaction
    print "ID:", str(saved_transaction.id)

    print "Same?:", saved_transaction is my_transaction

if __name__ == "__main__":
    main()