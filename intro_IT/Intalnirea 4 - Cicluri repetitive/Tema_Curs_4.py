'''
1.Având lista:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat',
'Trabant', 'Opel']
Folosește un for că să iterezi prin toată lista și să afișezi;
● ‘Mașina mea preferată este x’.
● Fă același lucru cu un for each.
● Fă același lucru cu un while.

'''
#-----------FOR---------
print(('---------------'))

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

for i in range(len(masini)):
     if masini[i]=='BMW':
          print(f'Mașina mea preferată este {masini[i]}!')

print(('---------------'))
#-----------FOR-EACH--------

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
for masina_preferata in list(masini):
    if masina_preferata == 'BMW':
         print(f'Mașina mea preferată este {masina_preferata}!')

print(('---------------'))
#-----------WHILE---------

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

i = 0
while i < len(masini):
     if masini[i] == 'BMW':
          print(f'Mașina mea preferată este {masini[i]}!')
     i += 1


'''
2. Aceeași listă:
Folosește un for else
În for

- Modifică elementele din listă astfel încât să fie scrie cu majuscule,
exceptând primul și ultimul.
În else:
- Printează lista.

'''
print(('---------------'))

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
for i in range(1 , len(masini)-1):
    masini[i] = masini[i].upper()
    #print(masini[i])
else:
     print(masini)

'''
3. Aceeași listă:
Vine un cumpărător care dorește să cumpere un Mercedes.
Itereaza prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes:
Printează ‘am găsit mașina dorită de dvs’
Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel:
Printează ‘Am găsit mașina X. Mai căutam‘
'''
print(('---------------'))
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

for i in range(len(masini)):
     if masini[i] == 'Mercedes':
          print(f'Am gasit masina dorita de dvs : {masini[i]}!')
          continue

     else :
          print(f'Am găsit mașina {masini[i]}. Mai căutam')


print(('---------------'))
'''
4. Aceași listă;
Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
excepția Trabant și Lăstun.
- Dacă mașina e Trabant sau Lăstun:
Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie else).
- Printează S-ar putea să vă placă mașina x.

'''

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

for i in masini:
    if i == 'Trabant' or i == 'Lăstun':
        continue
    print(f'S-ar putea să vă placă mașina {i}')

print(('---------------'))

'''
5. Modernizează parcul de mașini:
● Crează o listă goală, masini_vechi.
● Itereaza prin mașini.
● Când găsesti Lăstun sau Trabant:
- Salvează aceste mașini în masini_vechi.
- Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
● Printează Modele vechi: x.
● Modele noi: x.
'''

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
masini_vechi = []
for i in masini:
    if i == 'Trabant' or i == 'Lăstun':
        masini_vechi.append(i)
       # print(masini_vechi)
        masini_noi = masini.index(i)
        masini[masini_noi] = 'Tesla'
print('Modele vechi:', masini_vechi)
print('Modele noi:', masini)

print(('---------------'))

'''
6. Având dict:
pret_masini = {'Dacia': 6800,'Lăstun': 500,'Opel': 1100,'Audi': 19000,'BMW': 23000 }
Vine un client cu un buget de 15000 euro.
● Prezintă doar mașinile care se încadrează în acest buget.
● Itereaza prin dict.items() și accesează mașina și prețul.
● Printează Pentru un buget de sub 15000 euro puteți alege mașină  x Lastun
● Iterează prin listă.
'''

pret_masini = {'Dacia': 6800 , 'Lăstun': 500 ,'Opel': 1100 , 'Audi': 19000 , 'BMW': 23000 }
buget = 15000
for i , j in pret_masini.items() :
     if j <= buget :
         print(f'Pentru un buget de pana in {buget} euro puteti alege masina: {(i,j)}')


print(('---------------'))

'''
7. Având lista:
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
● Iterează prin ea.
● Afișează de câte ori apare 3 (nu ai voie să folosești count).
'''
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

for i in numere:
    if i == 3:
        i = i+1
        print(f'Numarul 3 apare de {i} ori in lista de numere !')
        break

print(('---------------'))

'''
8. Aceeași listă:
● Iterează prin ea
● Calculează și afișează suma numerelor (nu ai voie să folosești sum).
'''

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
suma = 0
for i in numere :
    suma = suma + i
print(f'Suma numerelor din lista este {suma}!')

print(('---------------'))


'''
9. Aceeași listă:
● Iterează prin ea.
● Afișază cel mai mare număr (nu ai voie să folosești max).
'''
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
mare = 0
for i in numere:
    if i > mare:
        mare = i
print(f'Cel mai mare numar este {mare}')

print(('---------------'))

'''
10. Aceeași listă:
● Iterează prin ea.
● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
Ex: dacă e 3, să devină -3
● Afișază noua listă.

'''
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
noua_lista =[]
for i in numere:
    #if i > 0 : #cu i >0 nu imi printa in noua lista  0 '-4
        i =-abs(i)
        noua_lista.append(i)
print(f'Lista noua este : {noua_lista}')

print(('---------------'))


'''Exerciții Opționale - grad de dificultate: Mediu spre greu: may need Google.
1.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
Itereaza prin listă alte_numere
Populează corect celelalte liste
Afișeaza cele 4 liste la final
'''
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []

for i in alte_numere:
    if (i % 2) == 0:
        numere_pare.append(i)
    else :numere_impare.append(i)
print (f'Numere pare:{numere_pare}')
print(f'Numere impare {numere_impare}')
for i in alte_numere:
    if i==i>0:
        numere_pozitive.append(i)
    else : numere_negative.append(i)
print(f'Numere pozitive :{numere_pozitive}')
print(f'Numere pozitive :{numere_negative}')

'''
2. Aceeași listă:
Ordonează crescător lista fară să folosești sort.
Te poți inspira vizual de aici.
https://www.youtube.com/watch?v=lyZQPjUT5B4
'''

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]

from itertools import permutations
for p in permutations(alte_numere):
    if all(i<=j for i,j in zip(p,p[1:])):
             print(p)
             break

#2
numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
print(f'Lista originala este {numere}')
swap = 0
for i in range(len(numere)) :
    for j in range(len(numere) - 1) :
         if numere[j] > numere[j + 1]:
             swap = numere[j]
             numere[j]=numere[j + 1]
             numere[j + 1] = swap
print(f'Lista ordonata este {numere}')





'''
3. Ghicitoare de număr:
numar_secret = Generați un număr random între 1 și 30
Numar_ghicit = None
Folosind un while
User alege un număr
Programul îi spune:
Nr secret e mai mare
Nr secret e mai mic
Felicitări! Ai ghicit!
'''
import random
numar_secret = random.randint(1,30)
Numar_ghicit = None
while Numar_ghicit is None:
    x = int(input('Alege un numar intre 1 si 30'))
    if x < numar_secret:
        print('Nr secret e mai mare')
    elif x > numar_secret:
         print('Nr secret e mai mic')
    elif x == numar_secret:
         print('Felicitări! Ai ghicit!')

'''
4. Alege un număr de la tastatură
Ex: 7
Scrie un program care să genereze în consolă următoarea piramidă
1
22
333
4444
55555
666666
7777777

Ex:3
1
22
333
'''

