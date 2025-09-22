"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.

get sales
while sales >= 0
    if sales < 1000
        bonus = sales * 0.10
    else:
        bonus = sales * 0.15
    display bonus
    get sales
display "Program ended"
"""

EDGE_CASE = 1000
LOW_BONUS_RATE = 0.10
HIGH_BONUS_RATE = 0.15

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < EDGE_CASE:
        bonus = sales * LOW_BONUS_RATE
    else:
        bonus = sales * HIGH_BONUS_RATE
    print(f"Bonus: ${bonus:.2f}")

    sales = float(input("Enter sales: $"))

print("Program ended.")
