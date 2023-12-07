def unique_names(names1, names2):
    unique_names_set = set(names1 + names2)
    unique_names_list = list(unique_names_set)
    return unique_names_list

result = unique_names(['Ava', 'Emma', 'Olivia'], ['Olivia', 'Sophia', 'Emma'])
print(result)
