"""
Given an array arr[], find the first repeating element.
The element should occur more than once and the index of its first occurrence should be the smallest.
"""

def first_repeated(arr):
    x = []
    for i in arr:
        rep_count = arr.count(i)
        if rep_count == 2:
            x.append(i)
            return f"{i} repeated {rep_count} times"
    if not x:
        return -1

def repeated_elements():
    pass

arr = [1, 5, 3, 4, 3, 5, 6]
print(first_repeated(arr))
arr = [1, 2, 3, 4, 5, 6]
print(first_repeated(arr))