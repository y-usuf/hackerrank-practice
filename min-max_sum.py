'''
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. 
Then print the respective minimum and maximum values as a single line of two space-separated long integers.
'''

arr = list(map(int, input().split())) [:5] #Allows user to input 5 integers
arr.sort()                                 #Sorts the values in ascending order

arr_max = arr[1:]                          #Removes the list value.
arr_min = arr[:4]
arr_max = sum(arr_max)
arr_min = sum(arr_min)

print(arr_min, arr_max)

