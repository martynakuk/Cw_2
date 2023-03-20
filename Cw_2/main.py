# Zadanie 1

napis = "Python 23"

zmiennaA = napis
zmiennaB = napis
zmiennaC = napis

# Zadanie 1A
print(zmiennaA.__eq__(zmiennaB))
print(zmiennaB.__eq__(zmiennaC))

# Zadanie 1B
print(type(zmiennaA))
print(zmiennaB.__class__)
print(type(zmiennaC))

print(hex(id(zmiennaA)))
print(hex(id(zmiennaB)))
print(hex(id(zmiennaC)))

zmiennaC = "Java 11"

print(zmiennaA.__eq__(zmiennaB))
print(zmiennaB.__eq__(zmiennaC))

print(type(zmiennaA))
print(zmiennaB.__class__)
print(type(zmiennaC))

print(hex(id(zmiennaA)))
print(hex(id(zmiennaB)))
print(hex(id(zmiennaC)))

# Zadanie 2

print("Napisz 2 liczby")
a = float(input())
b = float(input())

print("Napisz operator")
o = input()

if o.__eq__('+'):
    print(a + b)
elif o.__eq__('-'):
    print(a - b)
elif o.__eq__('*'):
    print(a * b)
elif o.__eq__('/'):
    print(a / b)

# Zadanie 3

print("Pytanie: Jak masz na imię oraz nazwisko?")
name = input()
print("Odpowiedz: ", name)
print("Pytanie: Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie: oglądanie telewizji/filmów/seriali, "
      "czytanie książek/czasopism, słuchanie muzyki ")
czas = input()
print("Odpowiedz: ", czas)
print("Pytanie: W jakich okolicznościach czytasz książki najczęściej? podczas podróży, w czasie wolnym (po pracy, "
      "na urlopie), podczas pracy/nauki (to ich element)")
czyt = input()
print("Odpowiedz: ", czyt)
print("Pytanie: Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru? chęć poszerzenia "
      "wiedzy, czytanie mnie relaksuje/odpręża, fakt, że czytanie jest modne")
abc = input()
print("Odpowiedz: ", abc)


