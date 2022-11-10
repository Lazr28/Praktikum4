import random
n = input("Masukan Jumlah N : ")
n = int(n)
for i in range(n) :
    a = random.random()
    while (a > 0.5) :
        a =random.random()
    print(a)
        