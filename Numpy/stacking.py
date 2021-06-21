# -*- coding: utf-8 -*-
import numpy as np

a=np.floor(10*np.random.random((2,3)))
b=np.floor(10*np.random.random((2,3)))
print(a)
print(b)
print("******")
c=np.vstack((a,b))#vstack(vertical-dikey)->a ve b  yi yan yana dikey halde getirir
print(c)

d=np.hstack((a,b))#hstack(horizontal-yatay)->a ve b yi alt alta yatay olarak birleştirir
print(d)

