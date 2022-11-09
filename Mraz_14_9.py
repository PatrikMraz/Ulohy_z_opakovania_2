import tkinter #naimportujem si plátno
import random #naimportujem si knižnicu random
canvas=tkinter.Canvas(width=500,height=500) #určím si akú šírku, výšku a farbu pozadia bude mať plátno
canvas.pack() #vytvorím si plátno

def kvapka(): #funkcia, ktorou vykreslujem kvapkanie a misku a vodu v miske
    global x #premennú x nastavím ako globálnu
    global y #premennú y nastavím ako globálnu
    global z #premennú z nastavím ako globálnu
    global w #premennú w nastavím ako globálnu
    global c #premennú c nastavím ako globálnu
    global v #premennú v nastavím ako globálnu
    global pk #premennú pk nastavím ako globálnu
    canvas.delete('kvapka') #vymažem kvapku
    canvas.delete('cislo') #vymažem text
    canvas.create_oval(100,450,400,500) #vykreslím oval
    canvas.create_oval(100,420,400,470) #vykreslím oval
    canvas.create_line(100,444,100,478) #vykreslujem čiaru
    canvas.create_line(400,444,400,478) #vykreslujem čiaru
    canvas.create_oval(x,y,x-10,y+10,fill='blue',tag='kvapka') #vykreslujem kvapku
    canvas.create_text(100,24,text='Počet kvapiek:',tag='cislo') #vykreslujem text 
    canvas.create_text(150,25,text=pk,tag='cislo') #vykreslujem text
    if y<460: #podmienka ak y je menšie ako 460
        y=y+10 #premennú y zväčšujem o 10
    if y==460: #podmienka ak y sa rovná 460
        y=120 #premennú y nastavím na 120
        pk=pk+1 #premennú pk zväčšujem o 1
        canvas.create_oval(z,w,c,v,fill='blue') #vykresľujem mláčku
        if z>100: #podmienka ak z je väčšie ako 100
            z=z-10 #premennú z zmenšujem o 10
            c=c+10 #premennú c zväčšujem o 10
        if w>450: #podmienka ak w je väčšie ako 450
            w=w-10 #premennú w zmenšujem o 10
            v=v+10 #premennú v zväčšujem o 10
    if pokracovat==1: #podmienka ak pokracovat sa rovná 1
        canvas.after(100,kvapka) #volám funkciu kvapka po 100 milisekundách
    
def stop(suradnice): #funkcia, ktorou stopnem kvapkanie
    global pokracovat #premennú pokracovat nastavím ako globálnu
    if pokracovat==1: #podmienka ak pokracovat sa rovná 1
        pokracovat=0 #premennú pokracovat nastavím na 0
    else:
        pokracovat=1 #premennú pokracovat nastavím na 1
        kvapka() #volám funkciu kvapka
        
pk=0 #premennú pk nastavím na 0    
pokracovat=1 #premennú pokracovat nastavím na 1     
x=260 #premennú x nastavím na 260
y=120 #premennú y nastavím na 120
z=230 #premennú z nastavím na 230
w=470 #premennú w nastavím na 470
c=270 #premennú c nastavím na 270
v=480 #premennú v nastavím na 480
kvapka() #volám funkciu kvapka
canvas.bind_all('p',stop) #nabindujem si funkciu stop na stlačenie klávesy p
