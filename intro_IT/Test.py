# '''numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# lista_neg = []
# for numar in numere:
#     if numar > 0:
#         numar = numar - numar*2
#         #numar = -(abs(numar)) # alta solutie
#     lista_neg.append(numar)
# print(f'Lista a devenit: {lista_neg}')
#
#
#
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# noua_lista =[]
# for i in numere:
#     if i > 0 :
#         i = -i
#         noua_lista.append(i)
# print(f'Lista noua este : {noua_lista}')'''
#
#
# #numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# # print(f'Lista originala este {numere}')
# # swap = 0
# # for i in range(len(numere)) :
# #     for j in range(len(numere) - 1) :
# #         if numere[j] > numere[j + 1]:
# #             swap = numere[j]
# #             numere[j]=numere[j + 1]
# #             numere[j + 1] = swap
# # print(f'Lista ordonata este {numere}')
# #
#
# # nr = int(input("Scrie un numar: "))
# # i = 1
# # while i <= nr:
# #     print(' ')
# #     for j in range(i):
# #         j = i
# #         print(j, end='')
# #         j = j + 1
# #     i = i + 1
#
#
# # def lista():
# #     x = []
# #     for i in x:
# #         if i >=0:
# #             return x
# # x = int(input('Introduceti lista de numere:'))
# # print('Lista cu numere pozitive este:',lista())
# import math
#
# nums = [34, 1, 0, -23, 12, -88]
#
# for pos_nums in nums:
#    if pos_nums > 0:
#       print(pos_nums)
# print("Original numbers in the list: ",nums)
# print("Positive numbers in the said list:",pos_nums)
#
#
# a=[2,-4,6,-10,22,34]
# b = [i for i in a if i>= 0]
# print(b)
#
#
# pozitive = []
# def lista_numere(lista):
#     for n in lista:
#         if lista[lista.index(n)] > 0:
#             pozitive.append(n)
#         else:
#             pass
#     return pozitive
# print(lista_numere(lista=[7,-2,3,6,-1,-3]))
#
#
# '''9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
# ● Primul număr x este mai mare decat al doilea nr y
# ● Al doilea nr y este mai mare decat primul nr x
# ● Numerele sunt egale.'''
#
# def comparatie(x,y):
#     if x>y:
#         print(f'Primul numar {x} este mai mare decat {y}')
#     elif x<y:
#         print(f'Al doi-lea numar {y} este mai mare decat {x}')
#     else:
#         print('Numerele sunt egale')
# comparatie(7,2)
#
# '''10. Funcție care primește un număr și un set de numere.
# ● Printeaza ‘am adaugat numărul nou în set’ + returnează True
# ● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
# returnează False'''
#
# def seturi(n,set):
#     if n not in set:
#         set.add(n)
#         print('Am adaugat numarul nou in set',set)
#         return True
#     elif n in set:
#         print('Numarul exista deja in set', set)
#         return False
# print(seturi(7,{2,3}))
#
# '''___________________________O-P-T-I-O-N-A-L-E___________________________'''
#
# '''1. Funcție care primește o lună din an și returnează câte zile are acea luna'''
#
# from datetime import date
# def data(month):
#     data1 = date(2022,month,1)
#     data2 = date(2022,month+1,1)
#     rezultat = data2-data1
#     return rezultat.days
# print('zile:',data(month=6))
#
# ''''''
#
# #print('Mc'Donalds')
# prop='Ana are mere'
# print(prop[4:9])
#
#
# def suma(a,b):
#     suma=a+b
#     return suma
# #num1=int(input("Introduceti primul numar: "))
# #num2=int(input("Introduceti al doilea numar :"))
# #print("Suma celor doua numere este",suma(num1,num2))  #am apelat functia
# #print(suma(2,1232320))
# suma(2,3)
import math


def find_Diameter(radius):
    return 2 * radius

def find_Circumference(radius):
    return 2 * math.pi * radius

def find_Area(radius):
    return math.pi * radius * radius

r = float(input(' Please Enter the radius of a circle: '))

diameter = find_Diameter(r)
circumference = find_Circumference(r)
area = find_Area(r)

print("  Diameter Of a Circle = %.2f" %diameter)
print(" Circumference Of a Circle = %.2f" %circumference)
print(" Area Of a Circle = %.2f" %area)


# def diametru_Cerc(self,raza=5):
#     return 2 * raza
#
#
# def circumferinta_Cerc(self, raza=5):
#     return 2 * math.pi * raza
#
#
# def aria_Cerc(self, raza=5):
#     return math.pi * raza * raza
#
#
# #raza = float(input(' Introdu raza cercului: '))
#
# diametru = diametru_Cerc()
# circumferinta = circumferinta_Cerc()
# aria = aria_Cerc()
#
# #print("\n Diameter Of a Circle = %.2f" % diametru)
# print(" Circumference Of a Circle = %.2f" % circumferinta)
# print(" Area Of a Circle = %.2f" % aria)

class Cont:
    # atribute/fields
    iban = None
    titular_cont = None
    sold = None

    # constructor
    def init(self, iban, titular_cont, sold):
         self.iban = iban
         self.titular_cont = titular_cont
         self.sold = sold

    # metode
    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei')

    def debitare_cont(self, suma):
        # print(f'Contul {self.iban} se debiteaza cu suma de {suma}')
        # print(f'Noul sold este {self.sold-suma}')
        self.sold = self.sold - suma
    def creditare_cont(self, suma):
        # print(f'Contul {self.iban} se crediteaza cu suma de {suma}')
        # print(f'Noul sold este {self.sold + suma}')
        self.sold = self.sold + suma

cont1 = Cont()
cont1.afisare_sold()
cont1.debitare_cont(500)
cont1.afisare_sold()
cont1.creditare_cont(1000)
cont1.afisare_sold()
