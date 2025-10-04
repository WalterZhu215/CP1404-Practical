# 1. Write user's name to name.txt using open and close
name = input("Enter your name: ")
file = open("name.txt", "w")
file.write(name)
file.close()


# 2. Read name from name.txt and print greeting using open and close
file = open("name.txt", "r")
name = file.read().strip()  # strip() removes any extra whitespace/newlines
file.close()
print(f"Hi {name}!")


# 3. Read first two numbers from numbers.txt, sum them (using with)
with open("numbers.txt", "r") as file:
    # Read first two lines, convert to integers, and sum
    num1 = int(file.readline())
    num2 = int(file.readline())
    total = num1 + num2
print(total)  # Should output 59


# 4. Read total of all numbers in numbers.txt (works for any number of lines)
total = 0
with open("numbers.txt", "r") as file:
    # Iterate over each line in the file
    for line in file:
        total += int(line.strip())  # strip() handles any extra whitespace
print(total)  # For the given numbers.txt, outputs 459 (17 + 42 + 400)