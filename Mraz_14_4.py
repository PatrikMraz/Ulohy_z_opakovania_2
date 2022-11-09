import tkinter #naimportujem si plátno
import random #naimportujem si knižnicu random
canvas = tkinter.Canvas(height=270,width=400) #určím si akú šírku, výšku a farbu pozadia bude mať plátno
canvas.pack() #vytvorím si plátno

def posuvaj(): #funkcia, ktorou vykreslujem otáčavý text
    global x #premennú x nastavím ako globálnu
    global y #premennú y nastavím ako globálnu
    global a #premennú a nastavím ako globálnu
    x=random.randrange(400) #premennú x vyberám náhodne
    y=random.randrange(270) #premennú y vyberám náhodne
    farba=random.choice(('blue','red','yellow','green','purple','brown','pink','orange')) #náhodne vyberám farbu
    canvas.delete('all') #zmažem obsah plátna
    canvas.create_text(x,y,text=entry1.get(),fill=farba,font='Arial 12 bold',angle=a) #vykreslujem text
    a=a+5 #premennú a zväčšujem o 5
    if a==95: #podmienka ak a sa rovná 95
        a=10 #premennú a nastavím na 10
    canvas.after(1000,posuvaj) #volám funkciu posuvaj po 1 sekunde
    
    
def zmaz(event): #funkcia, ktorou vymazávam obsah plátna
    canvas.delete('all') #vymažem obsah plátna

entry1 = tkinter.Entry() #pripravím si vstup
entry1.pack() #vytvorím si vstup
a=10 #premennú a nastavím na 10

canvas.bind('<Button-1>',zmaz) #nabindujem si funkciu zmaz na kliknutie myšou
posuvaj() #volám funkciu posuvaj