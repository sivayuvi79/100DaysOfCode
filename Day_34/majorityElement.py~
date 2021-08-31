# https://practice.geeksforgeeks.org/problems/majority-element-1587115620/1#
class Solution:
    def majorityElement(self, A, N):
        #Your code here
        arr = sorted(A)
        pre = arr[0]
        count = 1
        max_count = -1
        f = 0
        for v in range(1, N):
            if arr[v] == pre:
                count += 1
            else:
                count = 1
                pre = arr[v]
            if max_count < count:
                max_count = count
                ele = arr[v]
                if max_count > (N//2):
                    f = 1
                    break
        if f == 1: return ele
        else: return -1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
