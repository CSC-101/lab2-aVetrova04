#PART 1
def smallest(n:float, m:float) -> float:
    if n < m:
        return n             # For which calls below is this statement evaluated?
    else:                           #return n is evaluated for neither of the function
        return m                    #calls because in neither case is n strictly less than m

first = smallest(3, 2)       # What is the value of first?
                                            #the value of first is 2
second = smallest(2, 2)      # What is the value of second? Is this a reasonable result? Why or why not?
print()                                     #the value of second is also 2. it is consistent
                                            #with how the function is defined, however, it
                                            #would be nice to add an else to return an additional
                                            #message that the two inputted values are equal

#PART 2
def function2(a:int, b:int, c:int) -> int:
    if a > b and a > c:
        return a - b             # In general, when will a call to this function evaluate this statement?
    elif b > c:                         #If "a" is the largest value.
        return b + c             # In general, when will a call to this function evaluate this statement?
    else:                               #If "b" is the largest value.
        return 2 * c             # In general, when will a call to this function evaluate this statement?
                                        #If "c" is the largest value.

answer1 = function2(3, 2, 1)     # What is the value of answer1?
                                                #3
answer2 = function2(2, 3, 1)     # What is the value of answer2?
                                                #3
answer3 = function2(2, 1, 3)     # What is the value of answer3?
                                                #3
print()
