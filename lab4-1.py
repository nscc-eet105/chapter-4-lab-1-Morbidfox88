#Chad Collard
#Lab 4-1
#6/25/2025

def ctof(celsius):
    fahrenheit = (celsius * 9/5) + 32 
    print(f'{fahrenheit:.2f}')

def ftoc(fahrenheit):
    celsius = (fahrenheit -32) * 5/9
    return(celsius)


temp = float(input("enter the temp "))
type_of_temp = input("fahrenheit or celsius ")


if type_of_temp == "c":
    ctof(temp)

elif type_of_temp == "f":
    celsius = ftoc(temp)
    print(f'{celsius:.2f}')












