#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    res = f"{n:b}"
    count = 1
    test = []
    for i in range(1, len(res)):
        if res[i-1] == 0:
            pass
        else:
            if res[i-1] == res[i]:
                count += 1
            else:
                test.append(count)
                count = 1
    if count != 1: test.append(count)
    print(max(test))
