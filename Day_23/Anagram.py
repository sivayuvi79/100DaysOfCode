#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    # Write your code here
    # print(s[0:1],'test')
    j = 1
    count = set()
    for i in s:
        k = 0
        test = []
        
        for a in range(0, (len(s)-j)+1):
            t = s[k:k+j]
            test.append(t)
            k += 1
        test_ = [sum((ord(l) for l in o)) for o in test]
        
        for h, v in enumerate(test):
            del test_[0]
            num = sum((ord(l) for l in v))
            if num in test_:
                count.add(num)
            test_.append(num)   
        j += 1
    return len(count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()

