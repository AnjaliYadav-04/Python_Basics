''' ch = input("Enter a character: ")


if ch.lower() in ['a', 'e', 'i', 'o', 'u']:

    print("Vowel")

else:

    print("Not a Vowel")
'''


'''
ch = input("Enter a character: ")


if ch.lower() not in ['a', 'e', 'i', 'o', 'u']:

    print("consonants")

else:

    print("Not a consonants l")



num = int(input("Enter a number: "))


if num > 0:

    print("Positive")

else:

    print("Not Positive")





num = input("Enter value: ")


try:

    val = float(num)

    print("It is a number (float supported)")

except:

    print("Not a number")


num = float(input("Enter a number: "))


if isinstance(num, float):

    print("Float")





num = int(input("Enter a number: "))


if 100 <= num <= 999 or -999 <= num <= -100:

    print("3-digit number")

else:

    print("Not a 3-digit number")



s = input("Enter a string: ")


s = s.lower().replace(" ", "")


if s == s[::-1]:

    print("Palindrome")

else:

    print("Not Palindrome")






my_list = [10, 20, 30, 40, 50]  # Example list


if len(my_list) == 0:

    print("The list is empty, no middle value.")

else:

    mid_index = len(my_list) // 2

    if len(my_list) % 2 == 1:

        print(f"Middle value is: {my_list[mid_index]}")

    else:

        print(f"List has even length, middle values are: {my_list[mid_index-1]} and {my_list[mid_index]}")

'''


# Q) WAP to check whether last digit is 5 or not
'''num = int(input("Enter a number : "))
if num % 10 == 5:
    print("Yes, last digit is 5")
else:
    print("No, last digit is Not 5")'''


#Q) Print ASCII Value of a character only if it is Upper Case.
'''Name = input("Enter a character : ")
if 'A'<=Name<='Z':
    print("ASCII value is ",ord(Name))
else:
    print("Not an upper case char.")'''


# Q) WAP to print the cube of a number only if it is divisible by 9 or 6
'''num = int(input("Enter a number : "))
if num%9==0 or num%6==0:
    print(num**3)
else:
    print("Neighter divisible by 6 or 9")'''


# check char is upper case, lower case, digit and special char
'''c = input("Enter a character : ")
if 'A'<=c<='Z':
    print("upper case")
elif 'a'<=c<='z':
    print("lower case")
elif '0'<=c<="9":
    print("digit")
else:
    print("Special char")'''

# check whether the given number is single digit, two digit, 3 digit or more than 3.
# num = int(input("Enter a number : "))
'''var1 = abs(num)
if 0<=var1<=9:
    print("single digit")
elif 10<=var1<=99:
    print("two digit")
elif 100<=var1<=999:
    print("3 digit")
else:
    print("more than 3 digit")'''


# WAP to print the middle value of a list, only if it string.
'''lst = [23,'Hello',2.3]
if type(lst[len(lst)//2])==str:
    print("Yes, middle value is string")
else:
    print("No, middle value is not string")'''


# Sample list
# my_list = eval(input("Enter values for list : "))
'''if len(my_list)%2!=0:
    m=len(my_list)//2
    if type(my_list[m])==str:
        print("yes, middle value is string")
    else:
        print("middle value is not string")
print("Size of list is even")   '''


# WAP to print the Reverse string only if it is starting with vowel, ending with consonant and having a middle value.
'''name = input("Enter a string : ")
if len(name)%2!=0:
    if name[0] in 'AEIOUaeiou'and name[-1] not in 'AEIOUaeiou':
        print(name[::-1])
    else:
        print("Not start with vowel or end with consonant")
else:
    print("Given string characters are even")'''


# WAP to print the last value of a list, only if it is palindrome string (Starting with vowel)
# name = eval(input("Enter values for list : "))
'''lst = ["abc","monkey","tom","AnnnA"]
last = lst[-1]
if last==last[::-1]:
    if last[0] in 'AEIOUaeiou':
        print("Last value of list which is palindrome is : ",last)
    else:
        print("Palindrome's first character is not vowel")
else:
    print("last value is not palindrome.")'''


# Date: 22/4/26
# Q) Reverse every character but don't change words position
# 1st Way
'''def reverse_char(s):
    # out='syawlA peeK gnillims'
    words = s.split()
    res=''
    for i in words:
        rev=''
        for j in i:
            rev=j+rev  # A+''=A => l+A=lA => w+lA => wlA
        res+=rev+' '
    return res

print(reverse_char('Always keep smilling'))'''


#2nd Way
'''s='Always keep smilling'
l=s.split()
out=[]
for i in l:
    out.append(i[::-1])
print(" ".join(out))'''



a=10
b=20
def outer():
    c=30
    # print(a) # global access
    global a   # modifying global inside local
    a=a+10
    print(a) 

    def inner():
        # print(c) Accessing global var of outer function
        nonlocal c  #modifying c
        c=c+30
        print(c)
    inner()
outer()


