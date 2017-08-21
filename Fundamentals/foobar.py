#Tests if a number is a perfect square
def squareroot(num):
    results = [0, False]
    tracker = 1
    for i in range (1, num/2):
        if tracker * i == num and num % i == 0:
            results[0] = i
            results[1] = True
            break
        if tracker * i > num:
            results[0] =  i
            break
        tracker += 1
    return results

#squareroot(9)
#squareroot(100)
#squareroot(17)
        

#Tests if a number is prime - uses square function

def prime(num):
    testnum = squareroot(num)[0]
    for i in range(2, testnum):
        if num % i == 0:
            return False
    return True

#prime(12)
#prime(17)


#Foos and Bars numbers

def foo_bar():
    for num in range(100, 100001):
        if squareroot(num)[1]:
            print 'Bar'
            continue
        if prime(num):
            print 'Foo'
            continue
        print 'FooBar'
        
foo_bar()