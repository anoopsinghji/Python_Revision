# Write a program to print even numbers from 0 to 10 and fi nd their sum.

sum = 0
for i in range(0,11,2):
    print(i)
    sum = sum + i
print('The sum of even numbers from 0 to 10 is:', sum)
