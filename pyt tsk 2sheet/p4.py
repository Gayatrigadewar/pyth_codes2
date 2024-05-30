def is_proper_substring(string_list):
  
    if len(string_list) < 2:
        return False
    

    nth_minus_1_string = string_list[-2]
    nth_string = string_list[-1]
    

    return nth_minus_1_string in nth_string


input1 = ['a', 'abb', 'sfs', 'oo', 'de', 'sfde']
input2 = ['a', 'abb', 'sfs', 'oo', 'ee', 'sfde']

print(is_proper_substring(input1)) 
print(is_proper_substring(input2))  
