#User function Template for python3

class Solution:
    def productExceptSelf(self, nums, n):
        #code here
        final = []
        # from functools import reduce
        # from operator import mul
        # import math
        '''for i in range(0, n):
            # print(nums[i:], nums[:i])
            if i == 0:
                res = nums[1:]
            elif i == n-1:
                res = nums[:n-1]
            else:
                res = nums[:i] + nums[i+1:]
            prod = 1
            for k in res:
                prod *= k
            final.append(prod)'''
        prod = 1
        for k in nums:
            # if k == 0:
                # k = 1
            prod*=k
        for i in nums:
            # if i == 0:
                # i = 1
            final.append(int(prod*(i**-1)))
        return final

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())

    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]

        ans=Solution().productExceptSelf(arr,n)
        print(*ans)
# } Driver Code Ends
