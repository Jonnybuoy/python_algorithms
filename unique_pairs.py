'''

Array pair sum.

Given an integer array, output all the unique pairs that sum up to a specific value k.
So the input:
pair_sum([1,3,2,2], 4)
would return 2 pairs:
(1,3)
(2,2)

'''

def pair_sum(arr, k):
    if len(arr) < 2:  # if the size of the array is less than 2, there is no point in continuing
        return False
    
    seen = set()  # after an iteration we record a number here as seen
    output = set() # output of a pair

    for num in arr:  # iterate through every number in the array
        target = k - num  # create a target number by subtracting k from number
        if target not in seen: 
            seen.add(num)  # add the number to seen numbers
        else:  # if target number is in seen numbers then
            output.add((min(num, target), max(num, target)))  # add num and target to output
    
    print('\n'.join(map(str, list(output))))
    
pair_sum([1,3,2,2], 4)
        
            