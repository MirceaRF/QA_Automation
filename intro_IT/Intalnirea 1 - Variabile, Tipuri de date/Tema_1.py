'''1. În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.

    1.O variabila este un container din memorie care stochează valori

    2. Declară și initializează câte o variabilă din fiecare din următoarele tipuri de
variabilă :

- string
- int
- float
- bool

Observație: Valorile vor fi alese de tine după preferințe.
'''

#2

# String
import string

marca_Telefon = 'Iphone'
# String
model =  '13'
# Integer
memoriaGB = 128
# float
pret = 4500.5
# boolean
neverlocked = True

#3 3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.

print(type(marca_Telefon))
print(type(model))
print(type(memoriaGB))
print(type(pret))
print(type(neverlocked))

'''4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în
aceeași variabilă (suprascriere):
- Verifică tipul acesteia.'''

pret = round(pret)
print(type(pret))

'''
5. Folosește print() și printează în consola 4 propoziții folosind cele 4 variabile.

Rezolvă nepotrivirile de tip prin ce modalitate dorești.
'''
print(f'Am cumparat un telefon {marca_Telefon} {model} are memoria de {memoriaGB} GB cu pretul de {pret} si este deblocat de retea {neverlocked}')

'''
6. Citește de la tastatură:
    - numele;
    - prenumele.
  Afișează: 'Numele complet are x caractere'.
'''
numele = input('Numele')
prenumele = input('Prenumele')
#prop = 'Numele complet are x caractere'
#print(f'{numele} {prenumele}  are caractere')
print(f'Numele complet are {(len(numele)+ len(prenumele))}  caractere')

'''
7. Citește de la tastatură:
- lungimea;
- lățimea.
Afișează: 'Aria dreptunghiului este x'.
'''
lung=int(input('Lungimea'))
lat=int(input('Latimea'))
print(f'Aria dreptunghiului este {int(lung*lat)}')

'''
8. Având stringul: 'Coral is either the stupidest animal or the smartest rock':

- citește de la tastatură un int x;
- afișează stringul fără ultimele x caractere.

ex: Dacă ai ales 7 => 'Coral is either the stupidest animal or the smarte'.
'''
prop ='Coral is either the stupidest animal or the smartest rock'
x=int(input('Introdu nr '))# am citit de la tastatura nr de caractere care se doreste a fi scoase de la finalul stringului
print(prop[0:len(prop)-x])


'''
9. Același string:
a. declară un string nou care să fie format din primele 5 caractere + ultimele
5;
b. afișează de câte ori apare cuvântul 'the';
c. înlocuiește ‘the’ cu ‘THE’ peste tot - printează rezultatul;
d. salvează într-o variabilă și afișează indexul de start al cuvântului ‘rock’;
- hint: este o funcție care te ajută să faci asta;
folosind această variabilă + slicing, afișează tot stringul până la acest
cuvânt.

Output: 'Coral is either the stupidest animal or the smartest'
'''
#a
prop ='Coral is either the stupidest animal or the smartest rock'
prop_1=prop[0:5]+prop[len(prop)-5:]
print(prop_1)

#b
print(prop.count('the'))
#c
print(prop.replace('the','THE'))
#D
piatra=prop.index('rock')
print(piatra)
print(prop[0:piatra])

'''
10. Exercițiu:

- citește de la tastatură un string;
- verifică dacă primul și ultimul caracter sunt la fel.
Observație: se va folosi un assert.
Atenție: se dorește că programul să fie case insensitive - 'apA' e acceptat.
'''
text = input('Introduceti un cuvant:')
assert text[0].upper() == text[-1:].upper(), f'Eroare: primul și ultimul caracter nu sunt la fel '
#print('sunt la fel')
#assert text.upper[0] == text.upper[-1:], f'Eroare: primul și ultimul caracter nu sunt la fel '
print('primul și ultimul caracter sunt la fel')

'''
11. Având stringul '0123456789':
- Afișează doar numerele pare;
- Afișează doar numerele impare;
- hint: folosește slicing, controlează din pas.
'''
nr = '0123456789'
print(nr[0::2])
print(nr[1::2])

'''
12. Utilizand stringul de la 9.d.
- folosește un assert că să verifici dacă acest string conține doar numere;
- hint: merge cu slicing? Probabil că nu... Ce mai știi atunci legat de
string? Poate găsești o funcție ajutătoare.
'''
text_1 = 'rock'
#print(type(text_1))
#text_1 = int(text_1)
#print(type(text_1))

#assert type(text_1) == type('rock') ,f'Eroare'
assert text_1.isnumeric() == False ,f'Eroare'

#assert text_1 == text_1.__contains__ ,f'Eroare'
print('Contine nr')
#assert text_1 == text_1.isnumeric() , f'Eroare'
#print('True')

'''
Exerciții Opționale - grad de dificultate: Mediu spre greu (s-ar putea să ai
nevoie de Google).
1. Exercițiu:
- citește de la tastatură un string de dimensiune impară;
- afișează caracterul din mijloc.
'''
#text_2 = input('Text impar')
#text_3=int(text_2)
#print(not (text_3)/2)
#mijloc = len(text_2)/2
#text_2[(len(text_2)/2)]
#print(mijloc)

def middle_char(txt):
  return txt[(len(txt)-1)//2:(len(txt)+2)//2]
text = input('text')
print("Original string: ",text)
print("Middle character(s) of the said string: ",middle_char(text))

#solutia 2
#def get_middle(txt):
   # return txt[(len(txt)-1)/2:len(txt)/2+1]
#txt = input('text')
#print("Original string: ",txt)
#print("Middle character(s) of the said string: ",get_middle(txt))
                #Nu merge ##



#2 luci
#stringImpar = input('Scrie stringul ')  # ana are cas
#mijloc = stringImpar[math.floor(len(stringImpar)/2)]
#print(mijloc)  # r



    #2  2. Folosind assert, verifică dacă un string este palindrom.
def is_palindrome(s):
    string = s
    if (string==string[::-1]):
        print("The string IS a palindrome")
        return True
    else:
        print("The string is NOT a palindrome")
        return False

assert is_palindrome('noon')
assert not is_palindrome('house'), f'ERROR'

'''  #3.3. Folosind o singură linie de cod :
- citește un string de la tastatură (ex: 'alabala portocala');
- salvează fiecare cuvânt într-o variabilă;
- printează ambele variabile pentru verificare.'''


sentence = input('Text')
split_sentence = sentence.split(' ')
print(split_sentence)

'''
4. Exercițiu:
- citește un string de la tastatură (ex: alabala portocala);

- salvează primul caracter într-o variabilă - indiferent care este el, încearcă
cu 2 stringuri diferite;
- capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul
caracter => alAbAlA portocAla.
'''
