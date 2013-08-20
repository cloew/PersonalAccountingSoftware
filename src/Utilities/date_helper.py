from dateutil import parser

def DateToString(date):
    """ Returns a string format of the given date """
    return "{0:%m/%d/%Y}".format(date)
    
def StringToDate(dateString):
    """ Converts a String to a date """
    return parser.parse(value)