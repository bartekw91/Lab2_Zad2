import sys as system

system.stdout.write("Wpisz liczbę a:")

a = system.stdin.readline()

if a.find(".") != -1:
    a = float(a)
else:
    a = int(a)

system.stdout.write("Wpisz liczbę b:")

b = system.stdin.readline()

if b.find(".") != -1:
    b = float(b)
else:
    b = int(b)

system.stdout.write("Wpisz liczbę c:")

c = system.stdin.readline()

if c.find(".") != -1:
    c = float(c)
else:
    c = int(c)

wynik = a ** b + c

print(wynik)