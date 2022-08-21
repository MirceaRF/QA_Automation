'''
1.Clasa Cerc
Atribute: raza, culoare
Constructor pentru ambele atribute
Metode:
● descrie_cerc() - va PRINTA culoarea și raza
● aria() - va RETURNA aria
● diametru()
● circumferinta()

'''
import math


class Cerc:
    # atribute/campuri
    culoare = 'Verde'
    raza = 10


    def __init__(self,culoare,raza):
        self.culoare = culoare
        self.raza = raza

    def descrie_cerc(self):
        print(f'Cercul cu raza de {self.raza} are culoarea {self.culoare}')

    def diametru_Cerc(self, raza=10):
        return 2 * raza

    def circumferinta_Cerc(self,raza=10):
        return 2 * math.pi * raza

    def aria_Cerc(self,raza=10):
        return math.pi * raza * raza


    diametru = diametru_Cerc(raza)
    circumferinta = circumferinta_Cerc(raza)
    aria = aria_Cerc(raza)

    print(" Diametrul cercului = %.2f" % diametru)
    print(" Circumferinta cercului = %.2f" % circumferinta)
    print(" Aria cercului = %.2f" % aria)
    print(f'Cercul cu raza de: {raza} are culoarea: {culoare}')
instanta_Cerc =Cerc('Albastru', 5)
print(instanta_Cerc.descrie_cerc())
#print(f'{instanta_Cerc.descrie_cerc()} aria de: {instanta_Cerc.aria_Cerc()} diametru de :{instanta_Cerc.diametru_Cerc()}')

print('---------------------------')
'''
 2. Clasa Dreptunghi
Atribute: lungime, latime, culoare
Constructor pentru toate atributele
Metode:
● descrie()
● aria()
● perimetrul()
● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
Ea va lua ca și parametru o nouă culoare și va suprascrie atributul self.culoare. Puteti verifica schimbarea culorii 
prin apelarea metodei descrie().
'''
class Dreptunghi:
    #Atribute:
    lungime =10
    latime = 5
    culoare ='Albastru'
    def __init__(self,lungime,latime,culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare
    def descrie_Dreptunghi(self):
        print(f'Dreptunghiul cu lungimea de : {self.lungime} latimea de : {self.latime} are culoare : {self.culoare}')


    def aria_Dreptunghi(self,lungime,latime):
        aria = latime * lungime
        return aria
    #print("Aria dreptunghiului  este", aria_Dreptunghi(lungime,latime,))

    def perimetru_Dreptunghi(self,lungime,latime):
        perimetru = 2*(lungime+latime)
        return perimetru

    def schimbă_culoarea(self,noua_culoare):
        self.culoare = noua_culoare

instanta_Dreptunghi= Dreptunghi(5,10,'Verde')
print(instanta_Dreptunghi.descrie_Dreptunghi())
print(instanta_Dreptunghi.aria_Dreptunghi(lungime=15,latime=10))

print('---------------------------')

'''
3. Clasa Angajat
Atribute: nume, prenume, salariu
Constructor pt toate atributele
Metode:
● descrie()
● nume_complet()
● salariu_lunar()
● salariu_anual()
● marire_salariu(procent)
'''

class Angajat:
    #Atribute:
    nume = 'Floroaie'
    prenume = 'Mircea'
    salariu = 5000
    def __int__(self,nume,prenume,salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu
    def descrie_Angajat(self,nume,prenume,salariu):
        print(f'Angajatul cu numele de {self.nume_complet} are salariu  de {self.salariu}')
    def nume_complet(self,nume,prenume):
        nume_complet = nume + prenume
        return nume_complet
    def salariu_lunar(self):
        print(f'Salariu lunar este {self.salariu}')
    def salariu_anual(self,salariu):
        salariu_anual = salariu * 12
        return salariu_anual
    def marire_salariu(self,procent):
        procent = 0.3 * self.salariu
        return procent

instanta_Angajat = Angajat
#print(instanta_Angajat.salariu)
print(f'Angajatul {instanta_Angajat.nume}  are Salariu anual de {instanta_Angajat.salariu_anual(Angajat,5000)}')

print('---------------------------')

'''
4.Clasa Cont
Atribute: iban, titular_cont, sold
Constructor pentru toate atributele
Metode:
● afisare_sold() - Titularul x are în contul y suma de n lei
● debitare_cont(suma)
● creditare_cont(suma)
'''
class Cont:
    iban =[12345]
    titular_cont = 'Mircea Floroaie'
    sold = 10000
    def __int__(self,iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold
    def afisare_sold(self):
        print(f' Titularul {self.titular_cont} are în contul {self.iban} suma de {self.sold} lei ')
    def debitare_cont(self,suma):
        suma_ramasa =self.sold-suma
        return suma_ramasa
    def creditare_cont(self,suma):
        suma_creditata =self.sold+suma
        return suma_creditata
instantare_Cont = Cont
print(f' Titularul {Cont.titular_cont} are în contul {Cont.iban} suma de {Cont.sold} lei ')
instantare_Cont.debitare_cont(Cont,1000)
print(f' Din contul titularului {Cont.titular_cont} cu nr iban {Cont.iban} a fost debitata suma de 1000 Ron soldul ramas este: {instantare_Cont.debitare_cont(Cont,1000)} lei ')
instantare_Cont.creditare_cont(Cont,5000)
print(f'Contul titularului {Cont.titular_cont} a fost creditat cu suma de 5000 Ron,soldul actual este {instantare_Cont.creditare_cont(Cont,5000)}')