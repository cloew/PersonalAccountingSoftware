from db.categories import Categories
from db.transactions import Transactions

class CategoryStatistics:
    """ Represents the Pie Chart of the Category Values """

    def getLabelsAndPercentages(self):
        """ Returns the labels and percentages for the Category Statistics """
        self.getCategoriesAndTransactions()
        self.getTotalExpenses()

        labels = self.getLabels()
        percentages = self.getPercentages()
        return labels, percentages

    def getCategoriesAndTransactions(self):
        """ Gets the categories and their associated Expense Transactions """
        self.categoryTransactions = {}
        for category in Categories.all():
            transactions = Transactions.allExpenseTransactionsForCategory(category)
            if len(transactions) > 0:
                self.categoryTransactions[category] = transactions

    def getTotalExpenses(self):
        """ Gets the Total Expenses """
        self.total = 0
        self.totalForCategory ={}
        for category in self.categoryTransactions:
            categoryTotal = 0
            for transaction in self.categoryTransactions[category]:
                categoryTotal += transaction.amount
            self.totalForCategory[category] = categoryTotal
            self.total += categoryTotal

    def getLabels(self):
        """ Return a list of the labels for the Categories """
        labels = []
        for category in self.categoryTransactions:
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
