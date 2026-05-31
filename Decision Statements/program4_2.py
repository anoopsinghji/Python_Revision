# Write a program that prompts a user to enter two integer values. Print the message ‘Equals’ if 
# both the entered values are equal.

print('Enter firat number:')

num1 = int(input())

print('Enter second number:')
num2 = int(input())

if num1-num2==0:
    print('Both the entered values are equal.')