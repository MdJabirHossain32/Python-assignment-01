#Question 1: Variables and Data Types

#problem:01 

#Declaring Variables:
name= "Jabir"
age=22
gpa=3.5
is_student= True
#Data types:
print("Name: ",name,type(name))
print("Age: ",age,type(age))
print("Gpa: ",gpa,type(gpa))
print("is_student: ",is_student,type(is_student))



#problem:02

#Type conversion

#String to Integer
string_num="123"
integer_num=int(string_num)
print("String to Integer",integer_num, type(integer_num))

#Integer to String
integer_num=456
string_num=str(integer_num)
print("Integer to string",string_num,type(string_num))

#Float 3.99 to Integer
float_num=3.99
integer_num=int(float_num)
print("float to integer",integer_num,type(integer_num))
#Explaination:I converted the foal number into integer so only the integer part is considered as integer the decimal part is considered as float.


#integer 1 and 0 to boolean values
integer_num1=1
integer_num2=0
boolean_num1=bool(integer_num1)
boolean_num2=bool(integer_num2)
print("integer to boolean of 1",boolean_num1,type(boolean_num1))
print("integer to boolean of 0",boolean_num2,type(boolean_num2))


# Question 2: Operators

#problem 03

#operations

#Additions , Subtraction , Multiplication and Division

a=17
b=5
print("Addition",a+b)
print("Subtraction", a-b)
print("Multiplication",a*b)
print("Division",a/b)

#Floor division and Modulus
print("Floor Division",a//b)
print("Modulus",a%b)

#power
print("17 raised to the power of 5",a**b)

#Comparison
print("17 > 5",a>b)
print("17 == 5",a==b)
print("17!=5",a!=b)


#Question 3: String Manipulation

#problem :04

# String Manipulation
name= "python programming"

#Uppercase
print("Uppercase : ",name.upper())

#Title Case
print("Title case : ",name.title())

#Replace
print("Replace : ",name.replace("programming","language"))

#Total number of characters in the string
print("Total number of charecters : ",len(name))


#problem 05

 #Use of f string
name="Jabir"
age=22
gpa=3.50
print(f"My name is {name}, I am {age} years old, and my GPA is {gpa}")


#Question 4: Conditional Statements ★ Intermediate

#problem 06

#Age Checker
age=int(input("Enter your age: "))
if age >18:
  print("You are an adult")
elif age>=13 and age<=17:
  print("You are a teenager")
elif age<13:
  if age<=0:
    print("Invalid age")
  else:
    print("You are a child")
else:
  print("Enter your age correctly")


#problem 07

num=int(input("Enter a Integer number: "))
if num % 2==0:
  print("The number is Even .")
else:
  print("The number is Odd .")



#problem 08

#Grade Calculator
mark=int(input("Enter your mark: "))
if mark>=90 and mark<=100:
  print("'A+'")
elif mark>=80 and mark<=89:
  print("'A'")
elif mark>=70 and mark<=79:
  print("'B'")
elif mark>=60 and mark<=69:
  print("'C'")
elif mark>=50 and mark<=59:
  print("'D'")
elif mark>=0 and mark<50:
  print("'F'.You have failed")
else:
  print("Invalid mark !!!")


#problem 9

#Login System
fixed_username="admin"
fixed_password="1234"
attempt=0
while attempt<3:
  username=input("Enter your username: ")
  password=input("Enter your password: ")

  if username==fixed_username and password==fixed_password:
    print("Login successful! Welcome,",username)
    break

  elif username==fixed_username and password!=fixed_password:
    print("Incorrect password. Try again.")

  else:
    print("User not found.")

  attempt=attempt+1
if attempt==3:
  print("Your Account hasa been locked.")


#Question 5: ATM Simulation — Extend the Program

#problem 10

#ATM simulation
pin_num=1234
balance=10000
request=int(input("Enter the amount you want to withdraw: "))
if pin_num==1234:

  if request>500:

    if balance>=request:

       print("Successful withdrawal of",request,"Taka .")
       balance=balance-request
       print("Remaining balance: ",balance,"Taka only .")
    else:
       print("Insufficient balance !!!!")
       print ("You have ",balance,"taka only in your account .")
  else:
    print("The requested amount should be greater than 500 Taka .")

else:
  print("Try again!! Wrong pin number .")


#problem 11

#Adding an attempts counter to an ATM machine
name=str(input("Enter your namme: "))
pin_num=1234
balance=10000
attempts=3
while attempts>0:
  pin=int(input("Enter your pin number: "))
  if pin==pin_num:
    print(f"Successfully logged in Mr.{name} .")
    request=int(input("Enter the amount you want to withdraw: "))

    if request>500:

       if balance>=request:

          print("Successful withdrawal of",request,"Taka .")
          balance=balance-request
          print("Remaining balance: ",balance,"Taka only .")

       else:
          print("Insufficient balance !!!!")
          print (f"Mr.{name}You have ",balance,"taka only in your account .")
    else:
       print("The requested amount should be greater than 500 Taka .")
    break
  else:
    attempts=attempts-1
    if attempts>0:
      print(f"Wrong pin Mr.{name}!! Try again!!")
      print("Attempts remaining: ",attempts)

    else:
      print("Too many wrong pins!! ")
      print(f"Mr.{name} your Card has been blocked!!")
    break


#problem 12
# Adding a Login System before the ATM simulation

fixed_name="admin"
fixed_password="1234"

username=str(input("Enter your name: "))
password=str(input("Enter your password: "))

is_active=True

pin_num=1234
balance=10000
attempts=3

if is_active==False:
  print("Your account is disabled.")


else:
  if username==fixed_name and password==fixed_password:
    print("Login successful!!")

    while attempts>0:
      pin=int(input("Enter your pin number: "))
      if pin==pin_num:
        print(f"Successfully logged in Mr.{username} .")
        request=int(input("Enter the amount you want to withdraw: "))

        if request>500:

           if balance>=request:

              print("Successful withdrawal of",request,"Taka .")
              balance=balance-request
              print("Remaining balance: ",balance,"Taka only .")

           else:
              print("Insufficient balance !!!!")
              print (f"Mr.{username}You have ",balance,"taka only in your account .")
        else:
           print("The requested amount should be greater than 500 Taka .")
        break
      else:
        attempts=attempts-1
        if attempts>0:
          print(f"Wrong pin Mr.{username}!! Try again!!")
          print("Attempts remaining: ",attempts)

        else:
          print("Too many wrong pins!! ")
          print(f"Mr.{username} your Card has been blocked!!")
          break
  elif username==fixed_name and password!=fixed_password:
    print("wrong password!!")
  else:
    print("User not found !! ")


#Question 6: Basic Loops

#problem 13

# printing numbers from 1 to 100 using for loop
print("printing numbers from 1 to 100 using for loop")
for i in range(1,21):
    print(i)
print("\n")

#Print the multiplication table of 7 (7×1 up to 7×10)
print("Printing the multiplication table of 7 )")
for i in range(1,11):
   print("7 X",i,"=",7*i)
print("\n")

# Calculating and printing the sum of all numbers from 1 to 100
sum=0
for i in range(1,101):
  sum=sum+i
print("the sum of all numbers from 1 to 100 :",sum)
print("\n")

# Print all even numbers between 1 and 50 using range() with a step

print("Print all even numbers between 1 and 50 :")
for even_num in range(2,51,2):
  print(even_num)
print("\n")

#Printing each fruit with its position number (starting from 1)

print("Printing each fruit with its position number: ")
fruits = ['apple', 'banana', 'cherry', 'mango', 'grape']
for i in range(len(fruits)) :
  print( i+1 , fruits[i] )


# Problem 14

#Print numbers from 10 down to 1 using a while loop
print("Numbers from 10 down to 1 using a while loop :")
num=10
while num>=1:
  print(num)
  num=num-1
print("\n")

#The total sum of all valid numbers entered.
sum=0
while True:
  num=int(input("Enter a positive number (enter 0 to stop): "))
  if num==0:
    break
  sum=sum+num
print("Sum of positive numbers : ",sum)
print("\n")

#Simulate a countdown: start from 10, print each number, then print 'Blast off!'
print("Countdown:")
count = 10
while count >= 0:
    print(count)
    count -= 1
print("Blast off!")
print("\n")

# 10 multiples of 6 using a while loop3

print("First 10 multiples of 6:")

i = 1
while i <= 10:
    print(6*i )
    i += 1
