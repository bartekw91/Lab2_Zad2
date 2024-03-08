count = 0
size = 10
lista = []

while count < size:
    cyfra = int(input())
    if cyfra % 2 == 0:
        lista.append(cyfra)
    count += 1

print("\nOto lista zawierająca tylko liczby parzyste:")

for i in lista:
    print(i)