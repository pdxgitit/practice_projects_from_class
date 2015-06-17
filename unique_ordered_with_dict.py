def remove_dups(list):
    seen = dict()
    new_list = []
    for item in list:
        if item not in seen:
            new_list.append(item)
            seen[item] = True
    return new_list

print remove_dups([5, 4, 4, 3, 3, 2, 2, 2, 1])
