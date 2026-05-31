# Write a program to read three numbers from a user and check if the first number is greater or
# less than the other two numbers.

print('Enter first number:')
num1 = int(input())
print('Enter second number:')
num2 = int(input())
print('Enter third number:')
num3 = int(input())

if num1 > num2:
    if num1 > num3:
        print(num1, 'is greater than', num2, 'and', num3)
else:
    print(num1, 'is less than', num2, 'and', num3)

print('End of Nested if')
    