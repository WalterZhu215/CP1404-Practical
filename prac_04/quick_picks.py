import random

# Constants
MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_LINE = 6


def main():
    num_quick_picks = int(input("How many quick picks? "))
    for _ in range(num_quick_picks):
        quick_pick = []
        # Generate 6 unique numbers
        while len(quick_pick) < NUMBERS_PER_LINE:
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
            if number not in quick_pick:
                quick_pick.append(number)
        # Sort the numbers in ascending order
        quick_pick.sort()
        # Print with formatted alignment (2-digit width)
        print(" ".join(f"{num:2}" for num in quick_pick))


main()