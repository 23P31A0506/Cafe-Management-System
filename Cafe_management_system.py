# Define the menu of restaurant
menu = {
    'Pizza' : 70,
    'Pasta' : 40,
    'Burger' : 60,
    'Salad' : 50,
    'Coffee' : 80,
}

# Greet
print("Welcome to Mystic Grill Restaurant")
print("Pizza: Rs70\nPasta: Rs40\nBurger: Rs60\nSalad: Rs50\nCoffee: Rs80")

order_total = 0
# 70 + 80 = 150

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1] # 0 + 50
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} is not avaliable yet!")

another_order = input("Do you want to order another item? (Yes/No): ")
if another_order == "Yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"Ordered item {item_2} is not avaliable!")
print(f"The total amount of items to pay is {order_total}")