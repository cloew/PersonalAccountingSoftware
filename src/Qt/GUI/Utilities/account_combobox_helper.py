from db.accounts import Accounts

def UpdateComboBoxWithAccounts(comboBox, ignoreCurrent=False, table_view=None):
        """ Update Combo Box """
        names = GetAccountNames()
        if ignoreCurrent:
            names.remove(table_view.account.name)
        comboBox.clear()
        comboBox.addItems(names)
        
def GetAccountNames():
    """ Return Account Names """
    names = []
    for account in Accounts.all():
        if account.name is not None:
            names.append(account.name)
    return names