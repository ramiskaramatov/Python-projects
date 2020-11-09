import turtle

image = turtle.Turtle()
image.hideturtle()

image.speed(0)  # turtle motion
image.up()  # removes the lines  # pen control
image.shape("square")  # appearance
image.shapesize()  # standard size 20x20, if bigger use e.g. 50x50 # image.shapesize(50, 50)

screen = image.getscreen()  # Special Turtle methods
# screen.tracer(0)

height = 1600
width = 2000
screen.screensize(width, height)

x = -450
y = 300

img = [
    "0000000000000000000000000000000000000000000",
    "0000000000000000000000000000000000000000000",
    "000000000000ddddddddddddddddddd000000000000",
    "0000000000ddwssssssssssssssssssdd0000000000",
    "000000000dswwsssssssssssssssssssgd000000000",
    "000000000dswssgddgsssssssgddgsssgd000000000",
    "000000d0dssssgdlydgsssssgdlydgsssgd0d000000",
    "00000dlddswwsgdyydgsssssgdyydgsssgddld00000",
    "00000dlgdswwssgddgsssssssgddgssssgdgld00000",
    "00000dlgdsswsssssssssssssssssssssgdgld00000",
    "00000dlgdsssssssdddddddddddssssssgdgld00000",
    "00000dyddssssssdldldldldldldsssssgddyd00000",
    "000000d0dgsssssdydydydydydydsssssgd0d000000",
    "000000000dgsssssdddddddddddsssssgd000000000",
    "000000000dgggsssssssssssssssssgggd000000000",
    "0000000000ddgggggggggggggggggggdd0000000000",
    "000000000000ddddddddddddddddddd000000000000",
    "0000000000000000000dwsggd0000000000000000000",
    "00000000000000ddddddddddddddd00000000000000",
    "0000000d0dd0ddwwssgdwggdgssssdd0dd0d0000000",
    "000000dwdwgdswwssswgdddgwssssssdgwdwd000000",
    "00000ddgdgdswwssssswwwwwsssssssgdgdgdd00000",
    "0000dwdddddwwssssssssssssssssssgdddddwd0000",
    "0000ddd000dwwssssssssssssssssssgd000ddd0000",
    "000dwgd000dwwssssssssssssssssssgd000dgwd000",
    "000dsgd000dwwssssssssssssssssssgd000dgsd000",
    "0000dd0000dwwssssssssssssssssssgd0000dd0000",
    "000dwgd000dwwssssssssssssssssssgd000dgwd000",
    "0000dd0000dwwsssssssssssssssssggd0000dd0000",
    "00ddwgdd00dgggggggggggggggggggggd00ddgwdd00",
    "0dwsggggd00ddddddddddddddddddddd00dggggswd0",
    "0dsddddgd0dwwssssssssssssssssssgd0dgddddsd0",
    "0dgd00dgd0dwwsssssssssssssssssggd0dgd00dgd0",
    "00d0000d00dgggggggggggggggggggggd00d0000d00",
    "00000000000ddddddddddddddddddddd00000000000",
    "000000000000dwd0000000000000dwd000000000000",
    "000000000000dgd0000000000000dgd000000000000",
    "000000000000dgd0000000000000dgd000000000000",
    "00000000000dddd0000000000000dddd00000000000",
    "0000000000dwggd0000000000000dggwd0000000000",
    "000000000dwwgggd00000000000dgggwwd000000000",
    "000000000dwggggd00000000000dggggwd000000000",
    "000000000ddddddd00000000000ddddddd000000000",
    "000000000dwggggd00000000000dggggwd000000000",
    "0gggggggggdddddgggggggggggggdddddggggggggg0",
    "0000000000000000000000000000000000000000000"]

# "000000000000ddddddddddddddddddd000000000000" are the symbols in each element

for i in range(len(img)):  # reads each element in the list
    for j in range(len(img[i])):  # reads each symbol in each string of elements
        if img[i][j] != "0":
            image.shape("square")
            if img[i][j] == "d":
                color = "dimgray"
            elif img[i][j] == "g":
                color = "darkgray"
            elif img[i][j] == "s":
                color = "silver"
            elif img[i][j] == "w":
                color = "grey"
            elif img[i][j] == "y":
                color = "yellow"
            elif img[i][j] == "l":
                color = "#FFFACD"

            # image.shape("triangle")  # turtle changes to triangle shape

            image.color(color)
            image.stamp()
            image.fd(20)
        else:
            image.fd(20)

    y -= 20
    image.goto(x, y)


# screen.tracer(1)

screen.mainloop()








