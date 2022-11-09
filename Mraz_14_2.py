import tkinter #naimportujem si plátno
import random #naimportujem si knižnicu random
canvas=tkinter.Canvas() #určím si akú šírku, výšku a farbu pozadia bude mať plátno
canvas.pack() #vytvorím si plátno
canvas.create_rectangle(0,190,500,290,outline='',fill='blue') #vykreslím obdĺžnik

def balonalodka(suradnice): #funkcia, ktorou vykreslujem balón a loďku
    x=suradnice.x #do premennej x si uložím x-ovú súradnicu z kliknutia myši
    y=suradnice.y #do premennej y si uložím y-ovú súradnicu z kliknutia myši
    if y<150: #podmienka, ktorou kontrolujem kedy mám vykresliť balón
        canvas.create_oval(x,y,x+20,y+20)  #vykreslím kruh
        canvas.create_line(x,y+10,x+10,y+30) #vykreslím čiaru
        canvas.create_line(x+21,y+10,x+10,y+30) #vykreslím čiaru
        canvas.create_rectangle(x+5,y+30,x+15,y+40) #vykreslím štvorec
    if y>190: #podmienka, ktorou kontrolujem kedy mám vykresliť loďku
        canvas.create_line(x,y,x+40,y) #vykreslím čiaru
        canvas.create_line(x-5,y-10,x,y) #vykreslím čiaru
        canvas.create_line(x+45,y-10,x+40,y) #vykreslím čiaru
        canvas.create_line(x-5,y-10,x+45,y-10) #vykreslím čiaru
        canvas.create_line(x+20,y-10,x+20,y-30) #vykreslím čiaru
        canvas.create_line(x+20,y-30,x+40,y-20) #vykreslím čiaru
        canvas.create_line(x+40,y-20,x+20,y-15) #vykreslím čiaru
        
canvas.bind('<Button-1>',balonalodka) #nabindujem si funkciu balonalodka na kliknutie myšou