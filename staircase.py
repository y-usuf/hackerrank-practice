#Write a program that prints a staircase of size n.

n = int(input())

if 0 < n <= 100: #Limit for value entry of n
    # Number of spaces
    k = (n) - 1
    # Outer loop to handle number of rows
    for i in range(n):
        # Inner loop to handle number of spaces
        for j in range(k):
            print(end=" ")

        # Decrementing k after each loop
        k = k - 1

        # Inner loop to handle number of column
        for j in range(i+1):
            # Print #
            print("#", end="")
        
        # Ending line after each row
        print("\r")

