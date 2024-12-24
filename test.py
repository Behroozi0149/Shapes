from turtle import *
import winsound
frequency1 = 10000
duration1 = 1000
frequency2 = 500 
duration2 = 1000  
speed(0)
winsound.Beep(frequency1, duration1)
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
winsound.Beep(frequency2, duration2)
done()