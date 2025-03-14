"""
    You have an unsorted array of elements, and you need a simple and efficient
    way to sort them in ascending order.
    Solution: Use the Insertion Sort algorithm, which is well-suited for small
    datasets.
    Here's a brief outline of how it works:
    l. Start with the assum ption that the fi rst element is already sorted,
    considering a single element as a sorted list.
    2. Iterate through the unsorted portion of the array. For each element,
    compare it with the elements in the sorted portion .
    3. Insert the element into its correct position within the sorted portion. Shift
    larger elements to the right to create space for the element.
    4. Repeat steps 2 and 3 for all elements in the unsorted portion.
    5. 0nce all elements are processed, the entire array is sorted.
    I nsertion Sort is a straightforward sorting_algorithm algorithm that works well for small
    datasets. Its time complexity is O (nA2) in the worst and average cases and O(n)
    in the best case, making it a practical choice for small lists or when the data is
    already partially sorted.
"""

num_list = [4, 1, 3, 6, 4, 3, 7, 8]

for x in range(1, len(num_list)):
    current_num = num_list[x]
    prev_index = x - 1
    while prev_index >= 0 and current_num < num_list[prev_index]:
        num_list[prev_index + 1] = num_list[prev_index]
        prev_index -= 1
    num_list[prev_index + 1] = current_num
print(num_list)
