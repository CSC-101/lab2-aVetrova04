#PART 1
from typing import Optional             # gain access to the Optional[X] type hint


def checked_access(L:list[int], idx:int) -> Optional[int]:
    test = idx >= 0 and idx < len(L)    # What is the value of test on each call?
                                                #test is False for first and True for second call
    if test:                            # What is this check preventing?
        return L[idx]                           #an index outside of bounds of L
    else:
        return None


first = checked_access([1, 0, 1], 9)     # What is the value of first?
                                                        #None
second = checked_access([1, 0, 1], 2)    # What is the value of second?
                                                        #1
print()

#PART 2
def length_sum(L:list[str]) -> int:
    if len(L) > 2:
        result = len(L[0]) + len(L[1]) + len(L[2])    # For which call below is this statement evaluated
    elif len(L) > 1:                                  #   and what are the values being added?
                                                            #the call the result of which is in "first"
                                                            #"this" + "is" + "the"
        result = len(L[0]) + len(L[1])                # For which call below is this statement evaluated
    elif len(L) > 0:                                  #   and what are the values being added?
                                                            #the call the result of which is in "third"
                                                            #"another" + "call"
        result = len(L[0])                            # For which call below is this statement evaluated
    else:                                             # and what are the values being added?
        result = 0                                          #the call the result of which is in "second"
                                                            #no addition. returns just "second call"
    return result


first = length_sum(["this", "is", "the", "first", "call"])
second = length_sum(["second call"])
third = length_sum(["another", "call"])
print()

#PART 3
def surprising(L:list[str], other:str) -> list[str]:
    L.append(other.upper())
    return L


words = ["this", "is", "confusing", "code."]
first = surprising(words, "Avoid")
second = surprising(words, "such.")
         # What is the value of words at this point?
                #words = ["this", "is", "confusing", "code.", "AVOID", "SUCH."]
         # What are the values of first and second at this point?
                #first = ["this", "is", "confusing", "code.", "AVOID"]
                #second = ["this", "is", "confusing", "code.", "SUCH."]
         # What happened?
'''first and second took on the array of strings of "words" with
their respective statements ("AVOID" and "SUCH.") appended'''

print()