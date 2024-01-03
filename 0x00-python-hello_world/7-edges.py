#!/usr/bin/python3
word = "Holberton"
word_first_3 = word[:3] # character from the beginning to position 3 excluded
word_last_2 = word[-2:] # character from second last to the end
middle_word = word[1:-1] # characters in between the begining from position 1 to the first last
print("First 3 letters: {}".format(word_first_3))
print("Last 2 letters: {}".format(word_last_2))
print("Middle word: {}".format(middle_word))
