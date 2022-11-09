import tkinter #naimportujem si plátno
from random import * #naimportujem si knižnicu random
canvas=tkinter.Canvas() #určím si akú šírku, výšku a farbu pozadia bude mať plátno
canvas.pack() #vytvorím si plátno

def semafor(): #funkcia semafor, ktorou vykreslujem semafor
    farba=randint(0,100) #premennú farba vyberám náhodne
    canvas.create_rectangle(175,50,215,167,fill='black') #vykreslím obdĺžnik
    if 0<=farba<=20: #podmienka, ktorou zisťujem aké farby svietia
        canvas.create_oval(175,50,215,89,fill='red') #vykreslím kruh
        canvas.create_oval(175,89,215,128,fill='yellow') #vykreslím kruh
    if 20<=farba<=40: #podmienka, ktorou zisťujem aké farby svietia
        canvas.create_oval(175,128,215,167,fill='lime') #vykreslím kruh
    if 40<=farba<=60: #podmienka, ktorou zisťujem aké farby svietia
        canvas.create_oval(175,50,215,89,fill='red') #vykreslím kruh
        canvas.create_oval(175,89,215,128,fill='yellow') #vykreslím kruh
        canvas.create_oval(175,128,215,167,fill='lime') #vykreslím kruh
    if 60<=farba<=80: #podmienka, ktorou zisťujem aké farby svietia
        canvas.create_oval(175,89,215,128,fill='yellow') #vykreslím kruh
    if 80<=farba<=100: #podmienka, ktorou zisťujem aké farby svietia
        canvas.create_oval(175,50,215,89,fill='red') #vykreslím kruh
    canvas.after(1000,semafor) #volám funkciu semafor po 1 sekunde
semafor() #volám funkciu semafor  