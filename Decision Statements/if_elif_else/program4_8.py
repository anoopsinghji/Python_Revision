# Write a program to prompt a user to read the marks of five different subjects.
# Calculate the total marks and percentage of the marks and display the message
# according to the range of percentage given in table.

# Percentage                             Message
# per >= 90                              Distinction
# per >= 80 and per < 90                 First Class
# per >= 70 and per < 80                 Second Class
# per >= 60 and per < 70                 Pass
# per < 60                               Fail

subject1 = float(input("Enter the Marks of Data-Structure: "))
subject2 = float(input("Enter the Marks of Python: "))
subject3 = float(input("Enter the Marks of Java: "))
subject4 = float(input("Enter the Marks of C Programming: "))
subject5 = float(input("Enter the Marks of HTML: "))

total = subject1 + subject2 + subject3 + subject4 + subject5
per = total / 5

print("Total Marks Obtained", total, "Out of 500")
print("Percentage =", per)

if per >= 90:
	print("Distinction")
elif per >= 80:
	print("First Class")
elif per >= 70:
	print("Second Class")
elif per >= 60:
	print("Pass")
else:
	print("Fail")