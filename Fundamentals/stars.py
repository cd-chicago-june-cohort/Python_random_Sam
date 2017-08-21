from types import *

def stars(lst):
    for i in range(len(lst)):
        print '*' * lst[i]

stars([2,4,6,8])

def stars_part_two(lst):
    for i in range(len(lst)):
        if type(lst[i]) is IntType:
            print "*" * lst[i]
        else:
            print lst[i][0].lower() * len(lst[i])

stars_part_two([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])