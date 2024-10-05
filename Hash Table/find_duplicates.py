def find_duplicates(list):
    duplicates_list = []
    check_dict = {}

    
    
    # for i in list:
    #     if check_dict.get(i) is not None and check_dict.get(i) is False:
    #         check_dict[i] = True

    #     elif check_dict.get(i) is None:
    #         check_dict[i] = False
       

    for i in list:
        if i in check_dict:
            check_dict[i] += 1

        else:
            check_dict[i] = 1


    for key, val in check_dict.items():
        if val > 1:
            duplicates_list.append(key)

    return duplicates_list


print ( find_duplicates([1, 2, 3, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 3]) )
print ( find_duplicates([1, 1, 1, 1, 1]) )
print ( find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([]) )