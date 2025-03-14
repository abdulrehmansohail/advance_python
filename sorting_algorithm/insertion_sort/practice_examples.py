# Example of sorting_algorithm a list using insertion sort
easy = [7, 3, 5, 2]
for x in range(1, len(easy)):
    current_num = easy[x]
    prev_index = x - 1

    while prev_index >= 0 and current_num < easy[prev_index]:
        easy[prev_index + 1] = easy[prev_index]
        prev_index -= 1
    easy[prev_index + 1] = current_num
print(easy)

# Example of sorting_algorithm a list using insertion sort
medium= [10, 4, 6, 3, 2, 8]
def insertion_sort(lst):
    for index in range(1, len(lst)):
        _num = lst[index]
        _index = index - 1
        while _index >= 0 and current_num < lst[_index]:
            lst[_index + 1] = lst[_index]
            _index -= 1
        lst[_index+1] = current_num
insertion_sort(medium)
print(medium)

# Example of sorting_algorithm a list in REVERSE ORDER using insertion sort
# 💡 Bonus Challenge: Can you modify the code to sort in descending order?
hard = [12, 11, 13, 5, 6, 7, 3]
for h in range(1,len(hard)):
    c_num = hard[h]
    p_index = h - 1
    # key changes changed the position of c_num and hard[p_index] against < operator
    while p_index >= 0 and hard[p_index] < c_num:
        hard[p_index + 1] = hard[p_index]
        p_index -= 1
    hard[p_index + 1] = c_num
print(hard)