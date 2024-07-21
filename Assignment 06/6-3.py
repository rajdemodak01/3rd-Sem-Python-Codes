# Create the first dictionary
dict1 = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 4}

# Create the second dictionary
dict2 = {'apple': 'red', 'cherry': 'red', 'date': 'brown', 'elderberry': 'black'}

# Take a key from the user
search_key = input("Enter a key to search: ")

# Search for the key in the second dictionary
if search_key in dict2:
    print(f"Corresponding value in dict2: {dict2[search_key]}")
else:
    print("Key not found in dict2.")

# # Merge the two dictionaries
# merged_dict = {**dict1, **dict2}

# # Display the merged dictionary
# print("\nMerged Dictionary:")
# print(merged_dict)
dict1.update(dict2)
print(dict1)
