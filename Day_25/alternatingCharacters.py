#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternatingCharacters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternatingCharacters(s):
    # Write your code here
    count = 0
    if s.count('A') == len(s) or s.count('B') == len(s):
        print(len(s)-1)
        return len(s)-1
    else:
        if s[0] == 'A':
            cur = 'A'
            for i, v in enumerate(s[1:]):
                if v != cur:
                    cur = s[i+1]
                else:
                    count += 1
        if s[0] == 'B':
            cur = 'B'
            for i, v in enumerate(s[1:]):
                if v != cur:
                    cur = s[i+1]
                else:
                    count += 1
        return count
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()

