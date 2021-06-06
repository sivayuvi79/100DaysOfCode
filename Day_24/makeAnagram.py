#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def makeAnagram(a, b):
    # Write your code here
    str_a = dict(Counter(a))
    str_b = dict(Counter(b))
    set_a = set(str_a.items())
    set_b = set(str_b.items())
    return sum(dict(set_a ^ set_b).values())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()

