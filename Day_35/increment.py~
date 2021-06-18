#User function Template for python3
# https://practice.geeksforgeeks.org/problems/plus-one/1/#

class Solution:
    def increment(self, arr, N):
        # code here
        # arr = (str(i) for i in arr)
        # return str(int("".join(arr))+1).zfill(N)
        # if arr[-1] != 9:
            
        arr = arr[::-1]
        arr[0] += 1
        carry = arr[0]/10
        arr[0] = arr[0]%10
        
        for i in range(1, len(arr)):
            if carry == 1:
                arr[i] += 1
                carry = arr[i]/10
                arr[i] = arr[i]%10
        if carry == 1:
            arr.append(1)
                
                
        return arr[::-1]
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        ptr = ob.increment(arr,N)
        for i in ptr:
            print(i,end=" ")
        print()
# } Driver Code Ends
