# -*- coding: utf-8 -*-

import numpy as np

#a=np.arange(1,10)#1 den başlayıp 10 a kadar ki sayılardan dizi oluşturduk

a=np.array([1,3,5,7,9,11])#kendi sayılarımızla bir array oluşturduk
a=a.reshape(2,3)#a yı 2 satır 3 sütunluk ayarladık.a ya atayarak a nın içini değiştirmiş olduk. 
print(a)
print(a.dtype)#a nın içersinde float değer varsa a nın tipi float olur.String değer varsa a nın tipi String olur.
print(a.ndim)#boyut sayısı

b=np.array([[1,3],[5,7],[9,11]])
print(b)
print(b.ndim)