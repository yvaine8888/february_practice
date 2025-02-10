'''
Problem - Creating an acronym by taking the first letter of each word.

U - Ignore short words like of, or, and, and remove punctuation.

C - This is done by replacing each punctuation and while for looping
    ignore short words (<=3)

A - I'll split the string by using the split method
    Use a for loop to get the first letter (index 0) of ones greater than 3 and 
       add to a string.
    Upper case by useing the upper method.
    if it is 0 or 1 letter, tell it so.

S is below and E is in main.py.

Note* I expect it to return a message if given it. I don't think an acronym should be 
a single letter if given that so I'll return something if so.
'''

def acronym_generator(s):
    #Punctuation to replace
    replacing = "''!()-[]{};:\"\,<>./?@#$%^&*_~''"

    # Replacing it
    for ele in replacing:
        s = s.replace(ele, "")

    #Separating the words into a list
    words = s.split()

    #Getting the first letter of each word
    result = ""
    for word in words:
        if(len(word) > 3):
            result = result + word[0]
    
    #Turning it uppercase
    result = result.upper()

    if len(result) < 2:
        result = "This is too short."

    return result