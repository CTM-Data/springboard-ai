
# assignment: given an array a and a starting index I, find the meta index of the min value within the subarray a[i:]

#try with a counter
def indexOfMinimum(array, startIndex):
    currentMin = array[startIndex]
    currentMinIndex = startIndex
    counter = 0
    for num in array[startIndex + 1:]:
        counter += 1
        if num < currentMin:
            currentMin = num
            currentMinIndex = currentMinIndex + counter
            counter = 0
        
    return currentMinIndex

    
array = [18, 6, 66, 44, 9, 22, 14]
result = indexOfMinimum(array, 5)
print(result)