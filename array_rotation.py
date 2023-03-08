'''
Given 2 arrays (assume no duplicaates)
is 1 array a rotation of another - return True/False
same size and elements but start index is different
'''

# Rethink this solution

def rotation(list1, list2):
    if len(list1) != len(list2):
        return False
    
    key = list1[0]  # first element of list1
    key_index = 0  # index pointer on list2
    
    for i in range(len(list2)):
        if list2[i] == key:
            key_index = i
            break
    
    if key_index == 0:
        return False
    
    for x in range(len(list1)):
        l2index = (key_index + x) % len(list1)
        
        if list1[x] != list2[l2index]:
            return False
    
    return True

print(rotation([1,2,3,4,5,6,7], [4,5,6,7,1,2,3]))