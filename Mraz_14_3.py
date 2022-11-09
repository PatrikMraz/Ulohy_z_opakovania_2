import tkinter #naimportujem si plátno
from random import * #naimportujem si knižnicu random
canvas = tkinter.Canvas() #určím si akú šírku, výšku a farbu pozadia bude mať plátno
canvas.pack() #vytvorím si plátno

def kocky(): #funkcia, ktorou vykreslujem kocky
    canvas.delete('all') #vymažem obsah z plátna
    global cislo #premennú cislo nastavím ako globálnu
    global cislo1 #premennú cislo1 nastavím ako globálnu
    canvas.create_text(100, 10, text='Počet získaných bodov:') #vypisujem text
    canvas.create_text(200, 10, text=pocet_bodov) #vypisujem text
    cislo=choice(('1','2','3','4','5','6')) #náhodne si vyberám číslo do premennej cislo
    cislo1=choice(('1','2','3','4','5','6')) #náhodne si vyberám číslo do premennej cislo1
    canvas.create_rectangle(100,70,150,120,fill='red') #vykreslujem štvorec
    canvas.create_rectangle(230,70,280,120,fill='red') #vykreslujem štvorec
    canvas.create_text(255,95,text=cislo,fill='white',font='Arial 20') #vypisujem text
    canvas.create_text(125,95,text=cislo1,fill='white',font='Arial 20') #vypisujem text
    canvas.after(1000, kocky) #volám funkciu kocky po 1 sekunde
    
def porovnaj(): #funkcia, ktorou zisťujem počet získaných bodov
    global pocet_bodov #premennú pocet_bodov nastavím ako globálnu
    if cislo==cislo1: #podmienka, ktorou kontrolujem či sú čísla na kockách rovnaké
        pocet_bodov = pocet_bodov + 2 #premennú pocet_bodov zväčšujem o 2
    else: 
        pocet_bodov = pocet_bodov - 1 #premennú pocet_bodov zmenšujem o 1
        
button1 = tkinter.Button(text='Rovnaké', command=porovnaj) #nastavím si aké vlastnosti bude mať tlačítko
button1.pack() #vytvorím tlačítko

pocet_bodov = 0 #premennú pocet_bodov nastavím na 0
kocky() #volám funkciu kocky
