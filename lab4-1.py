#Chad Collard
#Lab 4-1
#6/25/2025

def ctof(celsius):
    fahrenheit = (celsius * 9/5) + 32 
    print(f"The current temperature is {celsius:.2f} celsius this temperature in fahrenheit is {fahrenheit:.2f} ")

def ftoc(fahrenheit):
    celsius = (fahrenheit -32) * 5/9
    return(celsius)


temp = float(input("What is the current temperature? "))

while True:
    type_of_temp = input("Did you enter the temperature in (c)elsius of (f)ahrenheit? ")
    if type_of_temp == "c":
        ctof(temp)
        break

    elif type_of_temp == "f":
        celsius = ftoc(temp)
        print(f"The current temperature is {temp:.2f} fahrenheit this temperature in celsius is {celsius:.2f} ")
        break
    else:
        print('invalid input, please try again!')
        continue










