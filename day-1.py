students = [("A", 85), ("B", 40), ("C", 72), ("D", 30)]

a = []
for i in students:
    if i[1] >= 50:
        a.append(i[0])

print(a)

b = 0
for i in students:
    b += i[1]

print(b/len(students))

print(sorted(students)[-1])


password = input("Enter password: ")

if len(password) >= 8:
    upper = False
    lower = False
    digit = False
    special = False

    for ch in password:
        if ch.isupper():
            upper = True
        elif ch.islower():
            lower = True
        elif ch.isdigit():
            digit = True
        else:
            special = True

    if upper and lower and digit and special:
        print("Strong")
    else:
        print("Weak")
else:
    print("Weak")
