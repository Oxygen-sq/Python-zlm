#!/usr/bin/env python
# coding: utf-8

# # 课堂练习3-17

# # 利用numpy进行统计分析

# ## 2.3.1 读写文件

# ### 代码 2-39 二进制数据储

# In[3]:


import numpy as np


# In[11]:


arry = np.arange(100).reshape(10,10)
np.save("C:/Users/HP/Desktop/test_3_17_2",arry)
print('保存的数组为：\n',arry)


# ### 代码 2-40 多个数组存储

# In[12]:


arry1 = np.array([[1,2,3],[4,5,6]])
arry2 = np.arange(0,1.0,0.1)
np.savez("C:/Users/HP/Desktop/testz_3_17_1",arry1,arry2)
print('保存的数组为：\n',arry1)


# In[13]:


print('保存的数组为：\n',arry2)


# ### 代码2-41 二进制文件读取

# In[14]:


loaded_data = np.load("C:/Users/HP/Desktop/test_3_17_2.npy")
print('读取的数组为：\n',loaded_data)


# In[24]:


loaded_data1 = np.load("C:/Users/HP/Desktop/testz_3_17_1.npz")
print('读取的数组1为：\n',loaded_data1['arr_0'])


# In[25]:


print('u取得数组2为：\n',loaded_data1['arr_1'])


# ### 代码 2-42 文件存储与读取

# In[26]:


arry = np.arange(0,12,0.5).reshape(4,-1)
print('创建的数组为：\n',arry)


# In[27]:


# fmt ="%d"表示保存为整数
np.savetxt("C:/Users/HP/Desktop/test_3_17.txt",arry,fmt="%d",delimiter=",")
#读入的时候也需要指定都好分隔
loaded_data = np.loadtxt("C:/Users/HP/Desktop/test_3_17.txt",delimiter=",")
print('读取的数组为：\n',loaded_data)


# ### 代码2-43 使用genfromtxt函数读取数组

# In[28]:


loaded_data = np.genfromtxt("C:/Users/HP/Desktop/test_3_17.txt",delimiter = ",")
print('读取的数组为：\n',loaded_data)


# #### 代码 2-44 使用sort函数进行排序

# In[29]:


np.random.seed(42)
arry = np.random.randint(1,10,size = 10)
print('创建的数组为:\n',arry)


# In[30]:


arry.sort()
print('排序后的数组为：\n',arry)


# In[32]:


arry1 = np.random.randint(1,10,size = (3,3))
print('创建的数组为：\n',arry1)


# In[33]:


arry1.sort(axis = 1) 
print('排序后的数组为：\n',arry1)


# In[34]:


arry1.sort(axis = 0) 
print('排序后的数组为：\n',arry1)


# #### 代码 2-45 使用argsort函数进行排序

# In[37]:


arry = np.array([2,3,6,8,0,7])
print('创建的数组为：\n',arry)
print('排序后的数组为：\n',arry.argsort())


# #### 代码 2-46 使用lexsort函数进行排序

# In[36]:


a = np.array([3,2,6,4,5])
b = np.array([50,30,40,20,10])
c = np.array([400,300,600,100,200])
d = np.lexsort((a,b,c))
print('排序后的数组为：\n',list(zip(a[d],b[d],c[d])))


# #### 代码 2-47 数组内数据去重

# In[39]:


names = np.array(['小明','小花','小环','小明','小兰','小白'])
print('创建的数组为：\n',names)


# In[41]:


print('去重后的数组为：\n',np.unique(names))


# In[42]:


# 跟np.unique等价的python代码实现过程
print('去重后的数组为：\n',sorted(set(names)))


# In[43]:


ints = np.array([1,2,3,4,5,6,7,8,9,10,4,6,8])
print('创建的数组为：\n',ints)


# In[44]:


print('去重后的数组为：\n',np.unique(ints))


# #### 代码 2-48 使用tile函数实现数据重复

# In[45]:


arry = np.arange(5)
print('创建的数组为：\n',arry)


# In[46]:


print('重复后的数组为：\n',np.tile(arry,3))


# #### 代码 1-49 使用repeat函数实现数据重复

# In[47]:


np.random.seed(42)
arry = np.random.randint(0,10,size = (3,3))
print('创建的数组为：\n',arry)


# In[48]:


print('重复后的数组为：\n',arry.repeat(2,axis = 0))


# In[49]:


print('重复后的数组为：\n',arry.repeat(2,axis = 1))


# #### 代码 2-50 Numpy中常用的统计函数的使用

# In[50]:


arry = np.arange(20).reshape(4,5)
print('创建的数组为：\n',arry)


# In[51]:


print('数组的和为：\n',np.sum(arry))


# In[53]:


print('数组纵轴的和为：\n',arry.sum(axis = 0))


# In[54]:


print('数组横轴的和为：\n',arry.sum(axis = 1))


# In[55]:


print('数组的均值为：\n',np.mean(arry))


# In[56]:


print('数组纵轴的均值为：\n',arry.mean(axis = 0))


# In[57]:


print('数组横轴的均值为：\n',arry.mean(axis = 1))


# In[58]:


print('数组的标准差为：\n',np.std(arry))


# In[59]:


print('数组纵轴的标准差为：\n',arry.std(axis = 0))


# In[60]:


print('数组的方差为：\n',np.var(arry))


# In[62]:


print('数组的最小值为：\n',np.min(arry))


# In[63]:


print('数组的最大值为：\n',np.max(arry))


# In[65]:


print('数组的最小元素的索引为：\n',np.argmin(arry))


# In[66]:


print('数组的最大元素的索引为：\n',np.argmax(arry))


# #### 代码 2-51 cumsum 和 cumprd 函数的使用

# In[68]:


arry = np.arange(2,10)
print('创建的数组为：\n',arry)


# In[69]:


print('数组元素的累计和为：\n',np.cumsum(arry))


# In[70]:


print('数组元素的累计积为：\n',np.cumprod(arry))


# #### 代码 2-52 花萼长度数据统计分析

# In[ ]:




