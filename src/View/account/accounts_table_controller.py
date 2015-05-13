from knot import KnotService, has_scope

@has_scope
class AccountsTableController:
    """ Controller to provide the accounts for the Accounts Table """
    _accounts = KnotService('accounts')
    
    @property
    def accounts(self):
        """ Return the accounts from the database """
        return self._accounts.all()