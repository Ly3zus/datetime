from functions import *
import datetime


beolvas('Eredmenyek.txt')

print(f'2. feladat: A versenyt {len(versenyzok)} versenyző fejezte be.')

print(f'3. feladat: Versenyzők száma az "elit junior" kategóriában: {kateg_db("elit junior")}')
print(f'3. feladat: Versenyzők száma az "elit junior" kategóriában: {len(kateg_db2("elit junior"))}')

print(f'4. feladat: Átlagéletkor: {atlag_eletkor():.1f} év.')

