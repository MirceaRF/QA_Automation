'''
1. Creează-ți cont de github și încarcă într-un repo nou tot ce am facut până
acum la ore.
Curs git/github
VIDEOS 1, 2 si 3
2. Rezolvă exercițiul după ce ai urcat proiectul (tot ce am facut până acum
împreună).
ABSTRACTION
Clasa abstractă FormaGeometrica
Conține un field PI=3.14
Conține o metodă abstractă aria (opțional)
Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai
probabil am colturi’
INHERITANCE
Clasa Pătrat - moștenește FormaGeometrica
constructor pentru latură

ENCAPSULATION
latura este proprietate privată
Implementează getter, setter, deleter pentru latură
Implementează metoda cerută de interfață (opțional, doar dacă ai ales să
implementezi metoda abstractă aria)


Clasa Cerc - moștenește FormaGeometrica
constructor pentru rază
raza este proprietate privată
Implementează getter, setter, deleter pentru rază
Implementează metoda cerută de interfață - în calcul folosește field PI
mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda
abstractă aria)
POLYMORPHISM
Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
Creează un obiect de tip Patrat și joacă-te cu metodele lui
Creează un obiect de tip Cerc și joacă-te cu metodele lui

'''

# ABSTRACTION
from abc import ABC, abstractmethod # avem nevoie de importul acesta pentru abstractizare in python

class FormaGeometrica(ABC):
    PI = 3.14

    @abstractmethod
    def aria(self):
        NotImplementedError
        pass

    print('Metoda abstarcta !')

    @classmethod
    def descrie(self):
        print('Cel mai probabil am colturi')


class Patrat( FormaGeometrica):   # INHERITANCE
    __latura = 30                 #ENCAPSULATION
    def __int__(self, latura):
        self.__latura = latura

    def aria(self):
        print(f'Aria este {(self.__latura**2)}')

    @property
    def latura(self):
        return self.__latura

    @latura.getter
    def latura(self):
        print(f'Getter: Latura este {self.__latura}')
        return self.__latura

    @latura.setter
    def latura(self, latura):
        self.__latura = latura
        print(f'Setter: Noua latura este {latura}')

    @latura.deleter
    def latura(self):
        self.__latura = None
        print(f'Deleter: Am sters latura')


    def descrie(self):
        print('Cel mai probabil am colturi')



class Cerc(FormaGeometrica):
    #__raza = 10

    def __init__(self, raza):
        self.__raza = raza

    def aria(self):
        print(f'Aria este {self.PI*self.__raza**2}')


    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        print(f'Getter: Raza este {self.__raza}')
        return self.__raza

    @raza.setter
    def raza(self, raza_set):
        self.__raza=raza_set
        print(f'Setter: Noua raza este {raza_set}')

    @raza.deleter
    def raza(self):
        self.__raza = None
        print(f'Deleter: Am sters raza')



    def descrie(self):
        print('Eu nu am colturi')


p1=Patrat()
p1.descrie()
p1.aria()
p1.latura
p1.latura=50
p1.aria()
del p1.latura
p1.descrie()

print('-----------------------')

c1=Cerc(10)
c1.aria()
c1.raza
c1.raza=50
del c1.raza

c1.descrie()




'''
3. Actualizează proiectul pe github facand un push la noul cod
În Foldereul de teme ajunge să pui doar linkul cu proiectul tău public
Curs git/github
https://github.com/MirceaRF/QA_Automation/blob/main/intro_IT/Tema_Curs_7-corectata.py
'''