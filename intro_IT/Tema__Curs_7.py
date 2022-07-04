'''
1. Creează-ți cont de github și încarcă într-un repo nou tot ce am facut până
acum la ore.
Curs git/github https://bit.ly/3yfFvqL
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
import  math
# ABSTRACTION

class FormaGeometrica:
    PI = 3.14
    def metoda_abstracta_aria(self):
        print('Metoda abstarcta !')
    def descrie(self):
        print('Cel mai probabil am colturi')


class Patrat( FormaGeometrica):   # INHERITANCE
    __latura = 30                 #ENCAPSULATION
    def __int__(self, latura):
         self.__latura = latura

    @property
    def latura(self):
        return self.__latura

    @latura.getter
    def latura(self):
        print(f'Getter: Culoarea este {self.__latura}')
        return self.__latura

    @latura.setter
    def latura(self, latura):
        if latura == 20:
            self.__latura = 30
        else:
            self.__latura = latura
        print(f'Setter: Noua latura este {latura}')

    @latura.deleter
    def latura(self):
        print(f'Deleter: Am sters latura')
        self.__latura = None

class Cerc(FormaGeometrica):
    __raza = 10

    def __init__(self, raza):
        self.__raza = raza

    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        print(f'Getter: Raza este {self.__raza}')
        return self.__raza

    @raza.setter
    def raza(self, raza):
        if raza == 20:
            self.__raza = 10
        else:
            self.__raza = raza
        print(f'Setter: Noua raza este {raza}')

    @raza.deleter
    def raza(self):
        print(f'Deleter: Am sters raza')
        self.__raza = None

    #@abstractmethod  # am folosit un decorator ca sa evidentiem mai bine faptul ca metoda este abstracta
    def metoda_abstracta_aria_cerc(self,raza):
        return math.pi * raza * raza
        #raise NotImplementedError
    print('Metoda abstarcta !')

    def descrie_cerc(self):
        print('Eu nu am colturi')



figura = Patrat()   #TypeError: Can't instantiate abstract class Patrat with abstract method metoda_abstracta_aria
#figura.latura()  #Metoda abstracta
figura.latura
figura.latura=20 # aici nu intra in if nu stiu de ce
del figura.latura
#figura.metoda_abstracta_aria() #TypeError: Can't instantiate abstract class Patrat with abstract method metoda_abstracta_aria
figura.descrie()
#figura.metoda_abstracta_aria() #TypeError: Can't instantiate abstract class Patrat with abstract method metoda_abstracta_aria

figura2 =Cerc(10)
#figura2.raza()  #TypeError: 'int' object is not callable
figura2.raza
figura2.raza = 30
del figura2.raza
figura2.metoda_abstracta_aria_cerc(30) #
figura2.descrie_cerc()
#figura2.metoda_abstracta_aria() #NotImplementedError
#figura2.descrie()

'''
Metoda abstarcta !
Metoda abstarcta !
Getter: Latura este 30
Setter: Noua latura este 20
Deleter: Am sters latura
Cel mai probabil am colturi
Getter: Raza este 10
Setter: Noua raza este 30
Deleter: Am sters raza
Eu nu am colturi

'''


'''
3. Actualizează proiectul pe github facand un push la noul cod
În Foldereul de teme ajunge să pui doar linkul cu proiectul tău public
Curs git/github
'''



