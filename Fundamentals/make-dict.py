def make_dict(lst1, lst2):
    if len(lst2) > len(lst1):
        keylist = lst2
        vallist = lst1
    else:
        keylist = lst1
        vallist = lst2
    new_dict = {}
    for i in range(len(vallist)):
        new_key = keylist[i]
        new_dict[new_key] = vallist[i]
    print new_dict
    return new_dict

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

make_dict(name, favorite_animal)