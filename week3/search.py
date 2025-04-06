def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1
    
numbers = [10, 20, 30, 40, 50]
print(linear_search(numbers, 60))
print(linear_search(numbers, 30))