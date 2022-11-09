import tkinter #naimportujem si plátno
from random import * #naimportujem si knižnicu random
canvas=tkinter.Canvas(width=410,height=350) #určím si akú šírku, výšku a farbu pozadia bude mať plátno
canvas.pack() #vytvorím si plátno

def texthra(): #funkcia, ktorou vykresľujem padajúce slovo a body
    canvas.delete('all') #vymažem plátno
    global sx,sy #premenné sx,sy nastavím ako globálne
    global slova #premennú slova nastavím ako globálnu
    canvas.create_text(100, 10, text='Počet získaných bodov:') #vypíšem text
    canvas.create_text(200, 10, text=pocet_bodov) #vypíšem text
    canvas.create_text(sx,sy,text=slova,fill='red',font='Arial 15') #vypíšem text
    sy=sy+20 #premennú sy zväčšujem o 20
    if sy>370: #podmienka ak sy je väčšie ako 370
        sy=20 #premennú sy nastavím na 20
        slova=choice(('vypiť','vipiť','vysieť','visieť','lenka','Lenka')) #náhodne vyberám slovo
    if pocet_bodov==10: #podmienka ak pocet_bodov sa rovná 10
        canvas.create_text(100,175,text='Gratulujem vyhral si:',fill='red',font='Arial 15') #vypíšem text
        canvas.create_text(208,200,text=cenu,fill='red',font='Arial 15') #vypíšem text
    else:
        canvas.after(500, texthra) #volám funkciu texthra po 500 milisekundách
        
def body(event): #funkcia, ktorou zisťujem počet bodov
    global pocet_bodov #premenné pocet_bodov nastavím ako globálnu
    x=event.x
    y=event.y
    if slova=='vypiť' or slova=='visieť' or slova=='Lenka': #podmienka ak slovo je správne
        pocet_bodov=pocet_bodov + 1 #premennú pocet_bodov zväčšujem o 1  
    else:
        pocet_bodov=pocet_bodov - 2 #premennú pocet_bodov zmenšujem o 2
        
  

slova=choice(('vypiť','vipiť','vysieť','visieť','lenka','Lenka')) #náhodne vyberám slovo
cenu=choice(('nový telefón','lístky do divadla','knihu s názvom Harry Potter a kameň mudrcov')) #náhodne vyberám slovo
pocet_bodov = 0 #premennú pocet_bodov nastavím na 0
sx = 205 #premennú sx nastavím na 205
sy = 20 #premennú sy nastavím na 20
texthra() #volám funkcia texthra
canvas.bind('<Button-1>',body) #nabindujem funkciu body na kliknutie myšou
