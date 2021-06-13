#!/bin/python3

#https://www.hackerrank.com/challenges/30-2d-arrays/problem

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    old = []
    for i,j in enumerate(arr):
        check = arr[i:i+3]
        for a in range(6):
            b = []
            for k in check:
                if a < 4:
                    fi = k[a:a+3]
                    b.append(fi)
            if b !=[]: # loop preventing
                old.append(sum(b[:][0]) + (b[:][1][1]) + sum(b[:][2]))
        if arr[i+2] == arr[len(arr)-1]: # loop preventing
            break
    print(max(old))

