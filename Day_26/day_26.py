# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
t = int(input())
phone_book = {}
for i in range(t):
    a = input().split()
    phone_book[a[0]] = a[1]
tests = []
while True:
    try:
        tests.append(input())
    except Exception as e:
        break
for k in tests:
    if k in phone_book:
        print(f"{k}={phone_book[k]}")
    else:
        print('Not found')

