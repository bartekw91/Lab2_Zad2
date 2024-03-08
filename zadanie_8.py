lista = [1, 3.12, 'test']

slownik = {
    lista[0]: 3,
    lista[1]: 2.51,
    lista[2]: 'test1'
}

print("Przed:")
print(slownik)

for i in lista:
    if i in slownik and type(i) is str:
        del slownik[i]

print("\nPo:")
print(slownik)
