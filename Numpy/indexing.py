# -*- coding: utf-8 -*-
import numpy as np

sayilar=np.array([0,5,10,15,20,25,30])
print(sayilar[::-1])#sayilar dizisini tersten dizer

#print(sayilar[6])
#print(sayilar[0:3])#0. indeksten 3.indekse kadarki sayıları yazar

sayilar2=np.array([[0,5,10],[15,20,25]])
print(sayilar2[1,2])#1.satırın 2.sütununu verir
print(sayilar2[:,2])#bütün satırlardan 2.indeksi verir.
print(sayilar2[:,0:2])#tüm satırların 0.indeksinden 2. indeksine kadar olan sayıları getirir.

print(sayilar2[-1:])#son satırın tüm sütunlarını getirir
print(sayilar2[:,-1])#tüm satırların son sütununu getirir