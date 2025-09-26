"""
import random

function main
    score = get_score()
    result = determine_result(score)
    display "Result: {result}"

    random_score = random.randint(0, 100)
    random_result = determine_result(random_score)
    display "Random score ({random_score}): {random_result}"

function determine_result(score)
    if 90 <= score <= 100:
        return "Excellent"
    else if 50 < score < 90:
        return "Passable"
    else if 0 <= score <= 50:
        return "Bad"
    else:
        return "Invalid score"

function get_score()
    is_valid = False
    score = 0.0
    while not is_valid:
        try:
            get score
            is_valid = True
        except ValueError:
            display "Invalid input. Please enter a numeric value."
    return score
"""


import random

MIN_SCORE = 0
MAX_SCORE = 100
EXCELLENT_SCORE = 90
PASSABLE_SCORE = 50

def main():
    score = get_score()
    result = determine_result(score)
    print(f"Result: {result}")

    random_score = random.randint(0, 100)
    random_result = determine_result(random_score)
    print(f"Random score ({random_score}): {random_result}")

def determine_result(score):
    """Return the corresponding rating result based on the score"""
    if score < MIN_SCORE or score > MAX_SCORE:
        return "Invalid score"
    elif score >= EXCELLENT_SCORE:
        return "Excellent"
    elif score >= PASSABLE_SCORE:
        return "Passable"
    else:
        return "Bad"

def get_score():
    is_valid = False
    score = 0.0
    while not is_valid:
        try:
            score = float(input("Enter score: "))
            is_valid = True
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    return score

main()

