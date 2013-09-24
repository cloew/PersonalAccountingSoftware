from db.categories import Categories
from db.transactions import Transactions

from datetime import datetime

class CategoryStatistics:
    """ Represents the Pie Chart of the Category Values """
    
    def __init__(self):
        """ Initialize Category Statistics """
        today = datetime.today()
        self.month = today.month
        self.year = today.year

    def getLabelsAndPercentages(self):
        """ Returns the labels and percentages for the Category Statistics """
        self.prepareStatistics()

        labels = self.getLabels()
        percentages = self.getPercentages()
        return labels, percentages

    def prepareStatistics(self):
        """ Prepare the Statistics """
        self.getCategoriesAndTransactions()
        self.getTotalExpenses()

    def getCategoriesAndTransactions(self):
        """ Gets the categories and their associated Expense Transactions """
        self.categoryTransactions = {}
        for category in Categories.all():
            transactions = Transactions.allExpenseTransactionsForCategory(category, self.month, self.year)
            if len(transactions) > 0:
                self.categoryTransactions[category] = transactions

    def getTotalExpenses(self):
        """ Gets the Total Expenses """
        self.total = 0
        self.totalForCategory ={}
        for category in self.categoryTransactions:
            categoryTotal = 0
            for transaction in self.categoryTransactions[category]:
                if transaction.subtransaction_set is not None:
                    amount = 0
                    for subtransaction in transaction.subtransaction_set.transactions:
                        amount -= subtransaction.getValue()
                    categoryTotal += amount
                else:
                    if transaction.amount is not None:
                        categoryTotal += transaction.amount
            self.totalForCategory[category] = categoryTotal
            self.total += categoryTotal

    def getLabels(self):
        """ Return a list of the labels for the Categories """
        labels = []
        for category in self.totalForCategory:
            labels.append(category.name)
        return labels

    def getPercentages(self):
        """ Return a list of percentages """
        percentages = []
        for category in self.totalForCategory:
            percentages.append(float(self.totalForCategory[category])/self.total)
        return percentages

    def getExpenseTransactionsForCategory(self, category):
        """ Return a list of the Expense Transactions for the given category """
        transactions = category.transactions
