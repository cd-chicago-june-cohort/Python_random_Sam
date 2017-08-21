def find_and_replace(str, sub, rep):
    pos = str.find(sub)
    print pos
    newstr = str.replace(sub, rep)
    print newstr

find_and_replace("It's thanksgiving day. It's my birthday,too!", "day", "month")

def min_and_max(lst):
    print min(lst)
    print max(lst)

min_and_max([1,2,3,4,5,6,7,8])

def first_and_last(lst):
    first = lst[0]
    last = lst[len(lst) - 1]
    print first, last
    newlst = [first, last]
    print newlst
    return newlst

first_and_last([1,5,4,'string', 8, 'lion', 'tiger'])

def new_list (lst):
    lst.sort()
    half = len(lst) / 2
    firstlst = lst[0:half]
    secondlst = lst[half-1: len(lst)]
    secondlst[0] = firstlst
    print secondlst
    return secondlst

new_list([12,11,-10,9,-8,-3,7,6,5,-19,29,435,99])

