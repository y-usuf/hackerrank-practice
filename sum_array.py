# n = int(input())
# arr = []
# for i in range(n):
#     arr.append(int(input()))

#array=list(map(int,input().split()))

ar_count = int(input())
#ar = list(map(int, input().rstrip().split()))
ar = list(map(int, input().split())) [:ar_count]

sum = 0
for i in range(0, len(ar)):
    sum += ar[i]

print(sum)