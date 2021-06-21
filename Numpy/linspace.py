# -*- coding: utf-8 -*-
import numpy as np

#a=np.linspace(1,10)#1 ve 10 arasında default değer olarak 50 tane sayı üretir.
a=np.linspace(1,10,5)#1 ve 10 arasında(1 ve 10 dahil) 5 tane eşit aealıklı sayı üretir.
print(a)

from numpy import pi
x=np.linspace(0,2*pi,100)
print(x)
print(np.sin(x))#0 dan 360 dereceye kadar ki sinüs değerlerini hesapladık.
