'''
You are in charge of the cake for your niece's birthday and have decided the cake will have one candle for each year of her total age. 
When she blows out the candles, she’ll only be able to blow out the tallest ones. Your task is to find out how many candles she can successfully blow out.
'''

ar_count = int(input())
ar = list(map(int, input().split())) [:ar_count]

max = ar[0] # Initialise maximum element
#max_value = max(ar)
count = 0 # Iniialise count to zero


#Traverse array element from second and compare every element with the maximum
for i in range(1, len(ar)):
    if ar[i] > max:
        max = ar[i]


    
#print(max_value)
print(count)
print(max)