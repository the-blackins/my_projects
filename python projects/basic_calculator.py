# recieve operands from the user which will be a parameter
# define the arithmetic functions 
# begin the operation based on the arithmetic sign used 
# print the answerr

def add(a , b):
    answer = a+ b
    print(str(a) + " + " + str(b) + " = " + str(answer) + "/n")    


def sub(a , b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer) + "/n") 



def mul(a , b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer) + "/n") 



def div(a , b):
    answer = a+ b
    print(str(a) + " / " + str(b) + " = " + str(answer) + "/n") 

while True:
   print("A. Addition")
   print("B. Subtraction")
   print("C. Multiplication")
   print("D. Division")
   print("E. Exit")

   choice = input("input your arithmetic operation " + " ")

   if choice == "a" or choice =="A" :
       a = int(input("inpuit first number for operation "));
       b = int(input("input second number for operation "));
       add(a, b)
   
   if choice == "b" or choice =="B" :
       a = int(input("inpuit first number for operation "));
       b = int(input("input second number for operation "));
       sub(a, b)

    
   elif choice == "c" or choice =="C" :
       a = int(input("inpuit first number for operation "));
       b = int(input("input second number for operation "));
       mul(a, b)

   
   elif choice == "D" or choice =="d" :
       a = int(input("inpuit first number for operation "));
       b = int(input("input second number for operation "));
       div(a, b)
   
   
   elif choice == "e" or choice =="E" :
      choice = False

   else:
       print("not a value")   
