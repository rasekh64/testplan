import os
from math import *
from Student import Student
import array

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


charachter_name = "hasan"
character_age = "28"
age2 = 44

print("heloo\nworld")
print("heloo\" world")
print(charachter_name + " is " + character_age + ".")

phrase = "Giraffe Academy"

print (phrase.lower() + phrase.upper())
print (phrase.isupper())
print (phrase.upper().isupper())
print (phrase[0])
print (phrase.replace("Giraffe", "Elephant"))
print(os.getcwd() + "\n")

print (pow(2, 3))
print(round(3.5))
print (sqrt(25))
print(str(age2) + " is" + charachter_name + "'s age.")
cmd = 'date'
os.system(cmd)

# my_name = input ("Enter your name: ")
# age = input("enter your age: ")
# print("hello " + my_name+ "! you are " +age )
# num_1 = input("enter a number: ")
# num_2= input("enter another number: ")
# print (num_1*num_2)
friends = ["xevin", "carin", "jim"]
friends.sort()
print(friends)

# Tuple
coordinates = (4, 5)
print (coordinates[1])


# function

def say_hi(name, age):
    print ("hello " + name + ", you are " + age)


say_hi("Ali", "34")


def cube(num1):
    return num1 * num1 * num1


print(cube(4))

# if statement

is_male = True
is_tall = False

if is_male and is_tall:
    print("you are a male or tall")
elif is_male and not (is_tall):
    print ("you are a short male")
else:
    print("you are neither a male nor tall")


def max_num(numm1, numm2, numm3):
    print ("numms")
    if numm1 >= numm2 and numm1 >= numm3:
        return numm1
    elif numm2 >= numm1 and numm2 >= numm3:
        return numm2
    else:
        return numm3


#print(max(1000, 20, 40))

# num_1 = input("Enter first number:")
# op=input("Enter operator: ")
# num_2 = input("Enter secound number:")
# if op == "+":
#    print(num_1+num_2)
# elif op == "-":
#    print(num_1-num_2)

month_conversions = {
    "Jan": "January",
    "Feb": "February",
}
#print(month_conversions.get("Jan"))

# i = 1
# while i <=10:
#   print(i)
#    i = i+1

# secret_word = "giraffe"
# guess = ""
# guess_count = 0
# guess_limit= 3
# out_of_guess= False

# while guess != secret_word and not(out_of_guess):
#    if guess_count <= guess_limit:
#        guess = input("Enter the words: ")
#        guess_count= guess_count+1
#    else:
#        out_of_guess = True
#
# if out_of_guess:
#    print ("you lost!")
# else:
#    print ("you win!")


#for s in "Giraffe":
#    print (s)

#print(pow(2, 3))


def raise_to_power(base_num, pow_num):
    result = 1
    for i in range(1, pow_num):
        result = result * base_num
    return result


#print (raise_to_power(2, 5))

#number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
#]
#print(number_grid[0][0])

#for row in number_grid:
#   for col in row:
 #       print(col)


#def translate(phrase):
#    translation = ""
#    for letter in phrase:
#        if letter in "AEIOUaeiou":
#            translation = translation + "g"
#        else:
#           translation = translation + letter
#    return translation

# print(translate(input("Enter the pharase:")))

# try:
#    value= 10/0
#    number= int(input("Enter a number: "))
#    print (number)
# except ZeroDivisionError:
#    print("Divided by zero")
# except ValueError:
#    print("invalid input")

file_1=open("ff_1.txt", "r")
#print(file_1.read())
#print(file_1.readline())
#print(file_1.readlines(1))
#for f in file_1.readlines():
#    print(f)
gg= file_1.readlines()
#print (gg[14][26:38])
s= float(gg[14][26:38])
print(s)
file_1.close()

file_2= open("ff_1.txt", "a")
file_2.write("Good Job! \n")
file_2.close()

student1 = Student("Jim", "b1", 3.1, False)
print(student1.name)

print (student1.on_honor_roll())



# fig = plt.figure()
# def f(x, y):
#     return np.sin(x) + np.cos(y)
#
# x = np.linspace(0, 2 * np.pi, 120)
# y = np.linspace(0, 2 * np.pi, 100).reshape(-1, 1)
# # ims is a list of lists, each row is a list of artists to draw in the
# # current frame; here we are just animating one artist, the image, in
# # each frame
# ims = []
# for i in range(60):
#     x += np.pi / 15.
#     y += np.pi / 20.
#     im = plt.imshow(f(x, y), animated=True)
#     ims.append([im])
#
# ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True,
#                                 repeat_delay=1000)
#ani.save('dynamic_images.mp4')
#plt.show()












