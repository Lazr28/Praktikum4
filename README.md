# PRAKTIKUM
## STRUKTUR KONDIRI DAN PERULANGAN

**Latihan 1**
-
Program menentukan bilangan terbesar dari 2 bilangan yang di input user / runtime.
### Code : 
```python
a = input("Masukan Bilangan pertama : ")
b = input("Masukan Bilangan kedua : ")

if a > b :
    print("Bilangan Pertama lebih besar dari bilangan kedua ({0} > {1})".format(a,b))
elif a == b :
    print("Bilangan pertama dan kedua sama")
else:
    print("Bilangan Pertama lebih kecil dari bilangan kedua ({0} > {1})".format(a,b))

```
>**Penjelasan**\
pada kode program di atas.\
pertama tama kita membuat variabel yang menampung input bilangan dari keyboard / user.\
lalu kita buat kondisi menggunakan `if`\
 kondisi pertama akan mengecek apakah nilai dari variabel `a` lebih besar dari variabel `b`\
 kondisi kedua mengecek apakah `a` dan `b` memiliki nilai yang sama.\
 jika kedua kondisi di atas tidak ada yang sesuai / `true` maka akan menjalankan sintak yang ada didalam `else`

### Output
![Screenshot Output 1](/Image/Output-1-1.png)
\
\
\
**Latihan 2**
-
Program mengurutkan 3 buah bilangan dari inputan user.

### Code :
```python
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
```
>**Penjelasan**\
Pada kode program diatas.\
kita menampung 3 buah bilangan yang akan di input user.\
lalu kita menampilkan " urutan Bilangan : " tanpa pindah baris.
setelah itu membuat kondisi `if elif`
jika variabel `a` lebih kecil dari `b` dan `b` lebih kecil dari `c`
akan menampilkan langsung dengan urutan `a, b, c`
lalu jika kondisi pertama tidak seusai, maka akan melakukan kondisi seterusnya dengan output sesuai kondisi yang ada.

### Output
![Screenshot Output 2](/Image/Output-1-2.png)
\
\
\
## Perulangan

**Latihan 1**