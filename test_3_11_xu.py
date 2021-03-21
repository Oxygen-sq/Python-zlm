#!/usr/bin/env python
# coding: utf-8

# #### 代码 2-17 生成服从正态分布的随机数

# In[1]:


import numpy as np
print('生成的随机数组为：\n',np.random.randn(10,5))


# #### 代码 2-18 生成给定上下限范围的随机数

# In[6]:


print('生成的限制范围的随机数为：\n',np.random.randint(3,9,size = [3,9]))


# In[ ]:




