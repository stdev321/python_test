def count_numbers(sorted_list, less_than):
    index = binary_search(sorted_list, less_than)
    return index

def binary_search(sorted_list, target):
    low, high = 0, len(sorted_list) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1   
    return low

result = count_numbers([1, 3, 5, 7], 4)
print(result)
