def string_together(list):
    last = list.pop()
    if len(list) > 0:
        return ", ".join(list) + ' and ' + last
    else:
        return last

print string_together(["Ollie", "Dar", "Sophia", "Paul"])
print string_together(["Ollie", "Dar"])
print string_together(["Ollie"])