from ORM.transaction import Transaction

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def main():
    """ Generate the Database """
    engine = create_engine('sqlite:///db/pas.db', echo=True)

    my_transaction = Transaction('Some Transaction')
    print "Name:", my_transaction.name
    print "ID:", str(my_transaction.id)

    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(my_transaction)
    saved_transaction = session.query(Transaction).filter_by(name='Some Transaction').first()
    print "Name:", saved_transaction.name
    print "ID:", str(saved_transaction.id)

    print "Same?:", saved_transaction is my_transaction

    my_transaction.name = "New Transaction Name"

    print session.dirty

    session.commit()

    saved_transaction = session.query(Transaction).filter_by(name='New Transaction Name').first()
    print "Name:", saved_transaction.name
    print "ID:", str(saved_transaction.id)

    print "Same?:", saved_transaction is my_transaction

if __name__ == "__main__":
    main()