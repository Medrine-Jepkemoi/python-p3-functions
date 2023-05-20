#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

greet_programmer()

def greet(name):
    print(f"Hello, {name}!")

greet("Medrine")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

greet_with_default("John Doe")

def add(num1, num2):
    answer = num1 + num2
    return answer

print(add(3, 4))    

def halve(number):
    half = number / 2
    return half

print(halve(5))
