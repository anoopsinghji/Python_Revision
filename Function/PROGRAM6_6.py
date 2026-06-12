# Write a program to find the maximum of two numbers. 

print("Enter two numbers:")

num1 = float(input())
num2 = float(input())

def maxNum(a,b):
    if a>b:
        print(a, "is greater than", b)
    elif b>a:
        print(b, "is greater than", a)
    else:        
        print("Both numbers are equal.")

maxNum(num1, num2)