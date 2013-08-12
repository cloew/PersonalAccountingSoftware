from table_wrapper import TableWrapper
from ORM.account import Account


class AccountsWrapper(TableWrapper):
    """ Class to wrap interaction to the Accounts table in the database """
    table_class = Account
    
    def accountWithName(self, name):
        """ Return the account with the given name """
        account = None
        with self.session() as session:
            account = session.query(self.table_class).filter_by(name=name).first()
        return account

Accounts = AccountsWrapper()