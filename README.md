# PRAKTIKUM
### STRUKTUR KONDIRI DAN PERULANGAN

**Latihan 1**\
Program menentukan bilangan terbesar dari 2 bilangan yang di input user / runtime.
\
\
Code : 
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

\
\
\
**Latihan 2**

