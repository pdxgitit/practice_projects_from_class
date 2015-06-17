def string_together(list):
    """
    Formats array as written sentence without pretentious Oxford comma.
    accepts array of strings and returns single string of comma separated values with and between last items
    """
    one_word = ""
    for word in list:
        if word == list[-1] and len(list) > 1:
            one_word = one_word + " and " + word
        elif word == list[0]:
            one_word = word
        else:
            one_word = one_word + ", " + word
    return one_word

print string_together(["Ollie", "Dar", "Sarah", "Paul"])
print string_together(["Ollie", "Dar"])
print string_together(["Ollie"])