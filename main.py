from functions import *
import datetime


beolvas('Eredmenyek.txt')

print(f'2. feladat: A versenyt {len(versenyzok)} versenyző fejezte be.')

print(f'3. feladat: Versenyzők száma az "elit junior" kategóriában: {kateg_db("elit junior")}')
print(f'3. feladat: Versenyzők száma az "elit junior" kategóriában: {len(kateg_db2("elit junior"))}')

print(f'4. feladat: Átlagéletkor: {atlag_eletkor():.1f} év.')

bekert_kategoria=input('5. feladat: Kérek egy kategóriát: ')

rajtszam_lista=kateg_db2(bekert_kategoria)

if len(rajtszam_lista)==0:
    print('\tRajtszám(ok): Nincs ilyen kategória!')
else:
    print('\tRajtszám(ok): ', end='')
    print(*rajtszam_lista,sep=' ')


print(f'\n6. feladat: A legjobb időt {gyoztes("n").nev} érte el.')