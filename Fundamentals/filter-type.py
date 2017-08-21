from types import *

def filter_by_type(val):
    if type(val) is IntType:
        if val >= 100:
            print "That's a big number!"
        else:
            print "That's a small number"
        return
    elif type(val) is StringType:
        if len(val) >= 50:
            print "That's a long sentence!"
        else:
            print "That's a short sentence"
        return
    elif type(val) is ListType:
        if len(val) >= 10:
            print "Big list!"
        else:
            print "Small list"
        return
    return

filter_by_type("Rubber baby buggy bumpers")
filter_by_type(250)
filter_by_type(10)
filter_by_type([4,34,22,68,9,13,3,5,7,9,2,12,45,923])

#print type([4,34,22,68,9,13,3,5,7,9,2,12,45,923])