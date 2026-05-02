"""
Smart Attendance System
Problem:
You are given a list of student login times. Mark a student "Present" only if they log in before 9:05 AM.
"""
student = []

n = int(input("Enter the number of students: "))

for i in range(n):
    name = input("Enter the name: ")
    time = input("Enter login time (HH:MM): ")
    student.append([name, time])

for s in student:
    name = s[0]
    time = s[1]

    if time <= "09:05":
        print(name, "Present")
    else:
        print(name, "Absent")


"""E-commerce Discount Engine
Problem:
Apply discounts:
Above ₹5000 → 20%
₹2000–5000 → 10%
Below ₹2000 → No discount
Return final price."""

items = int(input("Enter the number of items purchased: "))
count = 0

for i in range(items):
    amount = int(input("Enter the amount purchased: "))

    if amount > 5000:
        amount = amount - amount * 0.20
        print("Discounted Amount:", amount)
        count += amount

    elif 2000 < amount <= 5000:
        amount = amount - amount * 0.10
        print("Discounted Amount:", amount)
        count += amount

    else:
        count += amount

print("Total Amount:", count)



"""Chat Message Analyzer
Problem:
Count:
Total messages
Number of questions
Number of emojis"""






messages = []

n = int(input("Enter number of messages: "))

for i in range(n):
    msg = input("Enter message: ")
    messages.append(msg)

total_messages = len(messages)
question_count = 0
emoji_count = 0

# simple emoji list (you can expand)
emojis = ["😀","😂","😍","😎","😊","😭","👍","🔥"]

for msg in messages:
    if "?" in msg:
        question_count += 1
    
    for ch in msg:
        if ch in emojis:
            emoji_count += 1

print("Total messages:", total_messages)
print("Number of questions:", question_count)
print("Number of emojis:", emoji_count)
