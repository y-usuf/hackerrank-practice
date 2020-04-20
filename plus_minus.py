'''
Given an array of integers, calculate the fractions of its elements that are positive, negative, and are zeros. Print the decimal value of each fraction on a new line.
'''
n = int(input())
arr = list(map(int, input().split())) [:n]

#initializing count.
pos_sum = 0
neg_sum = 0
zero_sum = 0

#Using lambda to count the values of +ve, -ve and zeros in the array.
#The function filter(function, list) offers an elegant way to filter out all the elements of a list, for which the function function returns True.
pos_sum = len(list(filter(lambda x: (x > 0), arr)))
neg_sum = len(list(filter(lambda x: (x < 0), arr)))
zero_sum = len(list(filter(lambda x: (x == 0), arr)))

#Finding the decimal value of each fraction.
pos_ans = format(pos_sum/n, '.6f')
neg_ans = format(neg_sum/n, '.6f')
zero_ans = format(zero_sum/n, '.6f')

print(pos_ans)
print(neg_ans)
print(zero_ans)