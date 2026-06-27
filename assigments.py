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
class BankAccount:
    def __init__ (self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance <= amount:
            print("insufficient funds !!!")
        else:
            self.balance -=amount
    
    def get_balance(self):
        return self.balance

account = BankAccount("Mike", 100)
account.withdraw(50)
print(f"your current balance is : {account.get_balance()}")




