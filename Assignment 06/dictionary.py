def take_dictionary_input():
    repl_dict = {}
    num_entries = int(input("Enter the number of entries in the dictionary: "))
    
    for i in range(num_entries):
        key = input("Enter key {}: ".format(i + 1))
        value = input("Enter value for key {}: ".format(i + 1))
        repl_dict[key] = value
    
    return repl_dict

repl_dict = take_dictionary_input()
print("Dictionary:", repl_dict)
