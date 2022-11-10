print("Program mengurutkan data berdasarkan input sejumlah data")
b1 = int(input("Bilangan ke-1 : "))
b2 = int(input("Bilangan ke-2 : "))
b3 = int(input("Bilangan ke-3 : "))
##bilangan = [b1,b2,b3]
##bilangan.sort()
print("Urutan Bilangan :", end=" ")
##print(bilangan)
if b1 < b2 < b3 :
    print(b1, b2, b3)
elif b1 < b3 < b2 :
    print(b1, b3, b2)
elif b2 < b3 < b1:
    print(b3, b2, b1)
elif b2 < b1 < b3 :
    print(b2, b1, b3)
elif b3 < b1 < b2 :
    print(b3, b1, b2)
elif b3 < b2 < b1 :
    print(b3, b2, b1)


print("----------------------")
print("lets simplyfy it")
if b1 > b2:
    print(b1, " > " , b2)
    b1,b2 = b2,b1
    print("isi variabel di tukar b1 = ", b1, "b2 = ", b2)
if b1 > b3:
    print(b1, " > " , b3)
    b1,b3 = b3,b1
    print("isi variabel di tukar", b1,b3)
if b2 > b3:
    print(b2, " > " , b3)
    b2,b3 = b3,b2
print ("di simpel kan", b1, b2,b3)