'''
Problem - Given a sentence, find the first longest word and return it.

Get rid of non-alphabetic characters (punctuation, etc.) using replace.
Split.
Using a for loop, iterate and if the length is greater than the one before, 
change the result variable.
Testing is in main.py
'''

def longest_word(s):
    #Things to replace
    replacing = "''!()-[]{};:\"\,<>./?@#$%^&*_~''"

    # Replacing it
    for ele in replacing:
        s = s.replace(ele, "")
    
    #Split into seperate words
    words = s.split()

    result = ""

    #Getting the longest word
    for word in words:
        if len(word) > len(result):
            result = word

    return result