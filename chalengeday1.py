
from colorama import Fore, Back
#JOCK

line = "Whats the easy peasy coding language"
jock = (f" HI the jock is 'PYTHON is easy!!'")
print(line)
line1 = input(" press enter to see jock ")
print(Fore.BLUE + Back.LIGHTGREEN_EX + jock)

#NAME

name = input(f"What is your name")
message = (f"Hello {name}")
print( Fore.MAGENTA + message)

#AREA AND VOLUMNE
def shape(height, length, width):
    area = height * length
    volume = height * length * width
    print(Fore.CYAN + f"The Area is {area} m2")
    print(Fore.MAGENTA + f"The Volume is {volume} m3")

shape(2,4,2)


