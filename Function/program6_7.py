# Write a simple program on keyword argument.

def greet(name, age):
    print("Hello", name + "!", "You are", age, "years old.")


    greet(age=25, name="Anna")  # Using keyword arguments to call the function