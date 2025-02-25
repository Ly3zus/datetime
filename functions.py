from data import *

def beolvas(faljnev:str)->None:
    f=open(faljnev,'r',encoding='utf8')
    for sor in f:
        versenyzok.append(Versenyzo(sor))
    f.close()
