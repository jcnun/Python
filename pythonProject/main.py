import math
import collections
import itertools
import glob
import numpy as np
import random as rd
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt


# YOUR CODE HERE
s1=np.array([])
s2=np.array([])

for j in range(1000):
    l1=np.array([])
    l2=np.array([])
    for i in range(10):
        zz=np.random.normal(loc=200,scale=10,size=10)
        vA,vB=vars(zz)
        l1=np.append(l1,[vA])
        l2=np.append(l2,[vB])
    d1=np.average(l1)
    d2=np.average(l2)
    s1=np.append(s1,[d1])
    s2=np.append(s2,[d2])
plt.plot(range(1000),s1,label='Varianz',c='green')
plt.plot(range(1000),s2,label="Stichprobe",c='violet')
plt.plot(range(1000),[100]*1000,label="Varianz",c='blue')
plt.grid()
plt.legend()
plt.xlabel('Versuch')
plt.ylabel('Durchschnittswerte')
plt.title('Varianzen')
plt.show()