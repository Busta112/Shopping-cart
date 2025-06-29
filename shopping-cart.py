# Create a shopping cart programme that will continously ask the user for product and the price of the product
# Have an exit clause if the user wishes to stop adding more products to theor cart
# At the end show the product items and the total cost to the user


foods = []
prices = []
total = 0 # The reason why we're giving total a value of zero its because we don't want multiple values, we only need one total


while True:
    food = input("Enter food you want to buy or press x to exit: ")
    if food == 'x':
        break
    else:
        price = float(input(f"Enter the price of {food}: R"))
        foods.append(food)
        prices.append(price)

print("---------------------- YOUR CART ----------------------")

for food in foods:
    print(food, end = " ")
    
for price in prices:
    total += price

print("\n")
print(f"Over Price is: R{total}")
