def two_sum(nums, target):
    check_dict = {}

    # BETTER
    for index, num in enumerate(nums):
        complement = target - num 
        if complement in check_dict: 
            return [check_dict[complement], index]  
        
        check_dict[num] = index 

    # MINE
    # for index, num in enumerate(nums):
    #     check_dict[num] = index

    # for index, num in enumerate(nums):

    #     saved_index = check_dict.get(target - num)
    #     if saved_index is not None and index != saved_index:
    #         return [index, check_dict[target - num]]
            
    return []

    




print(two_sum([5, 1, 7, 2, 9, 3], 10))  
print(two_sum([4, 2, 11, 7, 6, 3], 9))  
print(two_sum([10, 15, 5, 2, 8, 1, 7], 12))  
print(two_sum([1, 3, 5, 7, 9], 10))  
print ( two_sum([1, 2, 3, 4, 5], 10) )
print ( two_sum([1, 2, 3, 4, 5], 7) )
print ( two_sum([1, 2, 3, 4, 5], 3) )
print ( two_sum([5, 1, 5], 10) )
