import random
import time
import tkinter
canvasWidth = 1440
canvasHeight = 720
screen = tkinter.Tk()
screen.title('Bus game')
screen.geometry('1440x720')
canvas = tkinter.Canvas(screen, width=canvasWidth, height=canvasHeight)
canvas.pack()
background = tkinter.PhotoImage(file='REF/bus/groundOG.png')
canvas.create_image(canvasWidth/2, canvasHeight/2, image=background)
lines = tkinter.PhotoImage(file='REF/bus/linesOG.png')
canvas.create_image(canvasWidth/2, canvasHeight/2, image=lines)
bus = tkinter.PhotoImage(file='REF/bus/busOG.png')
canvas.create_image(canvasWidth/2, canvasHeight/2, image=bus)
openedWindow = True
score = 0
def main_loop():
    while openedWindow == True:
        move_bus()
        screen.update()
        time.sleep(1)
        if openedWindow == True:
            gameOver
leftKey = 0
rightKey = 0
def when_key_pressed(event):
    global leftKey, rightKey
    if event.keysym == "Left":
        leftKey = 1
    elif event.keysym == "Right":
        rightKey = 1
def when_key_unpressed(event):
    global leftKey, rightKey
    if event.keysym == "Left":
        leftKey = 0
    elif event.keysym == "Right":
        rightKey = 0
speedBus = 6
def move_bus():
    mouvBus = speedBus*rightKey - speedBus*leftKey
    (busLeft, OverBus, busRight, UnderBus) = canvas.coords(bus)
    if ((busLeft > 0 or mouvBus > 0) and (busRight < canvasWidth
    or mouvBus < 0)):
        canvas.move(bus, mouvBus, 0)
mouvLines = 4
mouvBackground = 4
defOverBus = canvasHeight
defUnderBus = canvasHeight
def move_ground():
    global mouvLines, mouvBalleY, score, speedBus
    (groundLeft, overGround, underGround, groundRight) = canvas.coords(lines, background)
    if mouvLines > 0 and busRight > canvasWidth:
        mouvLines = -mouvLines
    if mouvLines < 0 and busLeft < 0:
        mouvBackground = -mouvLines
    if mouvBackground < 0 and OverBus < 0:
        mouvBackground = -mouvBackground
    if mouvBackground > 0 and underBus > defOverBus and basBalle < defUnderBus:
        (busLeft, OverBus, busRight, UnderBus) = canvas.coords(bus)
        if (mouvLines > 0 and (busRight+mouvLines > gaucheRaquette
        and busLeft < busRight) or mouvLines < 0
        and (busRight > busLeft and busLeft+mouvLines < busRight)):
            mouvBalleY = -mouvBalleY
            score = score + 1
            canvas.move(bus, mouvLines, mouvBackground)
def gameOver():
    bus_anim = 660
    if bus_anim == 1000:
        openedWindow == False
        screen.destroy()
    elif bus_anim == 420:
        openedWindow == False
        screen.destroy()
def score(event):
    global score
    global leftKey, rightKey
    score = score + 1
    if score == 1:
        print("1 m")
    elif score == 2:
        print("2 m")
    else:
        print(score, "m")
def close():
    global openedWindow
    openedWindow = False
    screen.destroy()
screen.protocol("WM_DELETE_WINDOW", close)
screen.bind("<KeyPress>", when_key_pressed)
screen.bind("<KeyRelease>", when_key_unpressed)
main_loop()
