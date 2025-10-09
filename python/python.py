# مفهوم پرینت گرفتن  درس اول
# print("hello world")

# کامنت کردن 
# <#>   <----------

# متغییر ها 
# a = 12
# b = 12
# sum = a + b
# print(sum)

# a = 12 + 12
# print(a)


#  data type in the python
# str 
# int integer
# float
# set list tupel
# bool 
# byte 
# nonetype

# a = "yas"
# print(type(a))  <---- خروجی نوع داده را از این طریق می گیرند

# Slicing Strings برش رشته ها
# a = "hello world"
# print(a[2:6])

#  متد در رشته 
# a = "yas"
# sum = a.upper()
# print(sum)

# وصل کردن رشته ها
# a = "yas"
# b = "mirhabibi"
# sum = a + b
# print(sum)

# Format Strings
# name = "yas"
# print(f"hello MR {name}")


# Escape Characters
# \'	Single Quote	
# \\	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \f	Form Feed	
# \ooo	Octal value	
# \xhh	Hex value


# انواع متد در رشته
# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	    Returns a centered string
# count()	    Returns the number of times a specified value occurs in a string
# encode()	    Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	    Searches the string for a specified value and returns the position of where it was found
# format()	    Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	    Searches the string for a specified value and returns the position of where it was found
# isalnum()	    Returns True if all characters in the string are alphanumeric
# isalpha() 	Returns True if all characters in the string are in the alphabet
# isascii()	    Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	    Returns True if all characters in the string are digits
# isidentifier()    Returns True if the string is an identifier
# islower()	    Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace() 	Returns True if all characters in the string are whitespaces
# istitle() 	Returns True if the string follows the rules of a title
# isupper() 	Returns True if all characters in the string are upper case
# join()	    Joins the elements of an iterable to the end of the string
# ljust()	    Returns a left justified version of the string
# lower()	    Converts a string into lower case
# lstrip()  	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	    Returns a string where a specified value is replaced with a specified value
# rfind()	    Searches the string for a specified value and returns the last position of where it was found
# rindex()	    Searches the string for a specified value and returns the last position of where it was found
# rjust()	    Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	    Splits the string at the specified separator, and returns a list
# rstrip()	    Returns a right trim version of the string
# split()	    Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	    Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	    Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	    Converts a string into upper case
# zfill()	    Fills the string with a specified number of 0 values at the beginning


# bool
# a = "yas"
# b = 10
# print("y" in a)


# عملگرهای محاسباتی پایتون

# +	Addition	x + y	
# -	Subtraction	x - y	
# *	Multiplication	x * y	
# /	Division	x / y	
# %	Modulus	x % y	
# **	Exponentiation	x ** y	
# //	Floor division	x // y


# عملگرهای انتساب پایتون
# =	    x = 5	    x = 5	
# +=	x += 3	    x = x + 3	
# -=	x -= 3	    x = x - 3	
# *=	x *= 3	    x = x * 3	
# /=	x /= 3	    x = x / 3	
# %=	x %= 3	    x = x % 3	
# //=	x //= 3	    x = x // 3	
# **=	x **= 3 	x = x ** 3	
# &=	x &= 3	    x = x & 3	
# |=	x |= 3	    x = x | 3	
# ^=	x ^= 3	    x = x ^ 3	
# >>=	x >>= 3	    x = x >> 3	
# <<=	x <<= 3	    x = x << 3	

# عملگرهای مقایسه‌ای پایتون
# ==	Equal	x == y	
# !=	Not equal	x != y	
# >	Greater than	x > y	
# <	Less than	x < y	
# >=	Greater than or equal to	x >= y	
# <=	Less than or equal to	x <= y	


# عملگرهای منطقی پایتون

# and 	Returns True if both statements are true	x < 5 and  x < 10	
# or	Returns True if one of the statements is true	x < 5 or x < 4	
# not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)	

# اولویت عملگرها
# () * / +-     
# نکته همیشه اولویت از سمت چپ خوانده میشه



# list
# Create a List:

# thislist = ["apple","banana","charry"]
# print(thislist)


# List Length طول لیست
# thislist = ["apple", "banana", "cherry"]
# print(len(thislist))


# بدشت اوردن نوع لیست از طریق شی type()
# thislist = ["apple", "banana", "cherry"]
# print(type(thislist))

# تبدیل هر چیزی به لیست از طریق شی زیر انجام می شود
# thislist = list(("apple","banana","cherry"))
# print(thislist)

#دست یافتن یه لیست 
# thislist = ["apple", "banana", "cherry"]
# print(thislist[1])

# نکته مهم : این است که در لیست یا تاپل یا ست همیشه ایتم های درونش از 0 شروع می شود
# -------------------------------------------------

# هرگاه در سرچ کردن ایتم ها منفی قبل از عدد اضافه کنیم یعنی اینکه میخواهیم ایتم های سمت راست را استفاده کینم

# thislist = ["apple", "banana", "cherry"]
# print(thislist[-1])

# خروجی این کد میشود (cherry)

# ---------------------------------

# بعضی اوقات ما میتوانیم چند ایتم را برگردانیم مانند کد زیر 

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])

#['cherry', 'orange', 'kiwi'] خروجی کد میشود 

# --------------------------------------------------------

# بعضی اوقات میشود که هیچ عدد برای شروع نزاریم و به صورت دیفالت خود برنامه تخیص بده که می خواهد از اول شروع شود 

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[:4])
#  خروجی کد میشود ['apple', 'banana', 'cherry', 'orange']

# ------------------------------------------------------------------------

# 
# تغییر ایتم های درون لیست

# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)

# یا تغییر دوتا ایتم

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)

# یا از طریق یک ایتم را انتخاب و جلوی ان ایتم جدید را لحاظ کتنید

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)

# ------------------------------------------------------------------

# اضافه کردن ایتم به لیست

# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)

# ترکیب دولیست 

# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)

# --------------------------------------------------

# حذف یک ایتم درون لیست

# fruits = ['apple', 'banana', 'cherry']
# fruits.remove('apple')


# حذف ایتم از طریق شماره ایندکس 
# fruits = ['apple', 'banana', 'cherry']
# fruits.pop(1)
# print(fruits)

# طریق یک ابجکت del
# fruits = ['apple','banana','cherry']
# del fruits[0]
# print(fruits)

# پاک کردن کامل لیست 
# clear()
# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)

# --------------------------------------

# loop in the list

# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#   print(x)


# پروژه ی  که میوه هایی اولشون aداشته باشد را بریز داخل new list

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#     if "a" in x:
#         newlist.append(x)
# print(newlist)        

# ساده کردن کد بالا 
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if "a" in x]
# print(newlist)


# پروژه  فقط اعداد کمتر از ۵ را می‌پذیرد:

# newlist = [x for x in range(10) if x<5]
# print(newlist)

# ----------------------------

# مرتب سازی لیست ها 

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)

# براساس عدد

# thislist = [100, 50, 65, 82, 23]
# thislist.sort()
# print(thislist)

# تنظیم لیست به صورت نزولی
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(reverse = True)
# print(thislist)

# یک مرتب‌سازی غیرحساس به حروف بزرگ و کوچک در لیست انجام دهید:

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort(key = str.lower)
# print(thislist)

# چاپ معکوس لیست
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.reverse()
# print(thislist)

# ------------------------------------------------

# کپی کردن لیت ها 

# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print(mylist)



# به دو لیست بپیوندید:

# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# list3 = list1 + list2
# print(list3)

# لیست ۲ را به لیست ۱ اضافه می‌کند:

# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# for x in list2:
#   list1.append(x)

# print(list1)



# انواع متد های لیست

# append()	--> اضافه کردن آِتم به لیست
# clear()	--> پاک کردن کامل لیست
# copy()	--> کپی لیست ب خصورت کامل 
# extend()	--> به پیوند دادن یک لیست به لیست دیگر
# insert()	--> اضافه کردن ایتم به لیست در محل تعیین شده
# pop()	    --> اضافه کردن ایتم به لیست از طریق شماره ایندکس 
# remove()	--> پاک کردن ایتم لیست از طریق  ایندکس لیست
# reverse()	-->  مرتب سازی لیتس براساس نزولی
# sort()	--> مرتب سازی لیست


# ----------------------------------------------------------------


# تاپل ها

# ساخت یک تاپل

# thistuple = ("apple", "banana", "cherry")
# print(thistuple)


# انواع داده در تاپل 

# tuple1 = ("apple", "banana", "cherry") str
# tuple2 = (1, 5, 7, 9, 3) number or int
# tuple3 = (True, False, False) bool

# نوع داده یک تاپل چیست؟
# mytuple = ("apple", "banana", "cherry")
# print(type(mytuple))

# تبدیل هر چیزی به تاپل از طریق زیر انجام می شود 
# thistuple = tuple(("apple", "banana", "cherry"))
# print(thistuple)



#  نکته بسیار مهم هرچیزی که تا الان دربارهی لیست یاد گرفتیم برای تاپل هم شاما میشود 


# ----------------------------------------------------------------------

# ایجاد یک مجموعه:
# set
# thisset = {"apple", "banana", "cherry"}
# print(thisset)
#  نکته بسیار مهم هرچیزی که تا الان دربارهی لیست یاد گرفتیم برای ست هم شاما میشود 

# Python Dictionaries

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# طول یک دیکشنری

# print(len(thisdict))

# انواع داده در دیکشنری

# thisdict = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# }

# تبدیل هر چیزی به دیکشنری از طریق زیر انجام میشودذ 

# thisdict = dict(name = "John", age = 36, country = "Norway")
# print(thisdict)



# if and else

# در اینجا باید عملگر های مقایسه ای  و منطقی یاد گرغته باشیم.

# a = int(input("what s numer1 :"))
# b = int(input("what s numer2 :"))



# if a==b:
#     print("ok")

# elif a<b:
#     print("a<b")


# a = int(input("what s numer1 :"))
# b = int(input("what s numer2 :"))

# if a<b:print("ok")


# a = int(input("what s numer1 :"))
# b = int(input("what s numer2 :"))

# print("ok") if a<b else print("NO")

# تمرین تعیین سن برای سربازی 

# age = int(input("how old are you : "))


# if age < 18 : 
#     print("naro sarbazi")
# else:
#     print("bro ssarbazi")



#  اینکه هرگاه نمی خوایم از دستورات شرطی استفاده کنیم باید یک کلید واژه را تعیین  کنیم

# pass

# a = 12

# if a<10:
#     pass

# match

# day = 1

# match day:
#     case 1:
#         print("شنبه")
#     case 2:
#         print("یکشنبه")


# while 

# a =1


# while a<=10:
#     print(a)
#     a+=1

# a = 1

# while a<10:

#     print(a)
#     a+=1
#     if a==3:
#         break



# for

# for x in range(0,11):
#     print(x)

#     if x==3:
#         continue




# for x in range(0,11):
#     print(x)

#     if x==3:
#         break








# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     break
#   print(x) 





# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     continue
#   print(x)





# -----------------------------------------------------------------------



#  اصل ماجرا


# ساخت توابع

# def hello ():
#     print("hello mr")

# hello()

# def person(fname,lname):
#     print(f"hello mr name shoma ast in {fname} va familly shoma in ast {lname}") 

# person("yasin","mirhabibi")




#args*



# def yasin(*kids):
#     print("your chil you: "+kids[2]) 

# yasin("email","phone","number")




    # def kids(child1,child2,child3):
    #     print("child entred " + child1)

    # kids(child1="yas",child2="mamad",child3="hossein")



# -----------------------------------------------------------------

# ساده کد بالا


# def kids(**kids):
#     print("hello kid " + kids["lname"])

# kids(fname = "yas",lname="miri",age=17)


# مقدار پارامتر پیش‌فرض

# def my_function(country = "Norway"):
#   print("I am from " + country)

# my_function("Sweden")
# my_function("India")
# my_function("iran")
# my_function("Brazil")


# def my_function(food):
#     for x in food:
#        print(x) 

# fur = ["banana","cherry","apple"]
# my_function(fur)






# ============================================






# lambda

# x =  lambda a : print("hello "+a)

# x("yasin")






# مبحث شی گرایی (oop)
# class and object

# class yas:
#     x = 12

# p1 = yas()
# print(p1.x)




# -----------------------------------

# class person:
#     def __init__(self,name,fname):
#         self.name = name
#         self.fname = fname
    


# p1 = person("yasin ","mirhabibi")
# sum = p1.name + "" + p1.fname
# print(sum)



# ساده کردن کد بالا 





# class person:
#     def __init__(self,name,fname):
#         self.name = name
#         self.fname = fname
    
#     def __str__(self):
#         return f"{self.name},{self.fname}"

# p1 = person("yasin","mirhabibi")
# print(p1)




# چاپ از طریق توابع


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def myfunc(self):
#     print("Hello my name is " + self.name)

# p1 = Person("John", 36)
# p1.myfunc()





# ----------------------------------------




# وارث

# class Person:
#     def __init__(self,name,fname):
#         self.name = name
#         self.fname = fname

#     def printsum(self):
#         print(f"{self.name},{self.fname}") 

# class students(Person):
#     def __init__(self,name,fname):
#         super().__init__(name,fname)


# x = students("yasin","mirhabibi")
# x.printsum()




# Iterator 


# mytuple = ("appel")

# myit = iter(mytuple)
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))



# mytuple = ("apple", "banana", "cherry")

# for x in mytuple:
#     print(x)




# class car :
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
    
#     def move(self):
#         print("Drive")

# class Boat:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model


#     def move(self):
#         print("Sail !")

# class Plane:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
    
#     def move(self):
#         print("Fly !")

# car1 = car("Ford", "Mustang")
# boat1 = Boat("Ibiza", "Touring 20")
# plane1 = Plane("Boeing", "747")


# for x in (car1,boat1,plane1):
#     x.move()



# import datetime


# a = datetime.datetime.now()
# print(a.month)





# math




# abs قدر مططلق
# min کوچک ترین
# max بزرگ ترین
# pow توان 
#   میشه استفاده کردmathاین چیز های بدون ماژول 





# a = min(1,3)
# v = max(12,14)
# d = abs(12)
# s = pow(2,3)

   



# ولی چز های پایین باید حتما با استفاده از ماژول استفاده کرد

# import math

# x = math.sqrt(64)   جذز گرفتن

# print(x)




# x = math.ceil(1.4) عدد را به بالا گرد میکنذ
# y = math.floor(1.4) عدد را به پایین گرد می کند
# x = math.pi  عدد پی








# json

#  js تبدیل یک فایل پایتون  به 
# یا برعکس


# import json

# # a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }

# # convert into JSON:
# y = json.dumps(x)

# # the result is a JSON string:
# print(y)















# import json

# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))















# python      js

# dict	    Object
# list	    Array
# tuple	    Array
# str	    String
# int	    Number
# float 	Number
# True	    true
# False	    false
# None	    null











# pip 

# برای نصب کتابخانه یا هرچیزی برای پایتون

# pip install (چیزی برای نصب )














































































# تمرین های جالب 

# from colorama import Fore
# print(Fore.RED + "yasin")
# print(Fore.BLUE + "yasin")








# 2 تمرین های جالب 

 
#   بنویسی برات تو ویس ذخیره میگنه داخ همون فایل پایتون که باز کردی و میگه text  این کاری انجام میده هرچیزی داحل 


# import asyncio
# import edge_tts

# async def main():
#     text = "سلام خسته نباشید به چنل هیولرن خوش آمدید"
#     voice = "fa-IR-DilaraNeural"
#     out_path = "voice.mp3"

#     # ساختن شی Communicate (بدون await)
#     communicate = edge_tts.Communicate(text, voice)

#     # ذخیره‌سازی صدا (await لازم است)
#     await communicate.save(out_path)

#     print("🥸 فایل ذخیره شد :", out_path)

# # اجرای تابع async
# asyncio.run(main())







# تشخص زوج بودن عدد

# a = 12

# if a % 2 == 0:
#     print("ok")
# else:
#     print("no")   






