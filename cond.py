# 'price' has already been created
price = float(input())
# Write your code here
if price >= 300:
    price *= 0.7
elif 200 <= price < 300:
    price *= 0.8
elif 100 <= price < 200:
    price *= 0.9
elif 0 <= price < 100:
    price *= 0.95
else:
    price

print (price)   