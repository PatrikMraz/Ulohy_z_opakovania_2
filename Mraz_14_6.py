import tkinter #naimportujem si plátno
from random import * #naimportujem si knižnicu random
canvas = tkinter.Canvas(height=270,width=400) #určím si akú šírku, výšku a farbu pozadia bude mať plátno
canvas.pack() #vytvorím si plátno

sirka=430 #premennú sirka si nastavím na 430
def posuvaj(): #funkcia, ktorou vykreslujem posuvný text
    global x #premennú x nastavím ako globálnu
    canvas.delete('all') #vymažem obsah plátna
    canvas.create_text(x,y,text=entry1.get(),fill='blue',tags='text') #vykreslujem text
    x=x-15 #premennú x zmenšujem o 15
    canvas.move('text',5,0) #posúvam text o 5 do ľava
    if x<0-30: #podmienka, ktorou zisťujem či je text za ľavým okrajom
        x=x+sirka+30 #premennú x zväčším o x,sirku a 30
        canvas.move('text',sirka+15,0) #posuniem text za okraj
    canvas.after(1000,posuvaj) #volám funkciu posuvaj po 1 sekunde
    
entry1 = tkinter.Entry() #pripravím si vstup
entry1.pack() #vytvorím si vstup

x=380 #premennú x nastavím na 380
y=250 #premennú y nastavím na 250

posuvaj() #volám funkciu posuvaj