#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print('11670224邱子齡')


# In[ ]:


import numpy as np    
a=np.array([1,1,6,7,0,2,2,4])
a
b=a[2]*a[6]/8
print('{:,.4f}'.format(b))


# In[ ]:


a=np.array([1,1,6,7,0,2,2,4])
c=np.random.randint(31,size=(1,8))
np.dot(a,c.T)


# In[ ]:


e=np.random.uniform(0,1,size=(10,8))
f=np.array(e).max(axis=1)
np.mean(f)
print("{:.2%}".format(np.mean(f)))


# In[ ]:


a=np.array([1,1,6,7,0,2,2,4])
g=np.random.randint(11,size=(1,8))
ra= np.flip(a) #反轉學號
result=0
i = 0
while i < len(a):
    result +=a[i] * ra[i]
    i += 1
result/= 7
print("{:.3f}".format(result))


# In[ ]:




