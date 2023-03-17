# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
major ='MSc Business Statistics'
tacos_Rating = 7
sleep_Rating = 8

first_name = input('Please enter your first name: ')
last_name = input('Please enter your last name: ')
full_name = first_name +' '+ last_name
print(full_name)

print(type(major))
print(type(tacos_Rating))
print(type(sleep_Rating))
print(type(first_name))
print(type(last_name))
print(type(full_name))

average = (tacos_Rating+sleep_Rating)/2
print(average)
percentage = average*10

print(f'My name is {first_name} and is give tacos a score of {tacos_Rating} out of 10!')
print(f'I am {full_name} and my sleeping enjoyment rating is {sleep_Rating} / 10!')
print(f'Based on the factors above, my happiness rating is {average} out of 10, or {percentage}%!')