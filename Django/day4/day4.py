menu = {
    'pasta': 40,
    'pizza': 50,
    'burger': 60,
    'salad': 70,
    'coffee': 40,
}

print("Welcome to our restaurant!")
print('pasta : RS 40\n pizza : RS 50\n burger : RS 60\n salad : RS 70\n coffee : RS 40')


# gpay credit card debit card cash
# how to add new item to the menu
# extra charges for extra cheese or toppings
# extra chareges on COD
# more than 5 items give any buy one get one free offer
# better waiting system for the customers
 

order_total = 0
items = input("Please enter the items you want to order (comma-separated): ").split(',')
if items in menu:
    order_total += menu[items]
    print(f"Your order total is: RS {order_total}")

