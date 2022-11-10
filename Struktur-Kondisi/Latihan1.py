# Program menentukan bilangan terbesar dari 2 bilangan yang di input user
a = input("Masukan Bilangan pertama : ")
b = input("Masukan Bilangan kedua : ")

if a > b :
    print("Bilangan Pertama lebih besar dari bilangan kedua ({0} > {1})".format(a,b))
elif a == b :
    print("Bilangan pertama dan kedua sama")
else:
    print("Bilangan Pertama lebih kecil dari bilangan kedua ({0} > {1})".format(a,b))
