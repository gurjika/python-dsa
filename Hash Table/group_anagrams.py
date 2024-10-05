def group_anagrams(strings):

    check_dict = {}
    group_list = []

    for string in strings:

        # ALSO WORKS
        # char_sum = 0
        # # for char in string:
        # #     char_sum += ord(char)

        sorted_string = ''.join(sorted(string))
        
        if sorted_string in check_dict:
            check_dict[sorted_string].append(string)
        else:
            check_dict[sorted_string] = [string]


        # if char_sum in check_dict:
        #     check_dict[char_sum].append(string)
        
        # else:
        #     check_dict[char_sum] = [string]




    for key, value in check_dict.items():
        group_list.append(value)

    return group_list


print("1st set:")
print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )

print("\n2nd set:")
print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )

print("\n3rd set:")
print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )

