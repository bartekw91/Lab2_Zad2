a = int(input("Proszę wpisać liczbę:"))
doskonala = 0
i = 1
while i <= a:
    if a % i == 0:
        doskonala += 1
    i+=1
print("Jest {:d} liczb doskonałych dla 1000".format(doskonala))