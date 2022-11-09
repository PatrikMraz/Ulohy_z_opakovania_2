from random import * #naimportujem si knižnicu random

def nahodna_veta(): #funkcia, ktorou poskladám vety a potom ich vypíšem do shellu
    cislo= randint(0,5) #náhodne si vyberám číslo a ukladám ho do premennej cislo
    kto = choice(('Kamarát','Spolužiak','Andrej','Roman','Miro','Jozef','Milan','Slavo','Mišo')) #náhodne si vyberám meno
    kto1 = choice(('Kamarát','Spolužiak','Andrej','Roman','Miro','Jozef','Milan','Slavo','Mišo')) #náhodne si vyberám meno
    kto2= choice(('Katarína','Silvia','Iveta','Helena','Mirka','Vika','Biba','Kika','Anka')) #náhodne si vyberám meno
    kto3= choice(('Katarína','Silvia','Iveta','Helena','Mirka','Vika','Biba','Kika','Anka')) #náhodne si vyberám meno
    corobil = choice(('videl','prezradil','povedal','napísal','zistil',
                    'nakreslil','vymyslel','vypočul','zahral')) #náhodne si vyberám čo robí
    corobil1= choice(('videl','prezradil','povedal','napísal','zistil',
                    'nakreslil','vymyslel','vypočul','zahral')) #náhodne si vyberám čo robí
    corobil2= choice(('videla','prezradila','povedala','napísala','zistila','nakreslila',
                      'vymyslela''vypočula','zahrala')) #náhodne si vyberám čo robí
    corobil3= choice(('videla','prezradila','povedala','napísala','zistila','nakreslila',
                      'vymyslela''vypočula','zahrala')) #náhodne si vyberám čo robí
    ake = choice(('veľké','malé','obrovské','drobné','smutné','veselé','mohutné','šokujúce','nezmyselné','neuveriteľné')) #náhodne si vyberám aká je daná vec
    ake1 = choice(('veľké','malé','obrovské','drobné','smutné','veselé','mohutné','šokujúce','nezmyselné','neuveriteľné')) #náhodne si vyberám aká je daná vec
    ake2 = choice(('veľké','malé','obrovské','drobné','smutné','veselé','mohutné','šokujúce','nezmyselné','neuveriteľné')) #náhodne si vyberám aká je daná vec
    ake3 = choice(('veľké','malé','obrovské','drobné','smutné','veselé','mohutné','šokujúce','nezmyselné','neuveriteľné')) #náhodne si vyberám aká je daná vec
    co = choice(('tajomstvo','prekvapenie','predsavzatie','klamstvo','blbosti')) #náhodne si vyberám čo
    co1 = choice(('tajomstvo','prekvapenie','predsavzatie','klamstvo','blbosti')) #náhodne si vyberám čo
    co2 = choice(('tajomstvo','prekvapenie','predsavzatie','klamstvo','blbosti')) #náhodne si vyberám čo
    co3 = choice(('tajomstvo','prekvapenie','predsavzatie','klamstvo','blbosti')) #náhodne si vyberám čo
    if cislo==0: #podmienka, ktorou zisťujem hodnotu premennej cislo
        spojene = kto +' '+corobil+' '+ake+' '+co+'.' #do premennej spojene si uložím vetu ktorú poskladám zo slov
    elif cislo==2: #podmienka, ktorou zisťujem hodnotu premennej cislo   
        spojene = kto2 +' '+corobil2+' '+ake2+' '+co2+'.' #do premennej spojene si uložím vetu ktorú poskladám zo slov
    elif cislo==3: #podmienka, ktorou zisťujem hodnotu premennej cislo
        spojene = kto +' '+corobil+' '+ake+' '+co+' '+'a'+' '+kto1 +' '+corobil1+' '+ake1+' '+co1+'.' #do premennej spojene si uložím vetu ktorú poskladám zo slov
    elif cislo==4: #podmienka, ktorou zisťujem hodnotu premennej cislo
        spojene = kto2 +' '+corobil2+' '+ake2+' '+co2+' '+'a'+' '+kto3 +' '+corobil3+' '+ake3+' '+co3+'.' #do premennej spojene si uložím vetu ktorú poskladám zo slov
    else:
        spojene = kto +' '+corobil+' '+ake+' '+co+' '+'a'+' '+kto3 +' '+corobil3+' '+ake3+' '+co3+'.'
    print(spojene) #vypíšem vetu do shellu
    
    
    
for i in range(1,21): #for cyklus na vypisovanie viet
    nahodna_veta() #volám funkciu nahodna_veta()