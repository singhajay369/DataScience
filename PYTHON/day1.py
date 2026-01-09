print("Hello")
# Module - python  files
# Package - directory with python files or folder with __init__.py file
# Script - file that can be executed directly
# keyword - reserved word in python that has special meaning
# Function - block of reusable code that performs a specific task
# Variable - a named location in memory to store data
# Class - a blueprint for creating objects that encapsulate data and behavioruv
# Object - an instance of a class that contains data and methods
# Method - a function defined within a class that operates on instances of that class
# Attribute - a variable that belongs to an object or class
# Exception - an error that occurs during program execution that can be handled
# Import - bringing in code from another module or package to use in the current script
# Decorator - a function that modifies the behavior of another function or method
# Loop - a control structure that repeats a block of code multiple times
# Conditional - a control structure that executes code based on a condition
# List - a collection of ordered items that can be changed
# Tuple - a collection of ordered items that cannot be changed
# Dictionary - a collection of key-value pairs that is unordered and changeable
# Set - a collection of unique items that is unordered and changeable
# String - a sequence of characters used to represent text
# Comprehension - a concise way to create lists, sets, or dictionaries using an expression
# Lambda - an anonymous function defined with the lambda keyword
# Generator - a special type of iterator that generates values on the fly
# Context Manager - a construct that allows for resource management, typically using the with statement
# Iterator - an object that allows iteration over a collection, implementing __iter__() and __next__() methods


my_name = "papa"
print(my_name)

a, x,y,z,  = "ajay", "harry", "rahul", "just now"
print(a)
print(x)    
print(y)
print(z)


b = 21
b

# learn about python exectuion pipeline .py-> tokenization -> parsing ->ast->compiler-> bytecode -> pvm(interpreter)-> out put

# uv is a package manager for python , cmd we use: uv python install version, uv venve command to create virtual environmentcd
# .ipynb is a jupyter notebook file, it is used for data science and machine learning projects it stands for interactive python notebook

balance = 1000

def add_money():
    global balance
    balance = balance + 500
    print("Balance after adding money:", balance)
    print(f"Inside Function: {balance}")
add_money()
print(f"Outside Function: {balance}")
