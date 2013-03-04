from ORM.transaction import Transaction

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import datetime

def main():
    """ Generate the Database """
    engine = create_engine('sqlite:///db/pas.db', echo=True)

    my_transaction = Transaction(description="Dinner", amount=251.00*100, income=False, date=datetime.datetime.now())
    print my_transaction
    print "ID:", str(my_transaction.id)

    Session = sessionmaker(bind=engine)
    session = Session()

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