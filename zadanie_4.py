a = int(input("Proszę wpisać liczbę:"))
counter = 0
i = 1
if a == 1:
    print("Liczba nie jest liczbą pierwszą")
else:

    while i <= a:
        if a % i == 0:
            counter += 1
        i+=1

    if counter <= 2:
        print("Liczba jest liczbą pierwszą")
    else:
        print("Liczba nie jest liczbą pierwszą")
