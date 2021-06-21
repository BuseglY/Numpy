# -*- coding: utf-8 -*-
import numpy as np

a=np.floor(10*np.random.random((3,4)))#floor(zemin) ile kesirli bir sayıyı zemin tam sayısına yuvarlar. Örn: 3.76 yı 3 e yuvarlar.
print(a)
print(a.shape)#boyutunu verir.3 satır 4 sütun
a=a.ravel()#a matrisini tek satırlık arraya dönüştürür.
#ravel atama yapmaz kendimiz atama yapmalıyız.
print(a)
print(a.shape)#12 elemanlı tek boyutlu dizi yaptık
print(a.reshape(2,6))#2 satır 6 sütuna çevirdik.
a=a.reshape(2,6)
print(a)
print(a.T)#transpose->matrisi 90 derece yana çevirerek yazar
print(a.reshape(2,-1))#2 satırlık olacak sütunu elemana göre belirleyecek.

#2 satırlık oluşturduğumuz için elemanların toplamının çift sayı olması lazım yoksa hata verir.
#b=a.resize(6,3)
#print(b)#hata verir
 