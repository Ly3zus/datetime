from datetime import datetime

class Versenyzo:
    def __init__(self,sor:str):
        adatok=sor.strip().split(';')
        self.nev=adatok[0]
        self.szuletesi_ev=int(adatok[1])
        self.rajtszam=int(adatok[2])
        self.neme=adatok[3]
        self.kategoria=adatok[4]
        self.uszas=adatok[5]
        self.elso_depo=adatok[6]
        self.kerekpar=adatok[7]
        self.masodik_depo=adatok[8]
        self.futas=adatok[9]
        self.osszido=self.idoatalkit(self.uszas)+self.idoatalkit(self.elso_depo)+self.idoatalkit(self.kerekpar)+self.idoatalkit(self.masodik_depo)+self.idoatalkit(self.futas)

    def idoatalkit(self,ido:str)->int:
        ido_adatok=ido.split(':')
        return int(ido_adatok[0])*3600+int(ido_adatok[1])*60+int(ido_adatok[2])

versenyzok:list[Versenyzo]=[]



