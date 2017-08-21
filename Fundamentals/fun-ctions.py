def odd_even():
    for num in range(1,2001):
        if num % 2 == 0:
            print "Number is " + str(num) + ". This is an even number"
        else:
            print "Number is " + str(num) + ". This is an odd number"

#odd_even()

def multiply(nums, x):
    for i in range(len(nums)):
        nums[i] = nums[i]*x
    return nums

#multiply([2,4,6,8,10],10)

def layered_multiples(lst):
    newlst = []
    inlst = []
    for i in range(len(lst)):
        r = lst[i]
        for j in range (r):
            inlst.append(1)
        newlst.append(inlst)
        inlst = []
    print newlst
    return newlst

layered_multiples(multiply([2,6,10], 2))
