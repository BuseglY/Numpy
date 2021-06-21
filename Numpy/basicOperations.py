# -*- coding: utf-8 -*-
import numpy as np
a=np.array([20,30,40,50])
b=np.arange(4)

c=a-b
print(c)
d=b**2
print(d)
e=10*np.sin(a)
print(e)
print(e<7)#boolean değer dizisi döndürür.
print(a*b)#elementwise(element çarpımı) product
print(a@b)#@ matris çarpımını verir.
print(a.dot(b))#bu da matris çarpımını verir.

f=np.ones((2,4))#2 satır 4 sütunluk 1 ler matrisi oluşturduk.
g=np.zeros((2,4))#2 satır 4 sütunluk 0 lar matrisi oluşturduk.
h=np.random.random((2,4))#0 ve 1 arasında 2 satırlık 4 sütunluk array oluşturur.
i=np.sum(b)#b nin içindeki sayıları topladık
print(i) 
j=np.min(b)#b nin en küçük sayısını yazar
k=np.max(h)#h nin en büyük sayısını yazar
print(np.sqrt(b))#b nin kareköklerini yazar