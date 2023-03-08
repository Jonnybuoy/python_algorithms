def anagram(str1, str2):
    str1 = str1.replace(' ', '').lower()
    str2 = str2.replace(' ', '').lower()
    
    if len(str1) != len(str2): # if the strings are not of the same length then exit early
        return False
    
    count = {} # keep a count of every letter
    
    for letter in str1:  # loop through every letter in string
        if letter in count:  # if letter is in the dictionary and has a count
            count[letter] += 1  # increment the letter's count by 1
        else:
            count[letter] = 1   # give the letter a count of 1
    
    for letter in str2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1
    
    for k in count:
        if count[k] != 0:
            return False
    
    return True


print(anagram('public relations', 'crap built on lies'))