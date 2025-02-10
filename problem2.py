''' 
Problem - Convert temperatures (Celsius, Fahrenheit, Kelvin) based on user input
and show error messages based on user input.

Clues - Need to use user input, if statement, and while statements and may try
and except and break for error.

Steps

Ask the user for scale to convert from.
   check error
Ask the user for the scale to convert to.
   check error
Ask for temp with if statement.
   check error and try and except and break used when converting to int

Convert in if statement and then print it out(turn the user input into what it really means
with if statement first).

Note* I accept it if it is not captilized and if the current and convert is the same,
I print the same thing.
'''

#Asking for the current scale until they choose a correct one.
current = input("Which scale are you converting from? (C/F/K) ")
current = current.lower()

while current != "c" and current != "f" and current != "k":
    current = input("Incorrect! Please type C, F, or K. ")
    current = current.lower()

#Asking for convert scale until they choose a correct one.
convert = input("Which scale are you converting to? (C/F/K) ")
convert = convert.lower()

while convert != "c" and convert != "f" and convert != "k":
    convert = input("Incorrect! Please type C, F, or K. ")
    convert = convert.lower()

#Asking for temp until it is actually a number.
temp = 0
if current == "c":
    temp = input("Enter the temperature in Celsius: ")
elif current == "f":
    temp = input("Enter the temperature in Fahrenheit: ")
else:
    temp = input("Enter the temperature in Kelvin: ")

while True:
    try:
        temp = int(temp)
        break
    except ValueError:
        temp = input("Please enter a number. ")

#Converting
result = 0
if current == "c" and convert == "f":
    result = (temp * 9/5) + 32
elif current == "c" and convert == "k":
    result = temp + 273.15
elif current == "f" and convert == "c":
    result = (temp - 32) * 5/9
elif current == "f" and convert == "k":
    result = (temp - 32) * 5/9 + 273.15
elif current == "k" and convert == "c":
    result = temp - 273.15
elif current == "k" and convert == "f":
    result = (temp - 273.15) * 9/5 + 32
else:
    result = temp

#Expand what it means.
if current == "c":
    current = "Celsius"
elif current == "k":
    current = "Kelvin"
else:
    current = "Fahrenheit"

if convert == "c":
    convert = "Celsius"
elif convert == "k":
    convert = "Kelvin"
else:
    convert = "Fahrenheit"

print(f"{temp}° {current} is {result}° {convert}.")