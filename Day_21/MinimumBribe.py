#!/bin/python3

import math
import os
import random
import re
import sys


def minimumBribes(q):
    count = 0
    q = [k-1 for k in q]
    for i, v in enumerate(q):
        if v-i > 2:
            print('Too chaotic')
            return
        for j in range(max(v-1, 0), i):
            if q[j] > v:
                count+=1
    print(count)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

