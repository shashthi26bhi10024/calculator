#this module will handle percentage, square, squareroot , power
import math 

def percentage(number,percent):
    return (number*percent)/100

def square(number):
    return number**2

def square_root(number):
    if number <0:
        return "error: cannot find square root of a negative number "
    return math.sqrt(number)

def power(number,exponent):
    return number**exponent