#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    count = 0
    j = 0
    for i, v in enumerate(c):
        if j == len(c) - 1:
            pass
        elif j == len(c) - 2:
            if c[j] == 0 and c[j+1] == 0:
                count += 1
                j += 1
        elif c[j] == 0 and c[j+2] == 0:
            j += 2
            count += 1
        elif c[j] == 0 and c[j+1] == 0:
                count += 1
                j += 1
        else:
            j += 1
    return count
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()

