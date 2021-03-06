from decimal import Decimal

def GetDollarString(amountInCents):
    """ Return a dollar amount as a string """
    filler = ""
    if amountInCents is None:
        amountInCents = 0
    if amountInCents < 0:
        amountInCents = amountInCents*-1
        filler = "-"
    dollars, cents = divmod(amountInCents, 100)
    return "${0}{1:,}.{2:{fill}2}".format(filler, dollars, cents, fill=0)

def GetCentsFromDollarString(dollarString):
    """ Returns an int of the number of cents the dollar string represents.
        Note: Throws an InvalidOperation if the Sring cannot be converted to a Decimal object """
    cleanedDollarString = dollarString.replace(",", "")
    if cleanedDollarString.startswith('$'):
        cleanedDollarString = cleanedDollarString[1:]
    newAmount = Decimal(cleanedDollarString)
    return int(newAmount*100)