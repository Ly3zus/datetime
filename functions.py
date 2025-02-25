from data import *

def beolvas(faljnev:str)->None:
    f=open(faljnev,'r',encoding='utf8')
    for sor in f:
        versenyzok.append(Versenyzo(sor))
    f.close()

def kateg_db(kategoria:str)->int:
    db=0
    for v in versenyzok:
        if v.kategoria==kategoria:
            db+=1
    return db

def kateg_db2(kategoria:str)->list:
    rajtszam_lista:list[int]=[]
    for v in versenyzok:
        if v.kategoria==kategoria:
            rajtszam_lista.append(v.rajtszam)
    return rajtszam_lista

def atlag_eletkor()->float:
    osszeg=0
    for v in versenyzok:
        osszeg+=2014-v.szuletesi_ev
    return osszeg/len(versenyzok)
