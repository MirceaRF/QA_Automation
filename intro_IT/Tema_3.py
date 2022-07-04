'''
1. Declară o listă note_muzicale în care să pui do re mi etc până la do
Afișeaz-o:
● Inversează ordinea folosind slicing și suprascrie această listă.
● Printează varianta actuală (inversată).
● Pe această listă aplică o metodă care bănuiești că face același lucru,
adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz,
deoarece metoda face asta automat.
● Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta
inițială.
Concluzii: slicing e temporar, dacă vrei să păstrezi noua variantă va trebui să
suprascrii lista sau să o salvezi într-o listă nouă. Metoda găsită de tine face

suprascrierea automat și permanentizează aceste modificări. Ambele variante
își găsesc utilitatea în funcție de ce ne dorim în acel moment.

'''

note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(note_muzicale)
print(note_muzicale[::-1])
print(('---------------'))
note_muzicale_2 = note_muzicale[::-1]
print(note_muzicale_2)
print(('---------------'))
note_muzicale_2.reverse()
print(note_muzicale_2)

print(('---------------'))

'''
2. De câte ori apare ‘do’?
'''

print(note_muzicale.count('do'))

print(('---------------'))

'''
3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
Găseste 2 variante să le unești într-o singură listă.
'''

list_1 = [3, 1, 0, 2]
list_2 = [6, 5, 4]
# print(list_1+list_2)

list_3 = list_1 + list_2
print(list_3)

print(('---------------'))
list_1 = [3, 1, 0, 2]
list_2 = [6, 5, 4]
for i in list_2:
    list_1.append(i)
print(list_1)

print(('---------------'))

list_1 = [3, 1, 0, 2]
list_2 = [6, 5, 4]
list_1.extend(list_2)
print(list_1)

print(('---------------'))

list_1 = [3, 1, 0, 2]
list_2 = [6, 5, 4]
import itertools
list_3 = list(itertools.chain(list_1, list_2))
print(list_3)

'''
4.
● Sortează și afișază lista generată la exercițiul anterior.
● Sortează numărul 0 folosind o funcție.
● Afișaza iar lista.
'''

list_3 = [3, 1, 0, 2, 6, 5, 4]
print(f"Vreau sa accesez numarul 0 si il voi gasi la indexul {list_3.index(0)}")
print(list_3)

print(('---------------'))

'''
5. Folosind un if verifică lista generată la exercițiul 3 și afișază:
● Lista este goală.
● Lista nu este goală.

'''

list_3 = [3, 1, 0, 2, 6, 5, 4]
if not list_3 :
    print('Lista este goala')
if list_3:
    print('Lista nu este goala ')

print(('---------------'))


'''
6. Folosește o funcție care să șteargă lista de la exercițiul 3.
'''

list_1 = [3, 1, 0, 2]
list_2 = [6, 5, 4]
list_3 = list_1 + list_2
print(list_3)
del list_3[:]
print(f'Lista 3 este goala:',list_3)

'''
7. Copy paste la exercițiul 5. Verifică încă o dată.
Acum ar trebui să se afișeze că lista e goală.
'''


if not list_3 :
    print('Lista este goala')
if list_3:
    print('Lista nu este goala ')

print(('---------------'))

'''
8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
Folosește o funcție că să afișezi Elevii (cheile)
'''

dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
print(dict1.keys())

print(('---------------'))
'''
9. Printează cei 3 elevi și notele lor
Ex: ‘Ana a luat nota {x}’
Doar nota o vei lua folosindu-te de cheie
'''
print(dict1.get('Ana'))
print('Ana a luat nota ',dict1.get('Ana'))

'''
10. Dorel a făcut contestație și a primit 6
● Modifică nota lui Dorel în 6
● Printează nota după modificare
'''
dict1['Dorel']= 6
print(dict1)
#sau
dict1.update({'Dorel': 6})
print(dict1)
print('Dorel a luat nota ',dict1.get('Dorel'))

'''
11. Gigel se transferă din clasă
● Căuta o funcție care să îl șteargă
● Vine un coleg nou. Adaugă Ionică, cu nota 9
● Printează noii elevi
'''
dict1.pop('Gigel')
print(dict1)

dict1['Ionica'] = 9
print(dict1)

'''
12.
Set
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
● Adaugă în zilele_sapt ‘luni’
● Afișeaza zile_sapt
'''

zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}

zile_sapt_1 = zile_sapt
zile_sapt.add('luni')
zile_sapt_2 = zile_sapt
print(zile_sapt_1,zile_sapt_2)

if zile_sapt_1 == zile_sapt_2:  # Am verificat daca valoarea setului inainte si dupa modificare este aceeasi
    print("Ai adaugat un duplicat")

'''
13.Folosește un if și verifică dacă:
● Weekend este un subset al zilelor din săptămânii.
● Weekend nu este un subset al zilelor din săptămânii.
'''

zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
#if weekend in zile_sapt:
 #   print('Weekend este un subset al zilelor din saptamana')


print(('---------------'))

if weekend.issubset(zile_sapt):
    print('Weekend este un subset al zilelor din saptamana')
else:
    print('Weekend nu este un subset al zilelor din saptamana')
if not weekend.issubset(zile_sapt):
    print('Weekend nu este un subset al zilelor din saptamana')


print(('---------------'))
'''
14. Afișează diferențele dintre aceste 2 seturi.
'''

print (zile_sapt.difference(weekend))

print (zile_sapt-weekend)
print(weekend-zile_sapt)

'''
15. Afișază intersecția elementelor din aceste 2 seturi.
'''
print(zile_sapt.intersection(weekend))

print(('---------------------------------------------'))

'''
Exerciții Opționale - grad de dificultate: Mediu spre greu(may need google) .
1. Ne imaginăm o echipă de fotbal pt teren sintetic.
3 Schimbări maxime admise:

● Declară o Listă cu 5 jucători
● Schimbari_efectuate = te joci tu cu valori diferite
● Schimbari_max = 3
Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
- Efectuează schimbarea
- Șterge jucătorul scos din listă
- Adaugă jucătorul intrat
- Afișaza a intra x, a ieșit y, mai ai z schimbări
Dacă jucătorul nu e în teren:
- Afișază ‘ nu se poate efectua schimbarea deoarece jucătorul x nu e în
teren’
- Afișază ‘mai ai z schimbări’
Testează codul cu diferite valori

Google search hint
“how to check if item îs în list python”
'''

jucatori = ['Gigel','Ionel','Costel','Vasi','Dorel']
#rezerva = ['Marian','Alex','Steli']
schimbari_max_admise = 3
schimbari_max = 3
schimbari_efectuate =0

print('Echipa este ',jucatori)
if schimbari_efectuate <= 3  or schimbari_efectuate >= schimbari_max:
    iesire = input('Scoate un jucator:')
    intrare =input('Baga o rezerva')
    if ('Gigel' in iesire or 'Ionel' in iesire or 'Costel' in iesire or 'Vasi' in iesire or 'Dorel' in iesire):
        schimbari_max_admise = schimbari_max_admise -1
        schimbari_efectuate = schimbari_max_admise
        jucatori.remove(iesire)
        jucatori.append(intrare)
        print(f'A intrat {intrare} a ieșit {iesire} mai ai {schimbari_efectuate} schimbări')
        print(f'Noua lista de jucatori {jucatori}')
    else:
        schimbari_max_admise = schimbari_max_admise -1
        schimbari_efectuate = schimbari_max_admise
        print(f'Nu se poate efectua schimbarea deoarece jucătorul {iesire} nu e în teren')
        print(f'Mai ai {schimbari_efectuate} schimbari')
else:
    schimbari_max_admise =schimbari_max_admise -1
    schimbari_efectuate = schimbari_max_admise
    print('Nu sunt schimbari disponibile')
