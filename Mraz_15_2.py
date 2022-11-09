from random import * #naimportujem si knižnicu random

def nahodna_veta(): #funkcia, ktorou poskladám vety a potom ich vypíšem do shellu
    cislo= randint(0,1) #náhodne si vyberám číslo a ukladám ho do premennej cislo
    kto = choice(('Kamarát','Spolužiak','Andrej','Roman','Miro','Jozef','Milan','Slavo','Mišo')) #náhodne si vyberám meno
    kto1 = choice(('Kamarát','Spolužiak','Andrej','Roman','Miro','Jozef','Milan','Slavo','Mišo')) #náhodne si vyberám meno
    corobil = choice(('videl','prezradil','povedal','napísal','zistil',
                    'nakreslil','vymyslel','vypočul','zahral')) #náhodne si vyberám čo robí
    corobil1= choice(('videl','prezradil','povedal','napísal','zistil',
                    'nakreslil','vymyslel','vypočul','zahral')) #náhodne si vyberám čo robí
    ake = choice(('veľké','malé','obrovské','drobné','smutné','veselé','mohutné','šokujúce','nezmyselné','neuveriteľné')) #náhodne si vyberám aká je daná vec
    ake1 = choice(('veľké','malé','obrovské','drobné','smutné','veselé','mohutné','šokujúce','nezmyselné','neuveriteľné')) #náhodne si vyberám aká je daná vec
    co = choice(('tajomstvo','prekvapenie','predsavzatie','klamstvo','blbosti')) #náhodne si vyberám čo
    co1 = choice(('tajomstvo','prekvapenie','predsavzatie','klamstvo','blbosti')) #náhodne si vyberám čo
    if cislo==0: #podmienka, ktorou zisťujem hodnotu premennej cislo
        spojene = kto +' '+corobil+' '+ake+' '+co+'.' #do premennej spojene si uložím vetu ktorú poskladám zo slov
    else:
        spojene = kto +' '+corobil+' '+ake+' '+co+' '+'a'+' '+kto1 +' '+corobil1+' '+ake1+' '+co1+'.' #do premennej spojene si uložím vetu ktorú poskladám zo slov
    print(spojene) #vypíšem vetu do shellu
    
for i in range(1,21): #for cyklus na vypisovanie viet
    nahodna_veta() #volám funkciu nahodna_veta()
