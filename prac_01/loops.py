"""
# a. Count in 10s from 0 to 100
for i in range(0, 101, 10)
    display (i, end=' ')

# b. Count down from 20 to 1
for i in range(20, 0, -1):
    display (i, end=' ')
print()

# c. Print n stars. Ask the user for a number
get number of stars
for i in range(number of stars):
    display ("*", end='')

# d. Print n lines of increasing stars
for i in range(1, number of stars + 1):
    display ("*" * i)
"""

# a. Count in 10s from 0 to 100
print("(a) Counting in 10s from 0 to 100:")
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b. Count down from 20 to 1
print("\n(b) Counting down from 20 to 1:")
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c. Print n stars. Ask the user for a number
print("\n(c) Printing n stars:")
number_of_stars = int(input("Number of stars: "))
for i in range(number_of_stars):
    print("*", end='')
print()

# d. Print n lines of increasing stars
print("\n(d) Printing n lines of increasing stars:")
for i in range(1, number_of_stars + 1):
    print("*" * i)
print()