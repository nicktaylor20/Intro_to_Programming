#DSC510
#Assignment 8.1
#Dominick Taylor
#2/5/2021
# program will process this .txt file: Gettysburg.txt Calculate the total words, and
# output the number of occurrences of each word in the file.

import string

def process_line(line, word_count_dict):
    line = line.strip()
    word_list = line.split()
    for word in word_list:
        if word != '--':
            word = word.lower()
            word = word.strip()
            word = word.strip(string.punctuation)
            add_word(word, word_count_dict)




def add_word (word, word_count_dict):
    if word in word_count_dict:
        word_count_dict[word] += 1
    else:
        word_count_dict[word] = 1






def pretty_print(word_count_dict):
    value_key_list = []
    for key, val in word_count_dict.items():
        value_key_list.append((val, key))
    value_key_list.sort(reverse=True)
    print('{:11s}{:11s}'.format("Word", "Count"))
    print(' '*21)
    for val, key in value_key_list:
        print('{:12s} {:<3d}'.format(key, val))







def main():
    word_count_dict = {}
    gba_file = open('gettysburg.txt', 'r')
    for line in gba_file:
        process_line(line, word_count_dict)
    print("The total length of the dictionary is: ", len(word_count_dict))
    print(' '*21)
    pretty_print(word_count_dict)

main()