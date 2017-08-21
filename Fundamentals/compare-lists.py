def compare_lists(list_one, list_two):
    same = True
    if len(list_one) == len(list_two):
        for i in range (len(list_one)):
            if list_one[i] != list_two[i]:
                same = False
                break
    else:
        same = False
    if same:
        print "The lists are the same"
    else:
        print "The lists are not the same"



list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]
compare_lists(list_one, list_two)
strings_one = ['celery','carrots','bread','milk']
strings_two = ['celery','carrots','bread','cream']
compare_lists(strings_one, strings_two)
        