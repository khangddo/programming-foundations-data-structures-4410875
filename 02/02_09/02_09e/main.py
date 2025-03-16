def find_second_smallest(my_list):
    if (len(my_list) < 2):
        return None
    
    smallest = float('inf')
    second_smallest = float('inf')
    for val in my_list:      
        if (val < smallest):
            second_smallest = smallest
            smallest = val
        elif (val < second_smallest):
            second_smallest = val
    return second_smallest

print(find_second_smallest([1, 0, 2, 3, 4, 5, 6]))
