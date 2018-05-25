#!/usr/bin/python3

#import of libraries
from math import pow, sqrt 
from time import sleep
from os import system
from sys import exit

#function definitions:
def add(x,y):
 return x+y

def sub(x,y):
 return x-y

def mul(x,y):
 return x*y

def div(x,y):
 return x/y

def power(x,y):
 return pow(x,y)

def square(x):
 return sqrt(x)

chars = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(){}:,./+-"

def char_count(string,char):
 count=0
 for c in string:
  if c == char:
   count+=1
 return count

def second_function():
 print("Now, this program is going to show the amount of each character in a defined string.")
 while True:
  string = input("\n\nPlease enter a string: ")
  if string == "":
   continue 
  else:
   break
 if string == 'Exit' or string == 'EXIT' or string == 'exit':
  exit()   
 print("\n\nThe entered string is: %s" % (string))
 sleep(5)
 for char in chars:
  if char == "a":
   print("\n")
  print("The amount of %s characters in the string is: %s" % (char, char_count(string,char)))
  sleep(1)

def output1():
 system("cat /proc/partitions | grep -w sd[a-z] | awk '{print $4}' | tr '\n' ' ' | uniq")

def output2():
 system("cat /proc/partitions")

def third_function():
 sleep(2)   
 print("\n\nDisk labels in this PC are: ")  
 output1()
 sleep(2)
 print("\nand the partitions here are the following: \n")
 output2()
 sleep(5)

def back():
 print("##########Going back to the beginning of the program##########\n") 

def enter():
 while True:
  hit = input("\nHit any key to start again the program or type exit to quit: ")
  if hit == 'exit' or hit == 'EXIT' or hit == 'Exit':
   print("\n\nGoodbye!!!!\n\n")
   sleep(5)
   system('clear')
   exit()
  else:
   system('clear')
   back()
   break

def invalid():
 for x in range(5):
  print ("\n\nINVALID OPERATION TYPE!!!!!\n\n")
  sleep(1)
 system('clear')

system('clear')

#Main program loop:
while True:
 system('date')   
 print("\n\n##########Siema, this is a simple program, that can add, subtract, multiple and divide and is doing something else##########\n")
 print("\nNow please select a valid operation for the calculator. Valid opertions are:")
 print("\nAdd, Sub, Mul, Div, Pow, Sqrt\n")

 while True:
  choice = input("\nPlease enter the valid operation here(type exit to exit program): ")
  if choice == "":
   continue
  else:
   break

 if choice == 'Add' or choice == 'add':
  num1 = int(input("\nPlease enter the first value here: "))
  num2 = int(input("\nPlease enter the second value here, to be added to the first value: "))
  print ("\n\n")
  print ("########## %s + %s = %s ##########" % (num1, num2, add(num1,num2)))
  print ("\n\n")
  second_function()
  third_function()
  enter()
  continue
 if choice == 'Sub' or choice == 'sub':
  num1 = int(input("\nPlease enter the first value here: "))
  num2 = int(input("\nPlease enter the second value here: "))
  print ("\n\n")
  print ("########## %s - %s = %s ##########" % (num1, num2, sub(num1,num2)))
  print ("\n\n")
  second_function()
  third_function()
  enter()
  continue
 if choice == 'Mul' or choice == 'mul':
  num1 = int(input("\nPlease enter the first value here: "))
  num2 = int(input("\nPlease enter the second value here: "))
  print ("\n\n")
  print ("########## %s * %s = %s ##########" % (num1, num2, mul(num1,num2)))
  print ("\n\n")
  second_function()
  third_function()
  enter()
  continue
 if choice == 'Div' or choice == 'div':
  num1 = int(input("\nPlease enter the first value here: "))
  num2 = int(input("\nPlease enter the second value here and the first value will be divided by this value: "))
  print ("\n\n")
  print ("########## %s / %s = %s ##########" % (num1, num2, div(num1,num2)))
  print ("\n\n")
  second_function()
  third_function()
  enter()
  continue
 if choice == 'Pow' or choice == 'pow':
  num1 = int(input("\nPlease enter the first value here: "))
  num2 = int(input("\nPlease enter the second value here to raise the first value to the power of this value: "))
  print ("\n\n")
  print ("########## %s ^ %s = %s ##########" % (num1, num2, pow(num1,num2)))
  print ("\n\n")
  second_function()
  third_function()
  enter()
  continue
 if choice == 'Sqrt' or choice == 'sqrt':
  num1 = int(input("\nPlease enter the value here: "))
  print ("\n\n")
  print ("########## square of %s = %s ##########" % (num1, square(num1)))
  print ("\n\n")
  second_function()
  third_function()
  enter()
  continue
 if choice == 'exit' or choice == 'EXIT'or choice == 'Exit':
  print("\n\nGoodbye!!!!\n\n")
  sleep(5)
  system('clear')
  break 
 else:
  invalid()
  continue
#End of the program
#More functions later
