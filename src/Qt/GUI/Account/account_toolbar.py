from db.accounts import Accounts
from ORM.account import Account
from PySide.QtGui import QAction
from Qt.GUI.tab_toolbar import TabToolBar

import datetime

class AccountToolBar(TabToolBar):
    """ Represents the Account Tool Bar """

    def addToolBarButtons(self):
        """ Add Tool Bar Buttons """
        self.addNewAccountButton()
        self.addSeparator()

    def addNewAccountButton(self):
        """ Adds the New Account Button to the ToolBar """
        newIcon = self.getQIcon('vault.png')
        newAccountAction = QAction(newIcon, 'New Account', self)
        newAccountAction.setShortcut('Ctrl+N')
        newAccountAction.setStatusTip("Create a New Account.")
        newAccountAction.triggered.connect(self.newAccount)
        
        self.addAction(newAccountAction)

    def newAccount(self):
        """ Creates a New Account """
        account = Account(initial_balance=0, initial_balance_date=datetime.date.today())
        Accounts.add(account)
        self.table_view.insertRow(account)
        
    def tabSelected(self):
        """ Do Nothing when this tab is selected """