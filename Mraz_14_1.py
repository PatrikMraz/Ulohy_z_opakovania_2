import tkinter #naimportujem si plátno
canvas=tkinter.Canvas(width=700,height=700) #určím si akú šírku, výšku a farbu pozadia bude mať plátno
canvas.pack() #vytvorím si plátno

def ziak(suradnice): #funcia, ktorá vykreslí žiaka
    x=suradnice.x #do premennej x si uložím x-ovú súradnicu z kliknutia myši
    y=suradnice.y #do premennej y si uložím y-ovú súradnicu z kliknutia myši
    canvas.create_oval(x,y,x+60,y+60) #vykreslím kruh
    canvas.create_rectangle(x-5,y+60,x+65,y+120) #vykreslím obdĺžnik
    canvas.create_text(x+30,y+135,text=entry1.get(),font='Arial 20') #vypíšem meno žiaka
    
entry1=tkinter.Entry() #pripravím si vstup
entry1.pack() #vytvorím si vstup
canvas.bind('<Button-1>',ziak) #nabindujem si funkciu ziak na kliknutie myšou