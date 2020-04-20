
n = int(input())  #User inputs the size of the array
ar = list(map(int, input().split())) #[:n] An array created with n values
       
sum = 0 #Initialise the sum
if 1 <= n <= 10: #Limits the sum to only a maximum of 10 values
    for i in range(0, len(ar)):
        sum += ar[i]

    print(sum)