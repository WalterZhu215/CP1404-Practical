# Part 1: Collect 5 numbers and display information
numbers = []
for _ in range(5):
    number = float(input("Number: "))
    numbers.append(number)

print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {sum(numbers) / len(numbers)}")


# Part 2: Woefully inadequate security checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
             'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
             'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

user_input = input("Enter your username: ")
if user_input in usernames:
    print("Access granted")
else:
    print("Access denied")


# Part 3: List comprehensions (示例：生成1-10的平方列表)
# 这里以生成1到10的平方列表为例展示列表推导式的用法
squares = [i **2 for i in range(1, 11)]
print("Squares of 1-10 (list comprehension example):", squares)