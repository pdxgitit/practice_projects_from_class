def remove_dups(list):
    single_list = set()
    for item in list:
        single_list.add(item)
    return single_list

print remove_dups([50.10, "one", 2, "alabama", 1, 1, 2, 2, "Hello", 3, 3, 4])
