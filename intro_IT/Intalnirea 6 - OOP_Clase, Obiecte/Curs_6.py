"""
 Programare orientata pe obiecte reprezinta o modalitate prin care noi putem templetiza
atributele si comportamentul unui anumit element.

 Programarea orientata pe obiecte este prescurtata cu acronimul POO sau varianta in engleza
OOP  object oriented programming

 O clasa in general este unul din elementele de baza al programarii orientate pe obiecte
si reprezinta tiparul in sine

 O clasa reprezinta un tipar, dar nu va fi util pana cand nu va fi apelat
 Folosirea unei clase se poate face prin intermediul unui obiect
 Un obiect este o reprezentare efectiva a unei clase
 Crearea unui obiect se numeste instantiere, motiv pentru care, prin definitie,
        un obiect se spune ca este o instanta a unei clase
 In momentul in care cream un obiect, noi vom avea acces prin intermediul lui
        la toate atributele si metodele clasei
 O metoda este o functie definita in interiorul clasei


Exemplu: Clasa masina
Cand definim o clasa ne gandim ce atribute poate sa aiba elementul
si ce actiuni poate sa faca

O masina de exemplu poate sa aiba urmatoarele atribute:
 culoare
 viteza
 an_fabricatie
 marca
 model
 capacitate_rezervor
 tip_combustibil
 tractiune
 serie_sasiu
 cutie_viteze
 numar_inmatriculare

O masina poate sa faca urmatoarele actiuni
 pornire de pe loc
 oprire
 accelerare
 franare
 consum_instant
 revizie_tehnica (daca masina este in stare buna, trece revizia tehnica)
 schimbare_directie
 vopsire_masina

"""

"""
Definirea clasei se face prin intermediul keywordului "class"
De regula, prin conventie, numele unei clase va incepe cu litera mare si va fi scris in format
        camelCase sau snake_case (de regula snake_case in python)
La fel ca la structurile alternative (IF) si cele repetitive (WHILE, FOR), corpul unei clase este definit
        de indentarea codului, adica lasarea unui spatiu intre marginea fisierului si cod

Constructor = un agent care este responsabil cu crearea obiectului
In orice limbaj de programare POO exista un constructor implicit si un constructor explicit

Constructorul explicit este cel care se defineste de catre dezvoltator in cod
Constructorul implicit este cel care se apeleaza automat de python atunci cand constructorul explicit nu este definit

Constructorul este o functie/metoda specifica unei clase care are rolul de a crea obiectul in sine
Constructorul se defineste cu numele __init__ si intre paranteze se vor specifica atributele
        care vrem sa existe in mod obligatoriu la crearea obiectului
        Daca nu se specifica niciun parametru, atunci toate atributele vor fi optionale

In general, intr-o clasa, atunci cand vrem sa accesam elemente definite in interiorul clasei 
        fie ele atribute sau metode, ele trebuie accesate cu elementul "self."
"""


class Masina:
    # fields/attribute
    model = None
    culoare = "Galben"  # Negru
    marca = None
    viteza_max = 0
    an_fabricatie = 0
    capacitate_rezervor = 40
    tip_combustibil = "motorina"
    tractiune = "fata"
    serie_sasiu = None
    cutie_viteze = "manuala"
    numar_inmatriculare = None
    consum_viteza_max = None
    consum_interactiv = None

    def __init__(self, marca, model,
                 culoare):  # self reprezinta un placeholder pentru viitorul nume al obiectului care se va instantia
        # model si culoare reprezinta ARGUMENTELE constructorului si ele vor fi considerate obligatorii la momentul instantierii obiectului
        self.model = model  # aici vom atribui atributelor clasei valorile date ca si PARAMETRU in interiorul constructorului
        # in stanga egalului vor fi intotdeauna atributele clasei care vor trebui initializate, iar in dreapta argumentele constructorului care vor fi stocate in atributele clasei
        self.culoare = culoare
        self.marca = marca
        while isinstance(model, (int, float)) == True:  # verific daca inputul de la utilizator este un string
            model = input(
                'Invalid value, please try again.')  # daca nu este string, promptez utilizatorul sa introduca o noua valoare
        if culoare == 'orange':  # verificam daca culoarea data ca si argument in constructor este orange
            self.culoare = 'portocaliu'  # daca este orange, o schimbam in portocaliu pentru ca nu avem culoarea orange in baza de date

    # metode
    def accelerate(self,viteza):  # argumentul self este obligatoriu pentru ca tine loc de numele obiectului care inca nu este definit
        # argumentul viteza este dat ca si parametru si care va fi instantiat diferit in functie de obiectul nostru
        return f'Trebuie sa acceleram cu {viteza} de km'  # avem nevoie de return in cazul asta specific pentru ca mai jos am folosit in print rezultatul functiei

    def paint(self, colour):
        self.culoare = colour

    def start_masina(self):
        print("Start masina")

    def calcul_consum_interactiv(self, viteza):
        for viteza in range(180, 100, 1):
            if viteza <= 180 and viteza > 160:
                self.consum_interactiv = 10
            elif viteza <= 160 and viteza > 120:
                self.consum_interactiv = 7
            elif viteza <= 120 and viteza > 100:
                self.consum_interactiv = 6
            else:
                self.consum_interactiv = 5
        return self.consum_interactiv

    def calcul_consum_max(self):
        if self.viteza_max <= 180 and self.viteza_max > 160:
            self.consum_viteza_max = 10
        elif self.viteza_max <= 160 and self.viteza_max > 120:
            self.consum_viteza_max = 7
        elif self.viteza_max <= 120 and self.viteza_max > 100:
            self.consum_viteza_max = 6
        else:
            self.consum_viteza_max = 5
        return self.consum_viteza_max


"""
instantierea unui obiect se face pe baza numelui clasei
Putem modifica alti parametri, sau chiar pe cei definiti prin constructor, dupa instantiere
IMPORTANT:
Orice atribut sau functie din interiorul clasei se poate accesa DOAR prin intermediul obiectului
"""
instanta_masina_bmw = Masina("BMW", "X5", "orange")  # Am instantiat un obiect al clasei Masina numit instanta_masina1
print(instanta_masina_bmw.culoare)
instanta_masina_bmw.viteza_max = 120
instanta_masina_volkswagen = Masina("Dacia", "Logan", "negru")
instanta_masina_volkswagen.viteza_max = 180
instanta_masina_golf = Masina("Volkswagen", "Golf", "Albastru")
instanta_masina_golf.viteza_max = 180

# instanta_masina_bmw.model = "BMW" # am modificat atributul model si i-am dat valoarea BMW
# instanta_masina_volkswagen.culoare = "Rosu"
# print(instanta_masina_bmw.culoare) # Am accesat culorea definita in interiorul clasei
# print(instanta_masina_volkswagen.culoare)
# print(instanta_masina_volkswagen.model)

# Nota: Putem sa consideram ca numele clasei este tipul de data al unui obiect

# print(instanta_masina1)
# instanta_masina1.culoare = 'Rosu'  # Am modificat culoarea masinii, dar doar pentru prima masina, nu si pentru a doua
# print(f"Culoarea pentru prima masina este {instanta_masina1.culoare}")
# instanta_masina2 = Masina()
# print(f"Culoarea pentru a doua masina este {instanta_masina2.culoare}")
# print(type(instanta_masina1))  #  printeaza valoarea <class '__main__.Masina'>
#
# instanta_masina2.marca = 'Volkswagen'
# instanta_masina1.marca = 'BMW'
# instanta_masina2.model = 'Golf'
# instanta_masina2.viteza = 30
# print(instanta_masina2.viteza)
# print(instanta_masina1.viteza)
#
# print(f"Masina 2 este un {instanta_masina2.marca} {instanta_masina2.model} {instanta_masina2.accelerate(instanta_masina2.viteza)} ")
# instanta_masina1.start_masina()
#
# if __name__ == "__main__":
#     instanta_masina4 = Masina("Golf","Negru")
#     instanta_masina5 = Masina("BMW","orange")
#     print(instanta_masina4.model, instanta_masina4.culoare)
#     print(instanta_masina5.model, instanta_masina5.culoare)

# Calcul consum in functie de viteza in afara clasei
for instanta_masina_bmw.viteza in range(180, 100, 1):
    if instanta_masina_bmw.viteza <= 180 and instanta_masina_bmw.viteza > 160:
        consum = 10
    elif instanta_masina_bmw.viteza <= 160 and instanta_masina_bmw.viteza > 120:
        consum = 7
    elif instanta_masina_bmw.viteza <= 120 and instanta_masina_bmw.viteza > 100:
        consum = 6
    else:
        consum = 5

lista_masini = [instanta_masina_bmw, instanta_masina_volkswagen, instanta_masina_golf]
for masina in lista_masini:
    print(
        f"Masina {masina.model} poate atinge o viteza maxima de  {masina.viteza_max} la care va consuma {masina.calcul_consum_max()}")





"""
Cerinte:

Clasa pisica
Atribute:
- culoare
- rasa
- varsta


Metode:
- miauna
- alearga
- zgarie
- se joaca
- toarce
"""

class Pisica:
    # atribute/campuri
    culoare = None
    rasa = None
    varsta= None
    stare = "chill"

    def miauna(self):
        print("Miau")

    def alearga(self,soarece):
        if(soarece == True):
            print("alearga")

    def zgarie(self,trasa_de_coada):
        if(trasa_de_coada==True):
            print("hhhhhhhhhhzzzzzz")

    def se_joaca(self):
        print("run for your life")

    def toarce(self):
        if self.stare=='chill':
            print("purrrr")

# pisica_katia = Pisica("maro","maidaneza") - returneaza eroare pentru ca in clasa Pisica nu exista constructor cu parametri
pisica_katia = Pisica() #  am creat un obiect cu numele pisica_katia, care reprezinta o instanta a clasei Pisica
pisica_katia.culoare = "maro"
print(pisica_katia.stare) # Am printat pe ecran starea curenta a pisicii
pisica_katia.toarce() #  am apelat metoda toarce prin intermediul obiectului
pisica_katia.stare = "Agitata" # Am schimbat valoarea atributului stare la "Agitata"

"""
Cerinte:

Clasa pisica
Atribute:
- culoare
- rasa
- varsta


Metode:
- miauna
- alearga
- zgarie
- se joaca
- toarce
"""

class Pisica:
    # atribute/campuri
    culoare = None
    rasa = None
    varsta = None
    stare = "chill"
    stare_de_sanatate = "buna"
    inaltime = 1.60

    def __init__(self,culoare,rasa,inaltime):
        self.culoare = culoare
        self.rasa = rasa
        self.inaltime = inaltime

    def miauna(self):
        print("Miau")

    def alearga(self,soarece):
        if(soarece == True):
            print("alearga")

    def zgarie(self,trasa_de_coada):
        if(trasa_de_coada==True):
            print("hhhhhhhhhhzzzzzz")

    def se_joaca(self):
        print("run for your life")

    def toarce(self):
        if self.stare=='chill':
            print("purrrr")
        else:
            print("hsssssssssssss")


pisica_katia = Pisica("maro","maidaneza",30)
pisica_kedi =  Pisica("alba","maidaneza",35)

pisica_katia.toarce()
print(pisica_katia.culoare)
pisica_katia.culoare="rosu"
print(pisica_katia.culoare)
pisica_katia.stare_de_sanatate = "conjuctivita"
print(pisica_kedi.culoare)
print(pisica_kedi) #-> printeaza <__main__.Pisica object at 0x7fa1cbebaf70>
# pisica_kedi = Pisica("negru","maidaneza") -> aici nu se va actualiza obiectul existent, ci se va crea unul nou
# print(pisica_kedi.culoare)
print(pisica_kedi) # printeaza  <__main__.Pisica object at 0x7fa1cbebaee0>

# Vrem sa schimbam starea pisicii din starea chill in starea agitata
pisica_katia.stare = "agitata"
pisica_katia.varsta = 3

pisica_katia.toarce()




# from introduction_to_programming.curs_06 import Masina
# masina1 = Masina("Ford",'Fuchsia')
# print(f"Modelul masinii este {masina1.model} si culoarea masinii este {masina1.culoare}")

class Scoala:
    adresa = None
    nr_clase = 0
    nr_elevi_per_clasa = 0

    def calculeazaNrTotalElevi(self,nr_clase,nr_elevi_sc1):
        nr_total_elevi = nr_clase * nr_elevi_sc1
        return nr_total_elevi

scoala1 = Scoala() # Am instantiat un obiect al clasei scoala care va primi in mod implicit atributele si metodele clasei scoala
print(scoala1.adresa)
scoala1.adresa = "Strada floricelelor nr 64, Ferentexas"
nr_clase_sc1 = int(input("Introdu numarul de clase pentru scoala 1"))
nr_elevi_sc1 = int(input("Introdu numarul de elevi pentru scoala 1"))
# nr_total_studenti = scoala1.calculeazaNrTotalElevi(nr_clase_sc1)
print(f"numarul de clase din scoala 1 este {nr_clase_sc1}")
print(f"numarul total de elevi din scoala 1 este {scoala1.calculeazaNrTotalElevi(nr_clase_sc1,nr_elevi_sc1)}")