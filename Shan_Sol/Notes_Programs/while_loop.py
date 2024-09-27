'''#WAP to print 'python' 5 timnes using while loop
count = 1
while count <= 5:
    print("python")
    count += 1

#WAP to print n number of natural number using while loop
num = int(input("Enter n:"))
count = 1
while count <= num:
    print(count)
    count += 1

#WAP to print countdown(reverse order) of the no. using while loop
num = int(input("Enter a num:"))
end = 0
while end <= num:
    print(num)
    num -= 1

#WAP to add all the digits in a user entered number using while loop.
num = int(input("Enter num:"))
sum = 0
while num != 0:
    last_digit = num % 10   #to get last digit
    sum += last_digit
    num //= 10              #to remove last digit
print(sum)

#WAP to add all the digits in a user entered number only if it is an even number using while loop.
num = int(input("Enter num:"))
sum=0
if num % 2 == 0:  #to check whether the num is even or not
    while num != 0:
        last_digit = num % 10    #to get last digit
        sum += last_digit
        num //= 10           #after summation,remove last digit
    print(sum)
else:
    print("num is not an even number")


#WAP to add all the digits in a user entered number only if it is an odd number using while loop.
num = int(input("Enter num:"))
sum = 0
if num % 2 == 1:  #to check whether the last digit is odd or not
    while num != 0:
        last_digit = num % 10    #to get last digit
        sum += last_digit
        num //= 10           #after summation,remove last digit
    print(sum)
else:
    print("num is not odd number")               


#WAP to add each digit in a number only if the digits is even.
num = int(input("Enter num:"))
sum = 0
while num != 0:
    last_digit = num % 10     #to get last digit
    if last_digit % 2 == 0:
        sum += last_digit     #summation of last digit
        num //= 10            #to remove last digit after summation
    else:
        num //= 10            #to remove last digit without summation
print(sum)

#WAP to check for number palindrome without using typecasting.
num = int(input("Enter a num:"))
temp = num
rev = 0
while num != 0:
    last_digit = num % 10        #to get last digit  from the number
    rev = last_digit + rev * 10  #pushing last digit to tens place by multiplying by 10 and then adding the last_digit at ones place
    num //= 10                   #to remove last digit from the number
if temp == rev:
    print("its a palindrome number")
else:
    print("Its not a palindrome number")
    
#WAP to check for word palindrome without using typecasting.
word = input("Enter a word:")
rev = ''
index = 0
while index < len(word):        #run this loop until length of the word
    rev = word[index] + rev     #add character before the given reverse character to make the word reverse
    index += 1
if rev == word:
    print("its a palindrome")
else:
    print("its not a palindrome")

#WAP to extract all uppercase & lowercase character using while loop.
string = input("Enter a string:")
lower = ''
upper = ''
index = 0
while index < len(string):
    char = string[index]    #to get each character from the string
    index += 1
    if 'A' <= char <= 'Z':
        upper += char       #add the item in empty string if it is uppercase
    elif 'a' <= char <= 'z':
        lower += char       #add the item in empty string if it is lowercase
print(upper,lower, sep=",")

#WAP to extract all alphabet,numeric and special character from a user entered word using while loop.
word = input("Enter a word:")
alpha = ''
numeric = ''
special_char = ''
index = 0
while index < len(word):
    char = word[index]
    index += 1
    if 'A' <= char <= 'Z' or 'a' <= char <= 'z':
        alpha += char
    elif '0' <= char <= '9':
        numeric += char
    else:
        special_char += char
print(alpha,numeric,special_char,sep=",")


#WAP to extract all immutable and mutable data from a given collection.
list_ = [(10,20),10,10.5,2+1j,{10,20},{'a':23}]
mutable = []
immutable = []
index = 0
while index < len(list_):
    element = list_[index]
    index += 1
    if type(element) not in [list,set,dict]:   #if data type is not mutable means it will be immutable
        immutable.append(element)
    else:
        mutable.append(element)
print(f"Mutable data:{mutable}")
print(f"Immuatble data:{immutable}")

#WAP to check whether an element in a given list is string or not,if it is a string check whether it is palindrome or not,if the string is palindrome store it in another list.
list_ = ['hello',10,"level",(10,20),"malayalam"]
palindrome = []   #taking an empty list so that we can store the palindrome element if present
index_list = 0    #to trace list element
while index_list < len(list_):
    element = list_[index_list]
    index_list += 1
    if type(element) == str:
        index_element = 0    #to trace each char of the string
        rev = ''             #to store all the characters after reversing it char by char
        while index_element < len(element):
            rev = element[index_element] + rev
            index_element += 1
        if rev == element:
            palindrome.append(element)
print(palindrome)
'''
#WAP to mimic replace function(method) in string.

#WAP to mimic string swapcase method.
#WAP to mimic string isalpha method.
#WAP to mimic string upper method.
#WAP to mimic string lower method.
#WAP to mimic string isnumeric method.
#WAP to mimic string isupper method.
#WAP to mimic string islower method.
#WAP to display a dictionary where the keys are the characters in a string and its value will be its ASCII value.
#WAP to display a dictionary,where the keys are the characters of the string and the values are its number of occurences.
#WAP to display a dictionary whose keys are words of a sentence and its values are length of each word.
#WAP to categorized all the file nbames with respect to its extensions.
# given (files=['start.py','demo.txt','hello.py','new.py','bte.txt','same.csv'])