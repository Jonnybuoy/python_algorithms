'''
Take an array with positive and negative integers and find the maximum sum of that array
[10, 12, 15, 20, 30, -15, 5, -20, 30]
'''

def largest_sum(arr):
    if len(arr) == 0:
        return False
    
    max_sum = current_sum = arr[0]
    
    for num in arr[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)
        
    return max_sum

print(largest_sum([10, 12, 15, 20, 30, -15, 5, -20, 30]))
        
        
    