
name = "Adam"
age = 36
is_student = False

print(name, age, is_student)


x = 10
y = 3.14
z = 'The answer is ' + str(x / y)
print(z)


score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"
print("Your grade is:", grade)

for fruit in ["apple", "banana", "cherry"]:
    print(fruit)

count = 0
while count < 5:
    print(count)
    count += 1

fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2:5])  # prints [2, 3, 4]

person = {"name": "Bob", "age": 25, "city": "New York"}
print(person["name"])

def greet(name):
    return f"Hello, {name}!"

print(greet("Charlie"))

class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

calc = Calculator()
print(calc.add(5, 3))  # prints 8
print(calc.subtract(5, 3))  # prints 2


import math

radius = 5
area = math.pi * (radius ** 2)
print("The area is:", area)
