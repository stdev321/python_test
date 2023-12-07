def find_two_sum(nums, target_sum):
    complement_dict = {}

    for i, num in enumerate(nums):
        complement = target_sum - num
        if complement in complement_dict:
            return complement_dict[complement], i
        complement_dict[num] = i
    return None

result = find_two_sum([3, 1, 5, 7, 5, 9], 10)
print(result)