#range vs enumrator Practice

'''
Fizz buzz problem
If the number diveded by 3 we call it as Fizz
If the number diveded by 5 we call it as Buzz
If the number diveded by both 3 and 5 we call it as Fizz - buzz
'''
number = [23, 45,62,75,59]

for i in range(len(number)):
    if number[i]%3 == 0:
        result = 'Fizz'
    if number[i]%5 == 0:
        result = 'Buzz'
    if number[i]%3 == 0 and number[i]%5 == 0:
        result = 'Fizz-Buzz'
    else:
        result = number[i]
#     nu?mber[i] = result

for i, num in enumerate(number):
    if num%3 == 0:
        result = 'Fizz'
    if num%5 == 0:
        result = 'Buzz'
    if num%3 == 0 and num%5 == 0:
        result = 'Fizz-Buzz'
    else:
        result = num
    number[i] = result
number