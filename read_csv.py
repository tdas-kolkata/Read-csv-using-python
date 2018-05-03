import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sc

def conv(sig,fil):
    x=np.shape(sig)[0]
    y=len(fil)
    k=x-y
    res=np.zeros(k)
    for i in range(k):
        res[i]=np.sum(np.multiply(sig[i:i+y],fil))
    return res
        

data1=pd.read_csv('park1.csv',nrows=500,skiprows=1,usecols=[1])
d1=np.array(data1)
data2=pd.read_csv('samples.csv',skiprows=1,nrows=500,usecols=[1])
d2=np.array(data2)

fil=np.random.rand(5)
res1=conv(d1,fil)
res2=conv(d2,fil)


plt.subplot(411)
plt.plot(data1)
plt.subplot(412)
plt.plot(data2)
plt.subplot(413)
plt.plot(res1)
plt.subplot(414)
plt.plot(res2)

plt.show()
