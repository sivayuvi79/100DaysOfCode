#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    count = n
    loop_count = 2
    def special_case(srt):
        srt_len = len(srt)
        if srt.count(srt[0]) == srt_len: 
            return 1
        else:
            if srt_len % 2 == 0:
                check = int(srt_len/2)
                srt_1 = srt[:check]
                srt_2 = srt[check:]
                if (srt_1 == srt_2) and (srt_1.count(srt_1[0]) == len(srt_1)):
                    return 1
                else:
                    return 0
            else:
                check = int(srt_len//2)
                srt_1 = srt[:check]
                srt_2 = srt[check+1:]
                if (srt_1 == srt_2) and (srt_1.count(srt_1[0]) == len(srt_1)):
                    return 1
                else:
                    return 0
    while n >= loop_count:
        for i in range(n):
            test = s[i:i+loop_count]
            if len(test) == loop_count:
                count += special_case(test)
            else:
                break
        loop_count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

