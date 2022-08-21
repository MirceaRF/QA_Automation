'''

Pentru toate exercițiile se va folosi noțiunea de if în rezolvare.
Indirect vei exersa și operatorii în cadrul condițiilor ramurilor din if.
X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe.
X este un int.


1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if
else.


 1.   Instructiunile conditionale determina programele sa testeze diferite conditii si in functie de
  acestea sa decida executia anumitor comenzi.
 Practic, dacă condiția este validă, atunci executăm instrucțiunile --
 Condiția este o expresie de tip bool și se consideră a fi adevărată doar dacă este adevărată (true).
    - Are tot timpul fix 2 ramuri.
    - If are condiție urmată de:

    -Else nu mai are nevoie de condiție, deoarece înseamnă în celălat caz.

  Folosind combinatia "if() ... else" (daca ... altfel) putem stabili comenzi care sa fie
  executate si cand conditia instructiunii "if()" este FALSE.
Forma generala a instructiuni "if() ... else" este urmatoarea :

if (conditie)
    # codul care va fi executat daca este Adevarata conditia

else
    # codul ce va fi executat daca conditia este falsa

- Unde 'conditie' poate fi orice expresie logica.
Daca rezultatul conditiei este TRUE se executa codul care apartine de "if()",
in caz contrar, cand conditia returneaza FALSE, sunt executate comenzile  de la "else".


'''

# 2.  2. Verifică și afișează dacă x este număr natural sau nu.
from typing import Set

x = int(input('Alegeti un numar:'))
if x in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ) :
    print('Numarul este natural !')
else:
    print('***Nu ati ales un numar natural***')

'''
3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
'''

x = int(input('Alegeti un numar:'))
if x >0 :
    print('Numar pozitiv')
if x<0 :
     print('Numar negativ')
if x == 0:
    print('Numar neutru')

'''
4. Verifică și afișează dacă x este între -2 și 13.
'''

x = int(input('Alegeti un numar intre -2 si 13 :'))
if x>=-2 and x<=13 :
    print('Ati ales un nr in intervalul corect !')
else: print('*** Nu ati ales un nr din intervalul corect!***')


'''
5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5.
'''
x = int(input('X'))
y = int(input('Y'))
z = x-y
if  z == z<5 :
    print(f'Diferența dintre x și y este {z} mai mică de 5')
else:
 print('**Diferenta este mai mare de 5** ')




 '''
 6. Verifică dacă x NU este între 5 și 27 - a se folosi ‘not’.
 '''

x = int(input('Alegeti un nr intre 5 si 27 :'))
print(not(x>=5 and x<=27))


x = int(input('X= '))
if (not (x>=5 and x<=27)):
   print('NU: Numarul NU se afla in interval')
else:
   print('DA: Numarul se afla in interval')


'''
7.
x și y (int)
Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai
mare.
'''

x = int(input('X'))
y = int(input('Y'))
if x==y :
    print('Numerele sunt egale')
elif  x>y:
    print(f' {x} Este mai mare')
elif y>x:
    print(f' {y} Este mai mare')


'''
8.
X, y, z - laturile unui triunghi.
Afișează dacă triunghiul este isoscel, echilateral sau oarecare.
'''

print('X, y, z - Laturile unui triunghi.')
x = int(input('X'))
y = int(input('Y'))
z = int(input('Z'))
if ( x==y and z!=x and z!=y) or (x==z and y!=x and y!=z) or (y ==z and x!=y and x!=z):
    print('Triunghi isoscel')
elif  x==y==z :
       print('Triunghi echilateral')
else:
    print('Triunghi oarecare')

# Metoda 2
j = int(input('Latura X = '))
k = int(input('Type y = '))
l = int(input('Type z = '))

if (j==k!=l or j!=k==l or j==l!=k):
    print('Triunghiul este isoscel')
elif (j==k==l):
    print('Triunghiul este echilateral')
elif(j==0 or k==0 or j==0):
    print('Triunghiul nu exista')
else:
    print('Triunghiul este oarecare')


'''
9. Citește o literă de la tastatură.

Verifică și afișează dacă este vocală sau nu
'''
litera = str(input('Citeste o litera si afla daca este vocala :'))
vocale = ['a', 'e', 'i', 'o', 'u', 'ă', 'î']
if litera in vocale:
    print('Ati ale o vocala')
else:
    print('Litera aleasa nu este o vocala')


'''
10.Transformă și printează notele din sistem românesc în >
Peste 9 => A
Peste 8 => B
Peste 7 => C
Peste 6 => D
Peste 4 => E
4 sau sub => F

'''
nota = float(input('Nota'))
if nota >= 9 :
    print('A')
elif nota >= 8 and nota <9:
     print('B')
elif nota >= 7 and nota < 8:
     print('C')
elif nota >=6 and nota <7:
     print('D')
elif nota >4 and nota < 6 :
    print('E')
elif nota <=4 :
     print('F')


'''
Exerciții Opționale - grad de dificultate: Mediu spre greu - might need Google.
1.Verifică dacă x are minim 4 cifre (x e int).
(ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
'''

#x = int(input('Numar de 4 cifre:'))
#num = raw_input('Numar de 4 cifre: ')
#num = int(input('Numar de 4 cifre: '))
#num = raw_input("Enter a 4 digit number: ")
#num = int(input('Numar de 4 cifre: '))
#if (len(num) == 4 and num.isdigits == True):
#if ((num) >= 4 ):

num = (input('Numar de 4 cifre: '))
if len(num) >= 4 and num.isdigit():
    print('Numarul are minim 4 cifre')
else:
    print('Error!')

#var 2
number_x=123
if (len(str(number_x))>=4):
   print (f'Numarul X are minim 4 cifre')
else:
   print('Numarul are mai putin de 4 cifre')




'''
2.Verifică dacă x are exact 6 cifre.
'''
num = (input('Numar de 6 cifre: '))
if len(num) == 6 and num.isdigit():
    print('Numarul are exact 6 cifre')
else:
    print('Error!')


'''
2.Verifică dacă x are exact 6 cifre.
'''
#if (count(num) == 6):
 #   print(f'Numarul are {count(num)} cifre')
'''
3.Verifică dacă x este număr par sau impar (x e int).
'''
number_x2 = 5
if (number_x2 % 2 == 0):
    print(f'Numarul {number_x2} este par')
else:
    print(f'Numarul {number_x2} este impar')
'''

'''



'''
3.Verifică dacă x este număr par sau impar (x e int).
'''
num = int(input ('Verifică dacă x este număr par sau impar'))
if (num % 2) == 0:
    print ('Numarul e par')
else:
    print ('Numarul e impar')

'''
4. x, y, z (int)
Afișează care este cel mai mare dintre ele?
'''

x1 = 3
y1 = 5
z1 = 5
if (x1 > y1 and x1 > z1):
    print(f'{x1} este cel mai mare numar')
elif (y1 > x1 and y1 > z1):
    print(F'{y1} este cel mai mare numar')
elif (z1 > x1 and z1 > y1):
    print(f'{z1} este cel mai mare numar')
else:
    print("Cel putin 2 numere sunt egale")






# Python program to find the largest
# number among the three numbers

a = int(input('a:'))
b = int(input('b:'))
c = int(input('c:'))
def maximum(a, b, c):
    if (a >= b) and (a >= c):
        largest = a
    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c
    return largest
print(maximum(a, b, c))


#metoda2

# creating empty list

list1 = []

# asking number of elements to put in list
num = int(input("Enter number of elements in list: "))

# iterating till num to append elements in list
for i in range(1, num + 1):
    ele = int(input("Enter elements: "))
    list1.append(ele)

# print maximum element
print("Largest element is:", max(list1))



x = int(input(' Introuceti numarul x  '))
print('x=', x)
y = int(input('Introuceti numarul y  '))
print('y=',y)
z = int(input('Introuceti numarul z '))
print('Z=', z)

if (x>y and x>z):
   print (f'X = {x} este cel mai mare număr')
elif (y>x and y>z):
   print (f'Y = {y} este cel mai mare număr')
elif (z>y and z>x):
   print(f'Z = {z} este cel mai mare număr')






'''
5.
X, y, z - reprezintă unghiurile unui triunghi
Verifică și afișează dacă triunghiul este valid sau nu.
'''


#Un triunghi este valid dacă suma celor trei unghiuri este egală cu 180 de grade.
a = int(input('a:'))
b = int(input('b:'))
c = int(input('c:'))
if ((a + b + c == 180) and a != 0 and b != 0 and c != 0):
       print('Triunghi valid')
else:
       print('Triunghi invalid')


'''
1.Verificare îmbarcare persoane
Ține minte următoarele date:
- Vârstă;
- Însoțit de mama;
- Însoțit de tata;
- Pașaport;
- Act permisiune mama;
- Act permisiune tata.
Condiții de îmbarcare
- Dacă pers are vârstă peste 18 ani și are pașaport.
- Dacă pers are sub 18 ani, are pașaport și e însoțită de ambii părinți.
- Dacă pers are sub 18 ani, are pașaport, e însoțită de cel puțin un părinte
și are permisiune în scris de la celalat părinte.
● Aici vreau să testezi codul cu toate variantele posibile.
● Să generezi cazuri de test și expected result, apoi să rulezi codul și să
completezi actual results.
Ex:
Vârstă 19 ani, nu am pașaport => Nu mă pot îmbarca.
Vârstă 17 ani, am pașaport, ambii părinți => Mă pot îmbarca.
'''


varsta = int(input("Va rugam sa introduceti varsta pasagerului: "))
pasaport = input("Are persoana pasaport? DA/NU: ")
if(pasaport == 'DA' and varsta >=18):
   print("Calatorie placuta")
elif(pasaport == 'DA' and varsta<18):
   parinti = input("Sunt ambii parinti prezenti? DA/NU: ")
   if(parinti=='DA'):
       print("Calatorie placuta")
   else:
       un_parinte = input("E cel putin un parinte prezent? DA/NU: ")
       if(un_parinte == 'DA'):
           parinte_lipsa = input("Introduceti parintele lipsa: Mama / Tata: ")
           permisiune = input(f"Exista permisiune de la {parinte_lipsa}? DA / NU: ")
           if(permisiune=="DA"):
               print("Calatorie placuta")
           else:
               print("Alerteaza autoritatile")
       else:
           print("Alerteaza autoritatile")
else:
   print("Ne pare rau, aveti nevoie de un pasaport valid pentru a calatori")


'''
2. Joc ghicit zarul

Varianta 1 de rezolvare (simpla):

import random

numar_ales = random.randint(1,6)
print(numar_ales)
zar = int(input("Alegeti un numar "))
incercare = 1
if zar == numar_ales:
   print(f"Ai ghicit. Felicitări. Ai ales {zar} și zarul a fost {numar_ales}.")
elif zar<numar_ales:
   print(f"Ai pierdut. Ai ales un număr mai mic. Ai ales {zar} dar a fost {numar_ales}.")
else:
   print(f"Ai pierdut. Ai ales un număr mai mare. Ai ales {zar} dar a fost {numar_ales}.")

Varianta 2 de rezolvare (complexa):

import random

numar_ales = random.randint(1,6)
print(numar_ales)
zar = int(input("Alegeti un numar "))
incercare = 1
if zar == numar_ales:
   print(f"Ai ghicit. Felicitări. Ai ales {zar} și zarul a fost {numar_ales}.")
elif zar<numar_ales:
   zar = int(input("Mai ai doua incercari. Numarul este mai mare "))
   incercare+=1
   if zar == numar_ales:
       print(f"Ai ghicit. Felicitări. Ai ales {zar} și zarul a fost {numar_ales}.")
   elif zar<numar_ales:
       zar = int(input("Mai ai o incercare. Numarul este mai mare "))
       incercare+=1
       if zar == numar_ales:
           print(f"Ai ghicit. Felicitări. Ai ales {zar} și zarul a fost {numar_ales}.")
       else:
           if zar<numar_ales:
               print(f"Ai pierdut. Ai ales un număr mai mic. Ai ales {zar} dar a fost {numar_ales}.")
           else:
               print(f"Ai pierdut. Ai ales un număr mai mare. Ai ales {zar} dar a fost {numar_ales}.")
   else:
       zar = int(input("Mai ai o incercare. Numarul este mai mic "))
       incercare += 1
       if zar == numar_ales:
           print(f"Ai ghicit. Felicitări. Ai ales {zar} și zarul a fost {numar_ales}.")
       else:
           if zar < numar_ales:
               print(f"Ai pierdut. Ai ales un număr mai mic. Ai ales {zar} dar a fost {numar_ales}.")
           else:
               print(f"Ai pierdut. Ai ales un număr mai mare. Ai ales {zar} dar a fost {numar_ales}.")
else:
   zar = int(input("Mai ai doua incercari. Numarul este mai mic "))
   incercare += 1
   if zar == numar_ales:
       print(f"Ai ghicit. Felicitări. Ai ales {zar} și zarul a fost {numar_ales}.")
   elif zar < numar_ales:
       zar = int(input("Mai ai o incercare. Numarul este mai mare "))
       incercare += 1
       if zar == numar_ales:
           print(f"Ai ghicit. Felicitări. Ai ales {zar} și zarul a fost {numar_ales}.")
       else:
           if zar < numar_ales:
               print(f"Ai pierdut. Ai ales un număr mai mic. Ai ales {zar} dar a fost {numar_ales}.")
           else:
               print(f"Ai pierdut. Ai ales un număr mai mare. Ai ales {zar} dar a fost {numar_ales}.")
   else:
       zar = int(input("Mai ai o incercare. Numarul este mai mic "))
       incercare += 1
       if zar == numar_ales:
           print(f"Ai ghicit. Felicitări. Ai ales {zar} și zarul a fost {numar_ales}.")
       else:
           if zar < numar_ales:
               print(f"Ai pierdut. Ai ales un număr mai mic. Ai ales {zar} dar a fost {numar_ales}.")
           else:
               print(f"Ai pierdut. Ai ales un număr mai mare. Ai ales {zar} dar a fost {numar_ales}.")




#
import random
x=int(input('Alege un numar de la 1 la 6: '))
a=random.randrange(1,6)
if x<a:
    print(f'Ai pierdut. Ai ales un numar mai mic decat {a}')
elif x>a:
    print(f'Ai pierdut. Ai ales un numar mai mare decat {a}')
else:
    print(f'Ai ghicit. Felicitari! Ai ales {x} si zarul a fost {a}')

Message #studiu_in_echipa


mijloc
stringImpar = input('Scrie stringul ')  # ana are cas
mijloc = stringImpar[math.floor(len(stringImpar)/2)]
print(mijloc)  # r
'''