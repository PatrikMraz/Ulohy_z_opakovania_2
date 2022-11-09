import tkinter #naimportujem si plátno
import random #naimportujem si knižnicu random
canvas=tkinter.Canvas(height=300) #určím si akú šírku, výšku a farbu pozadia bude mať plátno
canvas.pack() #vytvorím si plátno

def bosorka(): #funkcia, ktorou vykreslujem bosorky
    global x #premennú x nastavím ako globálnu
    global y #premennú y nastavím ako globálnu
    global x1 #premennú x1 nastavím ako globálnu
    global y1 #premennú y1 nastavím ako globálnu
    b=random.randrange(0,10) #náhodne si vyberám posun
    c=random.randrange(0,10) #náhodne si vyberám posun
    canvas.delete('bos') #vymazávam bosorky
    canvas.create_oval(x,y,x+10,y+9,tag='bos') #vykreslujem kruh
    canvas.create_rectangle(x,y+10,x+10,y+30,tag='bos') #vykreslujem obdĺžnik
    canvas.create_line(x-20,y+20,x+20,y+20,tag='bos') #vykreslujem čiaru
    canvas.create_line(x-40,y-10,x-20,y+20,tag='bos') #vykreslujem čiaru
    canvas.create_line(x-40,y,x-20,y+20,tag='bos') #vykreslujem čiaru
    canvas.create_line(x-40,y+10,x-20,y+20,tag='bos') #vykreslujem čiaru
    canvas.create_line(x-40,y+15,x-20,y+20,tag='bos') #vykreslujem čiaru
    canvas.create_line(x-40,y+20,x-20,y+20,tag='bos') #vykreslujem čiaru
    canvas.create_line(x-40,y+25,x-20,y+20,tag='bos') #vykreslujem čiaru
    canvas.create_line(x-40,y+30,x-20,y+20,tag='bos') #vykreslujem čiaru
    canvas.create_line(x-40,y+40,x-20,y+20,tag='bos') #vykreslujem čiaru
    canvas.create_line(x-40,y+50,x-20,y+20,tag='bos') #vykreslujem čiaru
    canvas.create_oval(x1,y1,x1+10,y1+9,tag='bos') #vykreslujem kruh
    canvas.create_rectangle(x1,y1+10,x1+10,y1+30,tag='bos') #vykreslujem obdĺžnik
    canvas.create_line(x1-20,y1+20,x1+20,y1+20,tag='bos') #vykreslujem čiaru
    canvas.create_line(x1-40,y1-10,x1-20,y1+20,tag='bos') #vykreslujem čiaru
    canvas.create_line(x1-40,y1,x1-20,y1+20,tag='bos') #vykreslujem čiaru
    canvas.create_line(x1-40,y1+10,x1-20,y1+20,tag='bos') #vykreslujem čiaru
    canvas.create_line(x1-40,y1+15,x1-20,y1+20,tag='bos') #vykreslujem čiaru
    canvas.create_line(x1-40,y1+20,x1-20,y1+20,tag='bos') #vykreslujem čiaru
    canvas.create_line(x1-40,y1+25,x1-20,y1+20,tag='bos') #vykreslujem čiaru
    canvas.create_line(x1-40,y1+30,x1-20,y1+20,tag='bos') #vykreslujem čiaru
    canvas.create_line(x1-40,y1+40,x1-20,y1+20,tag='bos') #vykreslujem čiaru
    canvas.create_line(x1-40,y1+50,x1-20,y1+20,tag='bos') #vykreslujem čiaru
    if y<250: #podmienka ak y je menšie alebo rovné 250
        y=y+b #premennú y zväčšujem náhodne
        if 240<y<250: #podmienka ak y sa rovná 250
            prva=True #premennú prva nastavím na True
            hodnotenie(prva) #volám funkciu hodnotenie s daným parametrom
    if y1<250: #podmienka ak y je menšie alebo rovné 250
        y1=y1+c #premennú y1 zväčšujem náhodne
        if 240<y1<250: #podmienka ak y1 sa rovná 250
            druha=True #premennú druha nastavím na True
            hodnotenie2(druha) #volám funkciu hodnotenie2 s daným parametrom
    canvas.after(100,bosorka) #volám funkciu bosorka po 100 milisekundách

def hodnotenie(prva): #funkcia hodnotenie na zistenie prvej bosorky
    if prva==True: #podmienka ak premenná prva je True
        canvas.create_text(120,25,text='Prva bola bosorka vlavo a druha vpravo') #vypíšem text
    
def hodnotenie2(druha): #funkcia hodnotenie na zistenie prvej bosorky
    if druha==True: #podmienka ak premenná druha je True
        canvas.create_text(120,25,text='Prva bola bosorka vpravo a druha vlavo') #vypíšem text  

x=80 #premennú x nastavím na 80   
y=40 #premennú y nastavím na 40
x1=220 #premennú x1 nastavím na 220
y1=40 #premennú y1 nastavím na 40
bosorka() #volám funkciu bosorka

