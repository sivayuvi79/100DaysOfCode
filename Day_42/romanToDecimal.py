#User function Template for python3



def romanToDecimal(str):
    # code here
    map_dict = {
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000,
    }
    num = 0
    inp = str[::-1]
    pre = map_dict[inp[0]]
    for i in inp:
        cur = map_dict[i]
        if pre < cur or pre == cur:
            num += map_dict[i]
        elif cur < pre:
            num -= map_dict[i]
        pre = cur
    return num

#{ 
#  Driver Code Starts
#Initial Template for Python 3




if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        print(romanToDecimal(str(input())))
# } Driver Code Ends
