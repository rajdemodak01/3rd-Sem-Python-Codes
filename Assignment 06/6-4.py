# def replace_words(input_str, repl_dict):
#     words = input_str.split()
#     replaced_words = [repl_dict.get(word, word) for word in words]
#     return ' '.join(replaced_words)

# test_str = 'TechnoIndia is one of the best colleges in India'
# repl_dict = {"India": "West Bengal"}

# output_str = replace_words(test_str, repl_dict)
# print(output_str)

def replace_words(input_str, repl_dict):
    words = input_str.split()
    replaced_words = []
    
    for word in words:
        if word in repl_dict:
            replaced_words.append(repl_dict[word])
        else:
            replaced_words.append(word)
    
    output_str = ' '.join(replaced_words)
    return output_str

test_str = 'TechnoIndia is one of the best colleges in India'
repl_dict = {"India": "West Bengal"}

output_str = replace_words(test_str, repl_dict)
print(output_str)
