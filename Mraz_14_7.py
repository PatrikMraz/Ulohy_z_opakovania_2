import tkinter #naimportujem si plátno
import random #naimportujem si knižnicu random
canvas=tkinter.Canvas(bg='white') #určím si akú šírku, výšku a farbu pozadia bude mať plátno
canvas.pack() #vytvorím si plátno

kery_k=random.choice((1,2,3,4)) #náhodne si vyberiem správny káblik
pokracovat=1 #premennú pokracovat nastavím na 1
čas=60 #premennú čas nastavím na 60

def casovac(): #funkcia, ktorou vykreslujem časovač
    canvas.delete('cas') #vymažem čas
    global čas #premennú čas nastavím ako globálnu
    global pokracovat #premennú pokracovat nastavím ako globálnu
    canvas.create_text(200,125,text=čas,fill='green',font='Arial 220 bold',tag='cas') #vypíšem čas
    if čas > -1: #podmienka, ktorou kontrolujem hodnotu premennej čas
         čas = čas - 1 #premennú čas zmenšujem o 1
         if čas == -1: #podmienka ak čas sa rovná 1
             čas = 0 #premennú čas nastavím na 0
             canvas.delete('cas') #vymažem čas
             canvas.create_text(200,100,text='Bomba vybuchla', font='Arial 30 bold',fill='green') #vypíšem text
    if pokracovat == 1: #podmienka ak pokracovat sa rovná 1
       canvas.after(100,casovac) #volám funkciu casovac po 1 milisekunde

def bomba(kabel): #funkcia, ktorou zneškodňujem bombu
    global kery_k #premennú kery_k nastavím ako globálnu
    if kabel==kery_k: #podmienka ak kabel sa rovná kery_k
        stop() #volám funkciu stop
        canvas.create_text(200,250,text='Zneškodnil si bombu',font='Helvetica 10',fill='red') #vypíšem text
    if kabel!=kery_k: #podmienka ak kabel sa nerovná kery_k
        stop() #volám funkciu stop
        canvas.create_text(200,250,text='Bomba vybuchla',font='Helvetica 10',fill='red') #vypíšem text

def stop(): #funkcia, ktorou ovládam časovač
    global pokracovat #premennú pokracovat nastavím ako globálnu
    if pokracovat == 1: #podmienka ak pokracovat sa rovná 1
        pokracovat = 0 #premennú pokracovat nastavím na 0
    else:
        pokracovat = 1 #premennú pokracovat nastavím na 1
        casovac() #volám funkciu časovač
    

def modry(): #funkcia, ktorou určím kábel, ktorý som prestrihol a zavolám funkciu bomba
    kabel=1 #premennú kabel nastavím na 1
    bomba(kabel) #volám funkciu bomba s parametrom kabel
    
def cerveny(): #funkcia, ktorou určím kábel, ktorý som prestrihol a zavolám funkciu bomba
    kabel=2 #premennú kabel nastavím na 2
    bomba(kabel) #volám funkciu bomba s parametrom kabel

def zlty(): #funkcia, ktorou určím kábel, ktorý som prestrihol a zavolám funkciu bomba
    kabel=3 #premennú kabel nastavím na 3
    bomba(kabel) #volám funkciu bomba s parametrom kabel
    
def zeleny(): #funkcia, ktorou určím kábel, ktorý som prestrihol a zavolám funkciu bomba
    kabel=4 #premennú kabel nastavím na 4
    bomba(kabel) #volám funkciu bomba s parametrom kabel
     
casovac() #volám funkciu casovac
button1 = tkinter.Button(text='Modrý kábel',command=modry) #pripravím si tlačítko
button1.pack() #vytvorím tlačítko

button2 = tkinter.Button(text='červený kábel',command=cerveny) #pripravím si tlačítko
button2.pack() #vytvorím tlačítko

button3 = tkinter.Button(text='žltý kábel',command=zlty) #pripravím si tlačítko
button3.pack() #vytvorím tlačítko

button4 = tkinter.Button(text='zelený kábel',command=zeleny) #pripravím si tlačítko 
button4.pack() #vytvorím tlačítko