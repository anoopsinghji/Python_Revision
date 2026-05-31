
# Write a program which prompts a user to enter the radius of a circle. If the radius is greater than 
# zero then calculate and print the area and circumference of the circle.

print('Enteer the requisite radius of a circle:')

R = eval(input())

if R>0:
    area = 3.14*R**2
    circumference = 2*3.14*R
    print('Area of the circle is :',area)
    print('Circumference of the circle is :',circumference)