# Return the index of the target element if found, otherwise return -1.


def linear_search(lst, target):

    for i in range(len(lst)):
        if lst[i] == target:
            return i

    return -1


numbers = [10, 20, 30, 40, 50]

position = linear_search(numbers, 40)

print(position)