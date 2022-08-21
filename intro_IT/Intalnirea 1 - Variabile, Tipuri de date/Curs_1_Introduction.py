print('Hello world')

'''comentarii multi line
nota explicativa, ignore la rulare
'''

# comentariu in line

# 1 - CTRL + / IN WINDOWS   or   COMAND + / in MAC
# 2
# 3

# print () - afisarea in consola a informatiei, intre parateze textul care se afiseaza, se se pune intre ' '  sau " "
# print este o functie; o modalitate prin care putem sa grupam o serie de linii de cod care pot refolosite


# VARIABILE
meserie = 'contructor'

meserie_1 = 'brutar'
print(meserie)
meserie_2 = 'aviator'
print(meserie_2)

# print('meserie') - not ok in caz de print variabila, nu printeaza continutul variabilei, ci doar informatia din ghilimele


## reguli de denumire a unei variabile
'''
- numele trebuie sa fie unic
- nu putem sa punem s[atiu in numele unei variabile( nume variabila - nu este corect)
- variabilele in python trebuie sa fie initializate in momentul definirii
- trebuie sa inceapa cu litera mica si sa contina litere, cifre sau _
     * exista 2 tipuri de format pt numele variabelor:  camelCase, snake_case  (meserie_unu sau meserieUnu)
- sunt case sensitive: nume variabile cu n sau N sunt diferite



'''

# o variabila poate sa-si schimbe continutul sau tipul de date in timpul rularii programului (change from string in int)
## functia type returneaza tipul de date al variabilei (<class 'str'>/ <class 'int'>)
variabila = 'test'
print(type(variabila))
variabila = 5
print(type(variabila))

# putem sa alocam aceeasi valoare mai multor variabile sau sa initializam mai multe variabile in acelasi timp
var_1 = 5
var_2 = 5
var_3, var_4 = 7.3, 6
print(var_1, var_2, var_3, var_4)
print(var_3, var_4)

# , este separator/// . se delimiteaza zecimal


# TIPURI DE DATE

'''
proprietate a unei variabile care defineste ce fel de informatii pot sa fie/ sunt stocate in acea variabila
functia type ne arata care este tipul de date al unei variabile definite, exemplu mai sus
exemple tipuri de date:
    - int -> stocheaza doar nr intregi
    - float -> numere zecimale (5.0)
    - boolean -> valori T or F
    - string -> text de orice fel (litere, cifre, caractere speciale )


concatenare - operatiune care uneste 2 stringuri

'''

var_int = 4
var_float = 4.5
var_boolean = True
var_string = 'string text'

print(type(var_int))
print(type(var_float))
print(type(var_boolean))
print(type(var_string))

## typecasting
nr_1 = 5
nr_2 = '6'
# print(nr_2 + nr_1)  TypeError: can only concatenate str (not "int") to str
nr_2 = 6
print(nr_2 + nr_1)  # s-au adunat valorile

nr_1 = '5'
nr_2 = '6'
print(nr_1 + nr_2)  # a concatenat continutul var_1 cu continutul var_2/ s-au lipit

nr_1 = 5

print(str(nr_1) + nr_2)  # am facut typecasting pentru nr_1 si am fortat continutul lui nr_1 la string
print(nr_1 + int(nr_2))  # am facut typecasting pentru nr_2 si am fortat continutul lui nr_2 la int

# vrem sa printam suma celor 2 numere in format de tip float
# sol 1
print(float(nr_1) + float(nr_2))

# sol 2
print(float(nr_1 + int(nr_2)))
nr_2 = 6
print(float(nr_1 + nr_2))

nr_3 = 5
nr_4 = 6.5
print(nr_3 + nr_4)

nume = 'Andreea'
print('Numele meu este: ' + nume)
varsta = 34
print('Numele meu este: ' + nume + ' si am ' + str(varsta) + ' ani')

print(f'Numele meu este: {nume} si am {varsta} ani')

# Assert - este o modalitate prin care evaluam dacaezultatul unei expresii este T or F => boolean
# opreste executia codului din punctul executiei si avem eroare la assert
nume = 'emag'
assert nume == 'emag', f'Eroare: continutul variabilei nume nu este {nume}'
# print(assert nume)
# print(nume)

## daca rulam doar asta, retuneaza T or F, dar nu opreste executia testului
# nume = "Andreea"
print(nume == "Andrea")

## input
# este o modalitate prin care cerem utilizatorului de la tastatura
# input() - nu va afisa pe ecran nici un mesaj, dar nu va termina executia pana nu va primi un input

# nume = input('Va rugam sa introduceti input: ')
# #input('Va rugam sa introduceti input: ')
# print(nume)


# string slicing
# extragem dintr-un string anumite bucati

nume = 'Marian'
print(len(nume))
text_de_procesat = 'Ana are mere'
print(text_de_procesat[4])

print(text_de_procesat[0:3])
print(text_de_procesat[0:6:2])  # a 3-a cifra arata din cate in cate merge/ pasul/ printeaza fiecare a 2-a litera

# string slicing in sens invers
print(text_de_procesat[::-1])  # se ia inceputul si sfarsitul stringului prin ::// le vede in oglinda prin -1 la a 3-a conditie
print(text_de_procesat[2::-1])

# index 0 = A
# index 1 = n
# index 2 = a
# index 3 =  (spatiu)


web = 'jdbc:mysql://database.company.com:3306/databaseuat_stage?zeroDateTimeBehavior=convertToNull'
print(web.index('://'))
print(web[13::])
print(text_de_procesat.index('are'))
print(text_de_procesat[4::])









