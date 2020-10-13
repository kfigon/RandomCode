from typing import List

# write a function which takes in two strings and checks whether 
# the characters in the first string form a subsequence 
# of the characters in the second string. 
# 
# In other words, the function should check whether the characters
# in the first string appear somewhere in the second string, 

# O(N+M)
def isSubsequence(a:str, b:str) -> bool:
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            i+=1
        j+=1
    
    return i >= len(a)

assert isSubsequence('hello','hello world') == True
assert isSubsequence('sing','sting') == True
assert isSubsequence('abc','abracadabra') == True
assert isSubsequence('abc','acb') == False # order matters
