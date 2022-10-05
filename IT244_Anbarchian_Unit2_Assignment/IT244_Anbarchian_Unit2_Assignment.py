str1 = "Your color choices are red, blue, green, white or yellow."
print(str1)

str2 = "Enter a color from the list above: "
print(str2)

userColor = input()

userColor = userColor.lower()

validColor = True
if userColor == "red":
    spanishColor = "roja"
elif userColor == "blue":
    spanishColor = "azul"
elif userColor == "green":
    spanishColor = "verde"
elif userColor == "white":
    spanishColor = "blanco"
elif userColor == "yellow":
    spanishColor = "amarillo"
else:
    validColor = False

if validColor:
    print("The color", userColor, "in Spanish is " + spanishColor)
else:
    print("That is not a valid color for this program. Ese no es un color válido.")

