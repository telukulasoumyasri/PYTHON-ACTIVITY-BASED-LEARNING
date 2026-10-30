n = int(input("Enter number of products: "))
total = 0

for i in range(n):
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))

    total += price * quantity

if total >= 1000:
    total = total - (total * 0.10)

print("Total Bill:", total)