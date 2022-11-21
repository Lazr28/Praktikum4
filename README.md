# PRAKTIKUM 4
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
![Screenshot Output 1](/Praktikum4/Image/Output-1-2.png)
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

**Latihan 1**\
Program perulangan bertingkat (nested) for.\
\
### Code :
```python
start = 0;
stop = 10;
for i in range(10):
    for j in range(start,stop):
        print(j, sep="  ", end=" ")
        if j < 10 :
            print('{0:>2}'.format(""), end="")
        else :
            print('{0:>1}'.format(""), end="")
    start+=1
    stop+=1
    print("")
```
>**Penjelasan**\
Pada kode program diatas.\
kita membuat variable `start` dan `stop` dulu untuk menampung angka pertama dan terakhir dari sintaks range yang akan di tambah seiring perulangan `for` nya.\
pertama kita buat for dengan pengulangan 10x\
lalu didalamnya (nested) kita buat `for` kembali dengan melakukan print Range dengan parameter `start` dan `stop` nya menggunakan variabel yang sudah kita deklarasikan di awal.
setelah itu gunakan kondisi if `j` kurang dari 10 maka akan menambahkan padding 2, sedangkan jika `j` tidak sesuai kondisi ( `else` ) atau `j` lebih dari sama dengan 10 maka padding yang digunakan hanya 1.\
\
`if` di atas digunakan untuk menentukan banyaknya padding yang akan di gunakan.
\
setelah itu kita tambahkan variabel `start` dan `stop` dengan 1. ( increment 1)\
lalu tambahkan `print("")` agar setah print angka stop akan pindah baris.\


### Output : 
![Output 2-1](/Image/Output-2-1.png)

**Latihan 2**\
Program menampilkan Angka acak dibawah 0.5 sebanyak N ( N ditentukan oleh user ).

### Code :
```python
import random
n = input("Masukan Jumlah N : ")
n = int(n)
for i in range(n) :
    a = random.random()
    while (a > 0.5) :
        a =random.random()
    print(a)  
```
>**Penjelasan**\
Pada kode diatas.\
pertama tama kita import lib `random`
lalu kita buat variabel `n` dengan isi berasal dari inputan user.\
setelah itu kita buat perulangan `for` dengan banyak perulangan sebanyak n.\
lalu masukan angka random ke dalam variabel `a`\
setelah itu kita cek menggunakan `while` jika variabel `a` berisi lebih dari 0.5\
kita akan mengubah variabel tersebut dengan angka random kembali.
setelah itu kita print variabel `a` jika sudah di dapat nilai kurang dari 0.5

### Output : 
![Output 2-2](/Image/Output-2-2.png)
\
