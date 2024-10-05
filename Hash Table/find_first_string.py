def first_non_repeating_char(string):

    check_dict = {}
    for char in string:
        if char in check_dict:
            check_dict[char] += 1
        else:
            check_dict[char] = 1


    for key, value in check_dict.items():
        if value == 1:
            return key
            


print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )