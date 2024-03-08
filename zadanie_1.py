slowo = input("Prosze cos wpisac:")
s = 0
d = 0

for i in slowo:
    if i == " " or "\n" or "\t":
        s += 1
if s == 0:
    print("Nie ma żadnego słowa")
else:
    print("Ilość słów w tym wyrazie:{:d}".format(s))