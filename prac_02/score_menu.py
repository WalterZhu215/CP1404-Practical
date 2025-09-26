MIN_SCORE = 0
MAX_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASSABLE_THRESHOLD = 50


def main():
    score = get_valid_score()

    menu = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit
>>> """

    # 使用标志变量控制循环
    continue_program = True
    while continue_program:
        choice = input(menu).upper()

        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            result = determine_result(score)
            print(f"Result: {result}")
        elif choice == 'S':
            print_stars(score)
        elif choice == 'Q':
            print("Farewell! See you again")
            continue_program = False  # 退出循环
        else:
            print("Invalid choice")


def print_stars(score):
    """Print the same number of asterisks as the number of scores"""
    stars = '*' * int(round(score))
    print(stars)


def get_valid_score():
    """Get and return a valid score between 0 and 100"""
    is_valid = False
    score = 0.0
    while not is_valid:
        try:
            score = float(input(f"Enter a score between {MIN_SCORE} and {MAX_SCORE}: "))
            if MIN_SCORE <= score <= MAX_SCORE:
                is_valid = True
            else:
                print(f"Score must be between {MIN_SCORE} and {MAX_SCORE}")
        except ValueError:
            print("Invalid input. Please enter a number.")
    return score


def determine_result(score):
    """Return the corresponding rating result based on the score"""
    if score >= EXCELLENT_THRESHOLD:
        return "Excellent"
    elif score >= PASSABLE_THRESHOLD:
        return "Passable"
    else:
        return "Bad"


main()

