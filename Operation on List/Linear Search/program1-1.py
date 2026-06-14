# Using a Function

def linear_search(lst, target):

    for item in lst:
        if item == target:
            return True

    return False


numbers = [10, 20, 30, 40, 50]

result = linear_search(numbers, 30)

print(result)