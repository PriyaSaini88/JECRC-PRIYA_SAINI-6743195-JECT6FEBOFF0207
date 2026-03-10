'''
1. Lambda is a keyword, which is used to create anonymous functions.
2. For calling the lambda function, we can store the address of lamda inside a variable. By invoking the var_name, we can call the functions.

'''
'''
var_name = lambda args: <exp>
var_name(args) ## calling the lambda function

'''

# lambda args: <exp>
# result = lambda a, b: a+b ## returns value
# print(result)
# print(result(1, 2))

# (lambda a, b: print(a+b))int((input('First Num'))) int(input('Second Num:'))


## WAP to find the square of a number if it's even

# num = int(input('Enter number:'))
# if num % 2 == 0:
#     print(num ** 2)  ## num * num

# lambda num: print(num ** 2) if num%2 == 0 else None

# result = lambda num: print(num ** 2) if num%2 == 0 else None
# result(12)


## WAP to find square of a number if it is even otherwise print cubbe of number
# num = int(input('Enter a number:'))
# result= lambda num: print(num ** 2) if num%2 ==0 else print(num ** 3)
# # result(12)
# # result(19)
# result(int(input()))

## Check whether a num is positive or negative or zero

# num = int(input())

# if num > 0:
#     print('pos')
# else:
#     if num < 0:
#         print('neg')
#     else:
#         print('zero')


result = lambda num: print('pos') if num > 0 else print('neg') if num < 0 else print('Zero')
result(int(input()))









