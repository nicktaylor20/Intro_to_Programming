#DSC510
#Assignment 9.1
#Dominick Taylor
#2/12/2021
# program will process this .txt file: Gettysburg.txt Calculate the total words, and
# output the number of occurrences of each word in the file to another file.

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






def process_file(word_count_dict, new_file_name):
    with open(new_file_name, 'w') as newfile:
        value_key_list = []
        for key, val in word_count_dict.items():
            value_key_list.append((val, key))
        value_key_list.sort(reverse=True)
        newfile.seek(65)
        newfile.write('{:11s}{:11s}'.format("Word", "Count"))
        newfile.write(' '*21)
        newfile.write('\n')
        for val, key in value_key_list:
            newfile.write('{:12s} {:<1d}\n'.format(key, val))








def main():
    word_count_dict = {}
    gba_file = open('gettysburg.txt', 'r')
    new_file_name = input("Please enter a name for the new file: ")
    with open(new_file_name, 'w') as newfile:
        for line in gba_file:
            process_line(line, word_count_dict)
            file_length = len(word_count_dict)
        newfile.write("The total length of the dictionary is: " + str(file_length))
        newfile.write(' '*21)
        newfile.write("\n")
        process_file(word_count_dict, new_file_name)



main()