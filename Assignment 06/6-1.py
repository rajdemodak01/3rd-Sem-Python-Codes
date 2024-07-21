# # Creating a dictionary
# my_dict = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 4}

# # Sorting dictionary by key
# sorted_by_key = dict(sorted(my_dict.items()))

# print("Sorted by key:")
# print(sorted_by_key)

# # Sorting dictionary by value
# sorted_by_value = dict(sorted(my_dict.items(), key=lambda item: item[1]))

# print("Sorted by value:")
# print(sorted_by_value)

# dict1={'apple':3,'cherry':1,'banana':0,'date':5}
# dict2=sorted(dict1.keys())
# print(dict2)

def take_dictionary_input():
    repl_dict = {}
    num_entries = int(input("Enter the number of entries in the dictionary: "))
    
    for i in range(num_entries):
        key = input("Enter key {}: ".format(i + 1))
        value = input("Enter value for key {}: ".format(i + 1))
        repl_dict[key] = value
    
    return repl_dict

repl_dict1 = take_dictionary_input()
print("Dictionary:", repl_dict1)
sorted_by_key=dict(sorted(repl_dict1.items()))
sorted_by_value=dict(sorted(repl_dict1.items(),key=lambda items:items[1]))
print(sorted_by_key)
print(sorted_by_value)
