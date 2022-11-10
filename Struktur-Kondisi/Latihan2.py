print("Program mengurutkan data berdasarkan input sejumlah data")
a, b, c = (int(input("Bilangan ke-1 : ")),
           int(input("Bilangan ke-2 : ")),
           int(input("Bilangan ke-3 : "))
           )
print("Urutan Bilangan :", end=" ")

if a < b < c:
    print(a, b, c)
elif a < c < b:
    print(a, c, b)
elif b < c < a:
    print(c, b, a)
elif b < a < c:
    print(b, a, c)
elif c < a < b:
    print(c, a, b)
elif c < b < a:
    print(c, b, a)
