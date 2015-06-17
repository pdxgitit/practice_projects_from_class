__author__ = 'Oliver'

# program to randomly pair classmates togther

import random

# function reorders classmates randomly

def randomize(students):
    length = len(students) - 1
    reorder = []
    for num in range(0, length):
        pick = random.randrange(0, length + 1)
        reorder.append(students.pop(pick))
        length = length - 1
    reorder.append(students[0])
    return reorder

# function prints out pairs

def print_groups(random_list):
    remainder = len(random_list) % 2
    if remainder > 0:
        last = random_list.pop()
    switch = 0
    out_string = ''
    for number in range(0, len(random_list)):
        if switch == 0 and len(random_list) > remainder:
            out_string = out_string + random_list[number] + " is paired with "
            switch = 1
        else:
            print out_string + random_list[number]
            switch = 0
            out_string = ''
    if last:
        print "and %s" % last

students = ["Ollie", "Paul", "Jay", "Jesse", "Dar", "Sophia", "Stephen", "Rachel", "Matt"]



random_list = randomize(students)
print_groups(random_list)