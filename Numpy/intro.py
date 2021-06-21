# -*- coding: utf-8 -*-
import numpy as np

#havaDurumu=[[12,21,31],[6,17,18],[11,12,13]]
#print(havaDurumu)

a=np.arange(15).reshape(3,5)#0 dan 15 e kadar sayı üretir.reshapeile 3 satır 5 sütunluk array oluşturur.
print(a)
print(type(a))
print("Dimension Count: "+str(a.ndim))#ndim boyutu verir.a 2 boyutludur

b=np.arange(10)
print(b.shape)#b nin boyutunu verdi(10,)->10 elemanlı tek boyutlu
print(b.ndim)#boyutunu belirtir->1