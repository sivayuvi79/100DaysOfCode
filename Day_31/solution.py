#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#

def getMax(operations):
    # Write your code here
    res = []
    maxi = 0
    for v in operations:
        if v == '2':
           res.pop()
           if v == maxi:
            maxi = max(res + [0])
        elif v == '3':
            print(max(res))
        else:
            k = v.split()
            res.append((int(k[1])))
            maxi = max(int(k[1]), maxi)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()

