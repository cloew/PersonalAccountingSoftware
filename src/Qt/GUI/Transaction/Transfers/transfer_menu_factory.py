from db.accounts import Accounts
from Qt.GUI.Transaction.Transfers.new_transfer_action import NewTransferAction

def AddTransferActionsToWidgetContextMenu(widget, transaction):
    """ Add Transfer Actions to the Widget Context Menu """
    widget.setContextMenuPolicy(Qt.ActionsContextMenu)
    for account in Accounts.all():
        if transaction.account is account:
            continue
        action = NewTransferAction(transaction, widget, account)
        widget.addAction(action)
    