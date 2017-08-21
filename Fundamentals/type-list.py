from types import *

def list_type_messages(lst):
    intlst = True
    strlst = True
    string = "String: "
    numsum = 0
    for item in lst:
        if type(item) is StringType:
            string = string + ' ' + item
            intlst = False 
        else:
            numsum = numsum + item
            strlst = False
    if not intlst and not strlst:
        print 'The list you input is of mixed type'
        print string
        print 'Sum: ' + str(numsum)
    elif intlst:
        print 'The list you input is of integer type'
        print 'Sum: ' + str(numsum)
    elif strlst:
        print 'The list you input is of string type'
        print string
    
list_type_messages(['magical unicorns',19,'hello',98.98,'world'])
list_type_messages([2,3,1,7,4,12])
list_type_messages(['magical','unicorns','are','pretty'])
        
        