#  Write a program to prompt a user to enter a day of the week. If the entered day of the week is 
# between 1 and 7 then display the respective name of the day


print('Enter a day of the week (1-7):')
day = int(input())

if day == 1:
    print('Monday')
elif day == 2:
    print('Tuesday')
elif day == 3:
    print('Wednesday')
elif day == 4:
    print('Thursday')
elif day == 5:
    print('Friday')
elif day == 6:
    print('Saturday')
elif day == 7:
    print('Sunday')
else:
    print('Invalid input. Please enter a number between 1 and 7.')
    