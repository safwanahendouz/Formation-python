# Reverse function 1

# def reverse_fun(s):
#     return s[::-1]
# print(reverse_fun("brother"))

# sum_function 2
# def sum_func(a, b):
#     return sum(range(a, b+1))
# print(sum_func(1, 5))

# 3
# def sum_even(nums):
#     return sum(x for x in nums if x%2 == 0)
# print(sum_even([1, 2, 3, 4, 5, 6]))

# 4
# def count_vowels(s):
#     vowels = "aeiouAEIOU"
#     return sum(1 for x in s if x in vowels)
# print(count_vowels("hello world"))

# 5
# def max_min(s):
#     return (max(s), min(s))
# print(max_min([1, 2, 3, 4, 5]))

# 6
# print("welcom")

# Name = input("Enter your name: ")
# Grade =int(input("Enter your grade: "))

# if Grade < 60: 
#     print("Your Grade is F")
# elif Grade >= 60 and Grade < 69:
#     print("Your Grade is D")
# elif Grade >= 70 and Grade < 79:
#     print("Your Grade is C")
# elif Grade >= 80 and Grade < 89:
#     print("Your Grade is B")
# else:
#     print("Your Grade is A")

# method 2
# from symtable import Class


# Class Assignment:
#     def ___init__(self, name, score):
#         self.name = name
#         self.score = score

#     def self_grade(self):
#         if self.score < 60:
#             return "F"
#         elif self.score < 70:
#             return "D"
#         elif self.score < 80:
#             return "C"
#         elif self.score < 90:
#             return "B"
#         else:
#             return "A"
# self.name ="ALICE"
# self.score = 85
# assignment = Assignment(self.name, self.score)

# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient funds")
#         else:
#             self.balance -= amount

#     def get_balance(self):
#         return self.balance

# print("Welcome to the Bank")
# account = BankAccount("Mike", 100)
# account.deposit(100)
# account.withdraw(50)
# print(f"Your current balance is: {account.get_balance()}")

# method 2
# class BankAccount:
#     def __init__ (self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount

#     def withdraw(self, amount):
#         if self.balance <= amount:
#             print("insufficient funds !!!")
#         else:
#             self.balance -=amount
    
#     def get_balance(self):
#         return self.balance

# account = BankAccount("Mike", 100)
# account.withdraw(50)
# print(f"your current balance is : {account.get_balance()}")

# 8
# class Rectangle:
#     def __init__(self ,width ,height):
#         self.width = width
#         self.height = height

#     def get_area(self):
#         return self.width * self.height
    
#     def get_perimeter(self):
#         return 2 * (self.width + self.height)

# rec = Rectangle(5, 10)
# print(rec.get_area())
# print(rec.get_perimeter())

# 9th

# def Fibonacci(n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, b+a
# #     return a
# # print(Fibonacci(6))

# # 10th
# class Counter:
#     def __init__(self):
#         self.count = 0

#     def increment(self):
#         self.count+= 1

#     def reset(self):
#         self.count = 0
    
#     def get_count(self):
#         return self.count
    
# c = Counter()
# c.increment()
# c.increment()
# print(c.get_count())
# c.reset()
# print(c.get_count)

# def fe(n):
#     a, b = 0, 1
#     for i in range(n):
#         a, b = b, b+a
#         return a
# print(fe(2))


# Assigments week 6

# Assigment 1
# def hello():
#     print("hello python")
# hello()

# Assigment 2
# def greet(name):
#     print(f"Hello {name}")
# greet("Safwan")

# Assigment 3
# def sum(a, b):
#     return a + b
# print(sum(2, 2))

# Assigment 4
# def calculatrice(a, b, operation):
#     if operation == "add":
#         return a + b
#     elif operation == "subtract":
#         return a - b
#     elif operation == "multipl":
#         return a * b
#     elif operation == "division":
#         if b != 0:
#             return a / b
#         else :
#             print("Error !!!")
#     else :
#         print("sorry the operation not founded try again !!!")

# print(calculatrice(2, 2, "add"))
# print(calculatrice(2, 2, "subtract"))
# print(calculatrice(2, 2, "multipl"))
# print(calculatrice(2, 0, "division"))

# Assigment 5
# def introduction(name, age,  city):
#     return f"hello everyone my name is {name}, i'm {age} years old I came from {city}"
# print(introduction("Safwan", "18", "Agadir"))

# week 13 - 14
# Assigment 1
# class rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def get_area(self):
#         return self.width * self.height
#     def get_perimeter(self):
#         return (self.width + self.height) * 2

# rec = rectangle(5, 3)
# print(f"the area is {rec.get_area()}")
# print(f"the perimeter is {rec.get_perimeter()}")

# Assigment 2
class students:
    def __init__(self, name):
        self.name = name
        self.scores = []
    def add_score(self, score):
        self.scores.append(score)
    def get_average()


