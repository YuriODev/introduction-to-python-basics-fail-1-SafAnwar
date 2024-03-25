# Exercise 1
# Your solution comes here

number = str(input("Enter a five-digit integer: "))
first_part = int(number[0]) + int(number[2]) + int(number[4])
first_part = first_part * 10
second_part = int(number[1]) + int(number[3])
print(first_part + second_part)