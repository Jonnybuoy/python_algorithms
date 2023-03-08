'''
Reverse a string
'''

def reverse_string(s):
    length = len(s)
    spaces = [' ']
    words = []
    i = 0
    
    while i < length:
        if s[i] not in spaces:
            word_start = i
            
            while i < length and s[i] not in spaces:
                i += 1
            
            words.append(s[word_start:i])
            
            i += 1
    
    return "".join(reversed(s))

print(reverse_string("This is the best"))