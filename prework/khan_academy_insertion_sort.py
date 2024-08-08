def insert(array, right_index, value): ## O(n) time complexity
    while array[right_index] > value and right_index >= 0:
        array[right_index+1] = array[right_index]
        array[right_index] = value
        right_index -= 1
    return array


def insertion_sort(array): ## O(n**2) time complexity
    for right_index in range(0, len(array) - 1):
        value = array[right_index + 1]
        array = insert(array=array, right_index=right_index, value=value)
    return array


array = [3, 5, 7, 11, 13, 2, 9, 6]
print(f'before: {array}')
array = insertion_sort(array)
print(f'after: {array}')

# array = insert(array=array, right_index=4, value=2)
# print(array)

# array = insert(array=array, right_index=5, value=9)
# print(array)

# array = insert(array=array, right_index=6, value=6)
# print(array)