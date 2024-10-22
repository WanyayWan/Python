item = input("What would you like to buy? : ")
price = float(input("What is the price? : "))
quantity = int(input("What is the quantity? :"))
total = int(price * quantity)

print(f"You have bought {item} * {quantity}")
print(f"Your total is ${total}")