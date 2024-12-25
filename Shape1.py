from turtle import *
import winsound
frequency = 500 
duration = 1000  
speed(0)
winsound.Beep(frequency, duration)
bg=str(input('Enter a Background color:'))
cr=str(input('Enter a color:'))
bgcolor(bg)
color(cr)
for i  in range(160):
    rt(i)
    circle(150,i)
    fd(i)
    rt(90)
    hideturtle()
done()
winsound.Beep(frequency, duration)