# Week 5
# Code Along 1
def string_to_dictionary(strng):
    strng = strng.lower()
    new_dict = dict()
    words = strng.split()

    for letter in words:
        if letter in new_dict:
            new_dict[letter] += 1
        else:
            new_dict[letter] = 1
    return new_dict

my_var = "The quick brown fox jumped over the lazy dog"
print(string_to_dictionary(my_var))
