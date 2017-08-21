#Multiples

#Part One

def odd_print():
    for num in range(1, 1000):
        if (num % 2 == 0):
            continue
        print num

#odd_print() 


#Part Two

def multiples_of_five():
    peak = 1000000 / 5
    for mult in range (5, peak + 1):
        print 5 * mult

#multiples_of_five()

#Sum

def sum_of_list(lst):
    lstsum = 0
    for item in lst:
        lstsum = lstsum + item
    print lstsum
    return lstsum

#sum_of_list([1,2,3,4,5,6,7,8,9,10])

#Average

def list_avg(lst):
    print sum_of_list(lst) / (len(lst) *1.0)

list_avg([1,2,3,4,5,6,7,8,9,10])