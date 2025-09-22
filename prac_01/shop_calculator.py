"""
function main()
    get number_of_items
    while number_of_items < 0:
        display "Invalid number of items!"
        get number_of_items

    total_price = 0
    for i in range(number_of_items):
        get price
        while price < 0:
            print "Invalid price"
            get price
        total_price += price

    if total_price > 100:
        discount = total_price * 0.1
        total_price = total_price - discount

    display "Total price for {number_of_items} items is ${total_price:.2f}"
"""

LOWEST_TIME = 0
LOWEST_PRICE = 0
DISCOUNT_PRICE = 100
DISCOUNT_RATE = 0.1
def main():
    number_of_items = int(input("Number of items: "))
    while number_of_items < LOWEST_TIME:
        print("Invalid number of items!")
        number_of_items = int(input("Number of items: "))

    total_price = 0
    for i in range(number_of_items):
        price = float(input(f"Price of item {i + 1}: "))
        while price < LOWEST_PRICE:
            print("Invalid price")
            price = float(input(f"Price of item {i + 1}: "))
        total_price += price

    if total_price > DISCOUNT_PRICE:
        discount = total_price * DISCOUNT_RATE
        total_price = total_price - discount

    print(f"Total price for {number_of_items} items is ${total_price:.2f}")

main()