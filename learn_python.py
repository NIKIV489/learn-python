
'''
month = input("enter the month to know the season ☀️❄️⛈️ :" )
date = int(input("enter the numbers between 1 to 31 :"))
if month =='january' or month =='december':
    if date>=1 and date<=31:
        print( f"the month is {month},the season is ** Winter **")
    else:
        print("enter the numbers between 1 to 31 ")
              
elif month == 'feburary':
    if date>=1 and date<=29:
        print( f"the month is {month},the season is ** Winter **")
    else:
        print("enter the numbers between 1 to 29 ")

elif month =='march' or month =='may':
    if date>=1 and date<=31:
        print( f"the month is {month},the season is ** spring **")
    else:
        print("enter the numbers between 1 to 31 ")
              
elif month == 'april':
    if date>=1 and date<=30:
        print( f"the month is {month},the season is ** spring **")
    else:
        print("enter the numbers between 1 to 30" )

elif month == 'june':
    if date>=1 and date<=30:
        print( f"the month is {month},the season is ** summer **")
    else:
        print("enter the numbers between 1 to 30 ")
              
elif month =='july' or month =='august':
    if date>=1 and date<=31:
        print( f"the month is {month},the season is ** summer**")
    else:
        print("enter the numbers between 1 to 31" )

elif month == 'september' or month =='november':
    if date>=1 and date<=30:
        print( f"the month is {month},the season is ** Autumn/Fall **")
    else:
        print("enter the numbers between 1 to 30 ")

elif month =='octomber':
    if date>=1 and date<=31:
        print( f"the month is {month},the season is ** Autumn/Fall **")
    else:
        print("enter the numbers between 1 to 31 ")
    
else:
    print("enter valid month or check your spelling")
'''
'''
m=5
for i in range(m):
    for j in range(m):
        print()

print(j)
'''
'''
for i in range(10,2):
'''




#palindrome or not (if we reverse a string it looks same the input given means palindrome )
'''
a=input("enter the word to check the palindrome or not :")
duplicate=""#no space must
for i in a:
    duplicate=i+duplicate
print(duplicate)
if a==duplicate:
    print(f"it is a palindrome for a word ,{a}")
else:
    print(f"it is a not palindrome for a word ,{a}")


'''
#enter the word to count the number of vowels in the strings
'''
a=str(input("enter the word to count the number of vowels in the strings :"))
vowels="aeiouAEIOU"
count=0
for i in a:
    if i in vowels:
        count+=1
print(f"the numbers of vowels count in word {count}")

'''

#reverse a string without using the build in function
'''
a=str(input("enter the word to reverse a string : "))
reverse=""
for i in a:
    reverse=i+reverse
print(f"the word {a} is reversed as {reverse}")

'''
#cont how many upper and lower case in the string
'''
a=str(input("enter the word to count the no of upper and lower case :"))
lcount=0
ucount=0
for i in a:
    if i.isupper():
        ucount=ucount+1
    else:
        if i.islower():
            lcount=lcount+1
print(lcount)
print(ucount)
print(f"In the given sentence the number of upper case is {ucount} and lower case {lcount}")

'''
#remove all the duplicate in the string
'''
a=str(input("remove all the duplicate in the string :"))
s=""
for i in a:
    if i not in s:
        s=s+i

print(f"the removed duplicate are {s}")

'''
#Find the most frequent character in a string
'''
a=str(input("enter the most frequent letter in word :"))
max_count=0
fre_count=''
for i in a:
    if a.count(i)>max_count:
        max_count=a.count(i)
        fre_count=i
print(f"the maximum character {fre_count}")
    
'''
#check if is a anagram or not
'''
a=str(input("enter the first input to check is a anagram or not :"))
b=str(input("enter the second input to check is a anagram or not :"))
c=a.lower()
d=b.upper()
if len(c) != len(d):
    print(f"The given texts '{a}' and '{b}' are NOT an anagram")
else:
    for i in c:
        if i in d:
            d = d.replace(i, "", 1)  # remove one occurrence
        else:
            print(f"The given texts '{a}' and '{b}' are NOT an anagram")
            break
    else:
        print(f"The given texts '{a}' and '{b}' are an anagram")

'''
#remove all the non alpha numeric
'''
a=str(input("enter the word :"))
c=""
for i in a:
    if i.isalpha():
        c=c+i
print(f"the only alpha numeric letters are {c}")

'''
#count the number of string letter in word
'''
a=str(input("clarify the count the number of word :"))
c=len(a.split())
print("the number of words ",c)
'''
#Find the sum of all digits in a string
'''
a=str(input("enter the word to count the number of letter on word :"))
c=0
for i in a:
    c=c+1
print(c)

'''
#Replace all spaces with hyphens
'''
a = input("Enter a string: ")
r = ""
for i in a:
    if i == " ":
        r += "-"
    else:
        r += i
print(r)
'''
# Replace all spaces with hyphens
'''
a = str(input("Enter the sentence to replace spaces with hyphens: "))
b = a.replace(" ", "-")
print(b)

'''
#captilize the first word
#/first iteration
#w[0].upper() → "W"
#w[1:] → "elcome"
#"W" + "elcome" → "Welcome"
#"Welcome" + " " → "Welcome "
#r += "Welcome " → r is now "Welcome "
#@//second iteration
#'''w[0].upper() → "T"
#w[1:] → "o"
#"T" + "o" → "To"
#"To" + " " → "To "
#r += "To " → r is now "Welcome To "
'''
a = input("Enter a sentence: ")
words = a.split()
r = ""
for w in words:
    r += w[0].upper() + w[1:] + " "
print(r.strip())

'''
#find digits
'''
a = input("Enter a string: ")
print("Digits in the string: ", end="")
for i in a:
    if i.isdigit():
        print(i, end="")
print()  # for newline

'''
'''
#
a = input("Enter a string: ")
result = ""

# Loop through indices starting from 1, step 2
for i in range(1, len(a), 2):
    result += a[i]

print("Every second character:", result)

a = input("Enter a string: ")
start = input("Start check: ")
end = input("End check: ")

print(a[:len(start)] == start)
print(a[-len(end):] == end)

'''
#python program to sum all the values in list
'''
a=[10,20,30,50]
b=0
for i in a:
    b=i+b
print(b)

c=[10,20,30,50]
d=sum(c)
print(d)

'''
#python program to find the largest value in list
a=[90,223,23,45]
for i,j in a:
    if i<j:
        i=i+1
        j=j+1
        if i<j:
            print(j)
        else:
            print(i)
    else:
        print(j)





































































    































































































































































