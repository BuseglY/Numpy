# -*- coding: utf-8 -*-
import numpy as np

a=np.arange(10)#10 tane elemandan oluşan dizi oluşturduk
print(a)

b=a
print(a[2])
print(b[2])

b[0]=100#referans ataması yaptık.
print(a)#a nın da 0.indeksteki elemanı 100 olur. array ler referans değerlerdir.
print(b)

c=a.copy()
print(c)
c[0]=500#burada referans ataması olmadı çünkü kopyası üzerinde çalıştık.
print(a)
print(c)

d=a.view()#view de kopyaya atanan değer de değişir, kopyaladığı değişkenin değeri de değişir.
print("*****")
print(a)
print(d)
d[0]=250
print(a)
print(b)
d.shape=2,5
print(a)#tek satırlık 10 elemanlı dizi
print(d)#2 satır, 5 sütunluk matris
#view ile a nın boyutları değişmez sadece d nin boyutları değişir
a[0]=123
print(a)
print(d)