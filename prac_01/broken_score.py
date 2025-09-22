"""
get score
if score < 0 or score > 100:
    display "Invalid score"
else if score >= 90:
    display "Excellent"
else if score >= 50:
    display "Passable"
else:
    display "Bad"
"""

MIN_SCORE = 0
MAX_SCORE = 100
E_SCORE = 90
P_SCORE = 50

score = float(input("Enter your score: "))
if score < MIN_SCORE or score > MAX_SCORE:
    print("Invalid score")
elif score >= E_SCORE:
    print("Excellent")
elif score >= P_SCORE:
    print("Passable")
else:
    print("Bad")