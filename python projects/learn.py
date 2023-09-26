
# print('hello\n samuel')
   # character_population ="5"
# print("hello world your current population  is censused to " + str(character_population) + "billion" )
# phrase = "AKINYOOLA SAMUEL"
# print(len(phrase))
#
# print(phrase.lower())
#
# print(phrase[8])
# print(4)

# prints out absolute value of an integer
# mathematical operations
#  % modulus
#  abs() for absolute value
#  str() to stringify a num
#  bodmas
#  pow(num1 , num2) power function
# provides math operations from python library
# from math import*

# recieving input data

# name = input("what is your name:")
# print("hello " + name)
# to convert str to number int() and float() for decimals could be used

# num1 = input("input number: ")
# num2 = input("input number: ")
# result = float(num1) + float(num2)
# print( result)
""" 
color = input("Enter a color:")
plural_noun = input("Enter a plural noun of your choice:")
celebrity = input("Enter your fav celebrity:")
print( "Roses are "+ color)
print( plural_noun +" are blue")
print("i love " + celebrity) """

# working with list

"""
append 
len
in
extend
[using of negative numbers listr start counting from behind]
# dogs+=["akinyoola", 18] also used as extension
dogs.remove()
dogs.insert(3, "third list")
print(dogs.sort(key=str.lower))
print(sorted(ite))


basic list functions
 """
""" prints from the first value indicated index and end before the last value indicated co
lucky_numbers = [2,6,6,9,6,48,4,3,66,6,7,8,8,3,367,7,4,3,3,5,]
friends =["sam", "segun", "praise","sam=", "segu", "prais-le"]
print(friends[1:3])
to extend lists

print(friends)


import random

def get_choices():
 player_choice = input("pick a choice(rock, paper, scissors)")
 options = ['rock' ,'paper', 'scissors']
 computer_choice = random.choice(options)
 choices = {"player": player_choice, "computer": computer_choice}
 return choices

def check_win(player, computer):
 print(f"You chose { player} , computer chose {computer}")
 if player == computer:
  return "we have a tie"
 elif player == "rock": 
  if computer=="scissors":
   return "rock smashes paper so therefore its a win!!"
  else:
  
   return "paper covers rock! you loose !!"
 elif p0layer == "paper": 
  if computer=="scissors":
   return "scissors cuts paper! you loose!!"
  else:
   return "paper covers rock! you win !!"
 elif player == "scissors": 
  if computer=="paper":
   return "scissors cuts paper! you win!!"
  else:
   return "rock smashes scissors! you loose !!"

choices = get_choices()
result = check_win(choices["player"] , choices["computer"])
print(result)


complex for complex num
bool fo booleans
list for lists
tuple for tuples
range for ranges
dict for dictionaries
set for sets


arithmetic operators
// divides (output is in integer datatype)
abs(absolute value)
round(4.784, 1)
complex numbers
num = 2+3j
num2 = complex
print(num.real num2.imag)


name = "boluwatife"
print(name[1:4])
 this implies that it prints out the letter indexed 1 to 3 it is called range

 done = True
print(type(done)==bool)

 testing for a a variable datatype 
name = "samuel"
print(isinstance(name, float))

# dictionaries
dogs = ["roger", 1, "syd", True, "quincy", 7]    

dogs[2] = "samuel"
dogs += ["akinyoola", 18]

dogs.remove("roger")
 
print(dogs.pop())react  
print(dogs) 

dogs.insert(3,"aduragbemi")

dog_char ={ "name": "vegas", "breed":"german shepard", "height": "3 ft"}

dog_char["favourite food"]= "meat"
print(list(dog_char.values()))
print(list(dog_char.items()))
print(len(dog_char))

del dog_char["height"]
print(dog_char)



 

ingredient_purchase = True
meal_cooked = False
 any which is a global variable that check if any of a list items 
is true returning a true value 
ready_to_serve = any([ingredient_purchase, meal_cooked])
print(ready_to_serve)


ingredient_purchase = True
meal_cooked = False
all which is a global variable that check if all of a list items 
is true returning a true value
ready_to_serve = all([ingredient_purchase, meal_cooked])
print(ready_to_serve)

from enum import Enum

class State (Enum):
 inactive = 0
 active = 1

print(len(State))

# sets

names = {"sam", "akin","butter "}
name2 = {"sam", "akin"}

intersect = names & name2

# union or modification
# mod = names / name2


mod = names - name2
print(mod)

# superset < or >

#functions
def hello(name, age):
    print("hello "+ name + " you are " + str(age)+ " years old")

hello("samuel", 8)    

# return function

def hello(name, age):
    print("hello "+ name + " you are " + str(age)+ " years old")
    return name, "garet", 7

    
print(hello
      ("sam",10 )
      )



      
def talk(phrase):
    def say(word):
        print(word)


    words = phrase.split(' ')
    for word in words:
        say(word)

talk('i am going to the mall next week')



      # global variable  a viariable which can be used within and outside a function

name = "samuel"

def hello(name):
    print("hello "+ name)

hello(name)
print(name)

# local variable 

def hello():
    name = "samuel"
    print("hello "+ name)

hello()
print(name)


def starting_num():
 count = 0
    
def increament():
    nonlocal count
    increase = count + 1
    print(increase)
    
increament()

starting_num()

# function
# return function
# variable scope

# a parameter is the value accepoted by a function by a function definition

# nested function
# split is to create a list out of a string


# objects

items=[1,2,3]
items.append(4)
items.pop()
print(items)
print(id(items))

# loops
# while loops


count = 0
while count < 10:
    count = count + 1
    
    print(count)

print(" after the loop")


 # items = [1, 2, 3, 4]
for item in range(110):
    print(item) 

# continue & break
items = [1, 2, 3, 4]
for item in items:
    if item == 2:
        break    # continue
    print(item)

# enumerate
items = [1, 2, 3, 4]
for index, item in enumerate(range(10)):
    print(index, item)


    #  classes
class animal:
    def walk(self):
        print("walking")


class Dog(animal):
    # constructor used to initialize more
    #  properties when u create an object from 
    # that class

    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def bark(self): 
        print("woof!")

roger = Dog("billy", 12)

print(roger.name)
roger.bark()
roger.walk()



 # standard library created for python
 math 
  re  for regular expression 
  json
   datetime
    sqlite3
     os operating system
      random
      statistics
      request to perform https network request
      http to create http servers
      urllib to manage urls


      # modules
# take note: modules work with position of file
from lib.module1 import bark

bark()

# accepting argument

import argparse

parser = argparse.ArgumentParser(
    description='this program prints the name of my dogs'
)

parser.add_argument('-c', '--color', metavar ='color', required=True, choices={'red', 'yellow'}, help='the color to search for')
args = parser.parse_args()

print(args.color)



# lambda num : num * 2
multiply = lambda a, b: a * b
# multiply = lambda num : num*2
print(multiply(2,5)) 


# def multiply(a):
#     return a *2

# result = map(multiply, numbers)
# print(list(result))

# # filter
# def isEven(n):
#     return n % 2 == 1
# result = filter(isEven, numbers)


  
numbers = [3, 4, 5, 6, 7]

result = filter(lambda n : n % 2 == 0, numbers)

print(list(result))  


# map() filter() reduce()

from functools import reduce
# map used to run a function 

expenses = [
    ('dinner',80),
    ('car repair', 120),
    
]

sum = 0
for expense in expenses:
    sum += expense[1]

# using reduce from a standard library 
sum = reduce(lambda a,c : a[1] +c[1], expenses)
print(sum)

# recursive function a function that calls iself`` 

def factorial(n):
    if n ==1: return 1
    else:
         return n* factorial(n-1)

print(factorial(1))


# decorators alters a function behaviour without changing the functio itseklf

def logtime(func):
     def wrapper():
          print("before")
          val = func()
          print('after')
          return val
     return wrapper
@logtime
def hello():
     print("hello")
hello()



# exception handles error

try:
    result = 2/1
except ZeroDivisionError:
    print('cannot divide by zero!')
finally:
    result = 1

print(result) 

class DogNotFoundxception(Exception):
    pass

try:
    raise DogNotFoundxception()
except DogNotFoundxception:
    print('dog not found')


filename = 'r.js'

with open(filename, 'r') as file:
    content = file.read()
    print(content)


    # pip
# operator overloading

class Dog:
    # the dog class
    def __init__(self, oruko, age) :
        self.oruko
        self.oruko= oruko
        self.age = age
    def __gt__(self, other):
        return True if self.age > other.age else False
roger = Dog("roger", 17)
syd  = Dog('syd', 15)

print(roger > syd)


blackjack notation

cards_dealt = deal(2)
card = cards_dealt[0]   # to get th first item in the cards list
rank = card[1]

if rank == "A":
   value = 11
elif rank =="j" or rank == "Q" or rank =="k":
   value = 10
else:
   value = rank

rank_dict = {"rank": rank, "value": value}
print(rank_dict["rank"], rank_dict["value"] )
rank["range"] = "3 years" to modify by adding items

shuffle()
card = deal(1)[0 ]
print(card[1]["value"])

 boy = 'the man  fornicated'
print(boy[0].upper())

print(boy)


advance python

for integer in "1234":
    print(integer)
    if integer == "3":
        break #stops a for loop from running after an if condition is met
    
try: #helps in error hhandling
    x = int(input("input an integer "))
    print(x)
except ValueError: #
    print("invalid input")
else:
    print("nothing went wrong")
finally: #runs even if there is an error or not
    print("try except finished")
    
reading a file in python
# r reading of the file- can read file
# w can write file
# r+ can read and write ile
# a means to append to the file usually done at the ending

# reading external files in python 
# readable() checks if a file is readable
# readline reads the first line in the file
# readlines  reads the  lines in the file and storing it in a list
# print(country_file.readlines()[5])

country_file = open ("text.txt", "r")
for countries in country_file:
    print(countries)
country_file.close()

# writing a file
country_file = open ("writableTxtFile.txt", "w")
country_file.write("this is part of the new  file")
country_file.close()
    
# appending  a file
country_file = open ("text.txt", "a")
country_file.write("\nthis is part of the new  file")
country_file.close()

working with classes

# creating a class
class Myclass:
    x = 5 

# creating an object in the class 
p1 =  Myclass()
print(p1.x)


working with class and objects

class person:
    def __init__(self, name, age) -> None:
        self.name = name 
        self.age = age
    pass #avoids errors
p1 = person("john", 4)
p1.name = input("enter your name ")
p1.age = input("user age is required for this input ")
print(p1.name)
print(p1.age )




age = input("user age is required for this input ")
name = input("enter your name ")
p1 = person(name, age)
del p1.age #todelete a class
print(p1)

  
# working with inheritance
from module1 import student

class person(student):
    pass
p1 = person()
print(p1.name)
"""
# working with dictionaries






student = {
    "name": "samuel",
    "age": 25,
    "courses": ["computer science", "math"]
}
# adding new value to your dictionary
# student["phone"] = 0o4444 result 2340
student["phone"] = '090340123'
# uptating key values in a dict
student.update({
    "name": "sal",
    "age": 15,
    "courses": ["computer", "mathatics"]
})
# removing a key and value from a dict using pop and del .
del student["name"]
print(student)  
age = student.pop("age")
print(age )
# handling error for a nonexisting key 
print(student.get("phone", "not found"))

# using the keys and value 
print(student.keys())
# print(student.values())
for key, value in student.items():
    print(key, value)
# for value in student:
#     print(value)