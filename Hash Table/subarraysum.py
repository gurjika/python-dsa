def subarray_sum(nums, target):

    check_dict = {}


    check_target = 0 
    for index, num in enumerate(nums):
        check_target += num

        if target == check_target:
            return [0, index]
        
        complement = check_target - target

        if check_dict.get(complement) is not None:
            check_index = check_dict[complement]

            return [check_index + 1, index]
            
            
        check_dict[check_target] = index


    return []




nums = [1, 2, 3, 4, 5]
target = 9
print ( subarray_sum(nums, target) )

nums = [-1, -2, -3, -4, 5]
target = -7
print ( subarray_sum(nums, target) )

nums = [2, 3, 4, 5, 6]
target = 3
print ( subarray_sum(nums, target) )

nums = []
target = 0
print ( subarray_sum(nums, target) )