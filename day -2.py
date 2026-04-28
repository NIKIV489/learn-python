"""
E-commerce Cart System
Problem:
Cart items:Python ,cart = {"apple": 2, "banana": 3, "milk": 1} ,prices = {"apple": 50, "banana": 20, "milk": 60}

Write a program to:
Calculate total bill Apply 10% discount if total > 100 ,Print final amount
"""


cart = {"apple": 2, "banana": 3, "milk": 1}
prices = {"apple": 50, "banana": 20, "milk": 60}

total = 0

for item in cart:
    total = total + cart[item] * prices[item]

print("Total Bill =", total)

if total > 100:
    discount = total * 10 / 100
else:
    discount = 0

final = total - discount

print("Discount =", discount)
print("Final Amount =", final)


"""
 5. Rotate Array to Sorted Form
Problem:
Given a rotated sorted array:
Python
arr = [4, 5, 6, 1, 2, 3]
"""



arr = [4, 5, 6, 1, 2, 3]

while arr[0] > arr[-1]:
    first = arr.pop(0)
    arr.append(first)

print(arr)         
