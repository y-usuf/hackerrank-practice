# Allows user to input values in an array
a = list(map(int, input().split()))
b = list(map(int, input().split()))

#Initialises our sum count to zero
sum_a = 0
sum_b = 0

'''
For each value in a to all values in b and incrementing them.
'''
# for i in range(0, len(a)):
#     for j in range(0, len(b)):
#         if a[i] > b[j]:
#             sum_a += 1
#         elif a[i] < b[j]:
#             sum_b += 1

'''
compares the values of the same index in both arrays, sums the score and outputs it.
'''
if len(a) == len(b):
    for i in range(len(a)):
        if a[i] > b[i]:
            sum_a += 1
        elif a[i] < b[i]:
            sum_b += 1

print(sum_a, sum_b)


