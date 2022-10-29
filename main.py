import PySimpleGUI as sg

sg.Window(title="dimensions", layout=[[]], margins=(100, 50)).read()


dimensions = ["Chocolate Dimension",
              "Double Dimension", "Black Hole Dimension"]

print("Hello, and welcome to the dimension travel hub.")
print("Here is the list of dimensions available: \n")
print(dimensions[0])
print(dimensions[1])
print(dimensions[2])
print(" ")

dimension = input("What dimension would you like to travel to? ")

if dimension == "Chocolate Dimension":
    print("great, you must love chocolate")
elif dimension == "Double Dimension":
    print("You really like doubling it huh?")
else:
    print("Max amount to stay in this dimension is 10 days!\n")

days_staying = input(
    "How many days will you be staying in the " + str(dimension) + "? ")
if int(days_staying) > 10:
    print("You cannot stay more than 10 days")
else:
    print("Great, hope you enjoy your stay")
