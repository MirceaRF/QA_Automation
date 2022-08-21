'''
1.Funcție care să calculeze și să returneze suma a două numere
'''

def suma(a,b):
    suma=a+b
    return suma
num1=int(input("Introduceti primul numar: "))
num2=int(input("Introduceti al doilea numar :"))
print("Suma celor doua numere este",suma(num1,num2))  #am apelat functia

print('------------------')

'''
2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar
'''
def par_impar(x):
    return x % 2 != 1
x =int(input("Introduceti un numar Par sau Impar: "))
print(f'Numarul este  {par_impar(x)} ')

print('------------------')

'''
3. Funcție care returnează numărul total de caractere din numele tău complet.
(nume, prenume, nume_mijlociu)
'''

def nr_caractere(nume,prenume,prenume_mijlociu):
    return len(nume+prenume+prenume_mijlociu)
nume=input('Numele:')
prenume = input('Prenumele:')
prenume_mijlociu =input('Prenumele mijlociu')
print(f'Numele are {nr_caractere(nume,prenume,prenume_mijlociu)} caractere')

print('------------------')

'''
4. Funcție care returnează aria dreptunghiului
'''

def aria(a,b):
    aria = a*b
    return aria

lungimea=int(input("Introduceti lungimea : "))
latimea =int(input("Introduceti latimea :"))
print("Aria dreptunghiului  este",aria(lungimea,latimea))  #am apelat functia

print('------------------')

'''
5. Funcție care returnează aria cercului
'''
# def cerc(pi=3.14, raza=raza**2 ):
#     #R2=R2**2
#     return cerc(pi,R2)
# raza=int(input("Introduceti raza cercului : "))
# print("Aria cercului este",cerc(pi=3.14,R2=raza**2))  #am apelat functia

print('------------------')

def aria_cerc(r):
    pi = 3.14
    r = float(r)
    aria_c = pi*r*r
    return aria_c
r = float(input("Introduceti raza cercului : "))
print(f'Aria cercului cu raza {r} este ',aria_cerc(r))

print('------------------')

'''
6. Funcție care returnează True dacă un caracter x se găsește într-un string dat
și False dacă nu găsește.
'''
string ='Mircea'
def caracter():
    #string ='Mircea'
    if x in string:
        return bool(string)

x =str(input("Cauta caracterul in string: "))
print(f'Caracterul este ', bool(caracter()))

print('------------------')

'''
7. Funcție fără return, primește un string și printează pe ecran:
● Nr de caractere lower case este x
● Nr de caractere upper case exte y
'''

def lower_upper(str):
    upper, lower,  = 0, 0,
    for i in range(len(str)):
        if str[i].isupper():
            upper += 1
        else :
            if str[i].islower():
                 lower += 1

    print('Nr de caractere upper case este:', upper)
    print('Nr de caractere lower case este :', lower)


str = 'Mircea'
lower_upper(str)

print('------------------')

'''
8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu
numerele pozitive
'''
def lista(lista_nr):
    lista_nr = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
    lista_poz = [i for i in lista_nr if i >= 0]
    return lista_poz
lista_nr = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]

print(lista(lista_nr = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]))
print(f'Lista cu numere pozitive este:', lista(lista_nr))

print('------------------')


'''
9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
● Primul număr x este mai mare decat al doilea nr y
● Al doilea nr y este mai mare decat primul nr x
● Numerele sunt egale.
'''

def mic_mare(x,y):
    if x>y:
        print(f'Primul numar {x} este mai mare decat {y}')
    elif x<y:
        print(f'Al doilea numar {y} este mai mare decat {x}')
    else:
        print('Numerele sunt egale')
mic_mare(3,10)
mic_mare(10,3)
mic_mare(10,10)

print('------------------')

'''
10. Funcție care primește un număr și un set de numere.
● Printeaza ‘am adaugat numărul nou în set’ + returnează True
● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
returnează False
'''
nr =int(input('Introduceti un numar:'))
set ={22,6}
def nr_set(nr,set):
    if nr not in set:
        set.add(nr)
        print('Am adaugat numarul nou in set', set)
        return True
    else:
        print('Nu am adaugat numărul în set. Acesta există deja', set)
        return False

print(nr_set(nr,set))
print(nr_set(38,{22,6}))
print(nr_set(38,{22,38}))
