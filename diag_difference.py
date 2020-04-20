
n = int(input()) # Allows user to input the size of matrix i.e 3*3
arr = [] # Create an empty array to store user input

for i in range(n):
    arr.append(list(map(int, input().split())))

length = len(arr)
prim_diag = 0
sec_diag = 0

for j in range(length):
    prim_diag += arr[j][j] # Sums up values in the primary diagonal
    sec_diag += arr[j][length - j - 1] # Sums up values in the secondary diagonal

#print(prim_diag)
#print(sec_diag)
ans = abs(prim_diag - sec_diag) # Finds the diagonal absolute difference
print(ans)

