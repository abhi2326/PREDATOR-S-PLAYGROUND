#counting numbers from 1 to ten by using count +1
'''count=1
while count < 10:
    print(count)
    count=count+1'''

#using type with print to display the datatype used
'''a=10
print(type(a))'''

#using datatypes to concatinate two diffrent kinda datatypes
'''distance = 14
units = "km"
print(str(distance) + units)'''

#adding two diffrent data type: int sand float
'''x = 9
y = 3.0
print(x+y)'''

#comparison whether its true or false:(boolean)
'''print(50>100)'''

#c will display nothing as an output as the condition is neutral for c
'''a=7
b=5
c =2
if c != a-b:
    print(c)'''

#comparison usong boolean datatype
'''heart_rate = 165
peak_rate = heart_rate > 160
print(peak_rate)'''

#Define the number of iterations
'''for i in range(5):
    print("Hello")'''

#printing the range till 10 with and without displaying 10
#without 10
'''for i in range(10):
  print(i)'''
# with 10
'''for i in range(10):
  print(i)'''

#Loop using i as internal variable
'''for i in range(3):
  print(i)
print("--")  #using this print is to use as a seperator
for something in range(3):
  print(something)'''

#using while loop to print sell tickets till all tickets are sold out
'''seats = 500
while seats > 0:
  print("Sell ticket")
  seats = seats - 1'''

#another example of while loop using counter
'''counter = 0
while counter < 4:
  print(counter)
  counter = counter + 1
print(counter)'''

#to print the boolean as a result using for loop
'''for i in range(3):
  print(i < 1)'''

#printing first and second thrice  as both are in the same intend
'''for i in range(3):
  print("First")
  print("Second")'''

#using another variable name as guess to show case boolean
'''password = "SecretWord"
guess = "1234"
print(guess != password)'''

#sum of the number of items entered by the user using while loop
'''total_values = int(input("Enter the number of items in your list"))
sum = 0
count = 0
while count < total_values:
    num = int(input("Enter number {}: "))
    sum += num
    count += 1
print("The sum is:", sum)'''

#sum of the listed number by the user using for loop and also with the help of list
'''x=int(input("enter the number of items:"))
a=[]
addition=0
for i in range (x):
    a.append(int(input("enter the number")))
    addition+=sum(a)
print(addition)'''

#using break loop or continue
'''n=0
while n <10:
    n+=1
    if n%2==0:
        continue
    print(n)'''

#how to the path of the directory currently working  on and also changing the path
'''import os
print (os.getcwd())'''
#changing path
'''import os
print (os.getcwd())
os.chdir("D:\\hello")
print(os.getcwd())'''

#loop doesnt break until user provides the correct password
'''password = "SecretWord"
guess = input()
while guess != password:
  guess = input()
print("Access Granted")'''

#if and else condtion on the basis of the 'size' selection
#sets the value of age
'''age = int(input())
if age >= 18:
  print("Regular price")
else:
  print("Discount")'''

#printing outside the intendation so that the output can convay the message too
'''age = 30
if age >= 18:
  print("Regular price")
else:
  print("Discount")
print("Proceed to payment")'''

#using and operator to give output as in boolean datatype: false and true= false
'''is_student = False
age = 16
print(is_student and (age < 18))'''

#using if_student indicates whether the peron is student or not (note: false or true= false)
'''age = 32
is_student = True
if age < 18 or is_student:
  print("Discount")
else:
  print("Regular price")'''

#using is_student and age to provide discount as per the qualification/eligibility criteria for discount
'''age = 16
is_student = True or False
if age < 18:
  if is_student:
    #execute if under 18 and also a student
    print("20% discount")
  else:
    #execute if under 18 and not a student
    print("10% discount")
else:
    print("Regular price")'''

#
'''age = 29
if age < 18:
  if is_student:
    print("20% discount")
else:
  print("Regular price")
print("Proceed to payment")'''


#LISTS


#Displaying the items stored inside the particular list
'''shopping_cart = [
  "laptop",
  "smartphone",
  "headphones",
  "backpack"
]
print(shopping_cart)'''

#Changing the name of the element from the list itself
'''products = ["apples", "oranges", "bananas"]
products[2] = "lime"
print(products[2])'''

#displaying the name, age, country as the data is stored outside the list
'''name = "Sarah"
age = 34
country = "Germany"
info = [name, age, country]
print(info[0])
print(info[1])
print(info[2])'''


#using list to display any characters in order of indexing
'''characters = "!#- ?"
print(characters[4])'''

#using list to display any month's character in order of indexing
'''month = "august"
month[0] = "A"'''

#using colon to print/display any two elements from the list according to the user
'''animals =["cat", "dog", "bird", "cow"]
print(animals[1:3])'''


#SLICING


#using colong after the indexing got print the first 3 elements from the given list
'''cart = ['lamp', 'candles', 'chair', 'carpet']
print(cart[:3])'''

#using just colon : to print the whole element from the string as well as the list
'''vehicle = 'motorbike'
print(vehicle[:])'''

#using negative indexing to print 4rth value from the list
'''c = ['$', '£', '€', '¥']
print(c[-1])'''

#using positive and negative indexing to print 2nd and 3rd value from the list
'''c = ['$', '£', '€', '¥']
print(c[1:-1])'''

#changimg the value stored in the list using c[1] as lists are mutable
'''c = ['$', '£', '€', '¥']
c[1] = '₣'
print(c)'''

#printing the 4rth value that is stored in the particular list
'''c = ['$', '£', '€', '¥']
print(c[-1])'''


#FUNCTIONS


#DISPLAYING MULTIPLE VALUES IN THE SAME LINE
'''print("Your seat:", 4)'''

#print function accepts the arguments of any data type
'''print("Online:", True) 
print("Credit:", 385.91) 
print(2, "bananas")'''

#the print() function can accept math, logical and comparison operations.
'''print(55 * 3) 
print(5 > 7) 
print(True and False) 
print("motor" + "bike") '''

#concatenation of two strings
'''x = "air"
y = "plane"
print(x + y)'''

#finding any particular character from the string formed using find function
'''print("robot".find("A"))'''

#finding any particular character from the string formed using find function but if its not present output will be (-1)
'''word = 'vehicle'
print(word.find('r'))'''

#using len to find the number of characters re there in a particular string
'''movie = "Avatar"
print(len(movie))'''

#using append function to simply add any particular element/data in the list only
'''songs = ["Yesterday", "Hello", "Believer"]
songs.append("Imagine")
print(songs)'''

#using insert and append function both to print the desierd output usung indexing
'''colors = ["Red", "Blue", "Yellow"]
colors.insert(2, "Green")
colors.append("Black")
print(colors[3])'''

#using pop function to delete any particular element from the list
'''items = ["book", "pen", "pencil"]
items.pop(1)
print(items)
print(items[1])'''

#using def to define any particular element as with same amt of data block so that it can be called again and again

'''def greet():
  print("Hello from a function")
  print("Have a great day")
greet()#function call'''

#using proper use of the def funtion to built a greeting message
'''def personal_greet(name):
  print("Hello", name)
  print("Have a great day")
personal_greet("Sarah")
personal_greet("Henry")'''

#calculating bmi of any person by just using arguements with th help of def function
'''def bmi(weight, height):
  index = weight / (height * height)
  return index 
patient_5 = bmi(61, 1.83)
print("underweight:", patient_5 < 18.5)
patient_7 = bmi(75, 1.74)
print("underweight:", patient_7 < 18.5)'''

#printing area and parameter of rectangle
'''def rect(length, width):
  area = length * width
  perimeter = 2 * length + 2 * width
  return area, perimeter
x, y = rect(50, 100)
print(x, y)'''

#using def to make a greeting message and then doing changes in that
'''def greet(name="Guest"):
  print("Welcome", name)
greet("Anna")'''
