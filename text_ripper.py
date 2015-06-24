__author__ = 'Oliver'

import fnmatch
import os
import operator

# program to rip through text and return all words ranked by how often they occur

def which_file():
    for file in os.listdir('.'):
        if fnmatch.fnmatch(file, '*.txt'):
            print file
    last = raw_input("Which text file would you like to read in? ")
    return "/Users/Oliver/PyCharm/practice_projects_from_class/" + last


def word_count_dict(filename):
    word_count = {}
    input_file = open(filename, 'r')
    for line in input_file:
        words = line.split()
        for word in words:
            word = word.lower()
            if not word in word_count:
                word_count[word] = 1
            else:
                word_count[word] = word_count[word] + 1
    input_file.close()
    return word_count

def print_words(obj):
    sorted_dict = sorted(obj.items(), key=operator.itemgetter(1))
    for pair in sorted_dict:
        print pair[0], pair[1]


send = which_file()
print send
output = word_count_dict(send)
print_words(output)