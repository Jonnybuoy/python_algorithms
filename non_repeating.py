"""
Non repeat element
Take a string and return character that never repeats
if multiple uniques then return only the firsst unique
"""

def non_repeating(s):
    s = s.replace(" ", "").lower()
    
    char_count = {}
    
    for c in s:
        if c in char_count:
            char_count[c] += 1
        
        else:
            char_count[c] = 1
    
    for c in s:
        if char_count[c] == 1:
            return c
    
    return None

print(non_repeating('I Apple Ape Peels'))