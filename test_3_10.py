#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np  #导入Numpy库
arry1 = np.array([1,2,3,4]) #创建一个一维数组
print('创建的数组为：',arry1)


# In[2]:


#创建二维数组
arry2 = np.array([[1,2,3,4],[4,5,6,7],[7,8,9,10]])
print('创建的数组为：\n',arry2)


# In[3]:


print('数组维度为：',arry2.shape) #查看数组结构


# In[4]:


print('数组类型为：',arry2.dtype) #查看数组类型


# In[5]:


print('数组元素的个数为：',arry2.size) #查看数组元素个数


# In[6]:


print('数组每个元素的大小为：',arry2.itemsize) #查看数组每个元素大小


# ### 代码2-2 重新设置shape的属性

# In[7]:


arry2.shape = 4,3 #重新设置shape
print('重新设置shape属性后的arry2为：\n',arry2)


# ### 代码2-3 使用arange函数创建数组

# In[8]:


print('使用arange函数创建的数组为：\n',np.arange(0,1,0.1))


# ### 代码2-4 使用linspace函数创建数组

# In[9]:


print('使用linspace函数创建的数组为:\n',np.linspace(0,1,12))


# ### 代码2-5 使用logspace函数创建数组 (等比数列)

# In[10]:


print('使用logspace函数创的建数组为：\n',np.logspace(0,2,20))


# ### 代码2-6 使用zeros函数创建数组

# In[11]:


print(' 使用zeros函数创建的数组为：\n',np.zeros((2,3)))


# ### 代码2-7 使用eye函数创建数组

# In[12]:


print(' 使用eye函数创建的数组为：\n',np.eye(3))


# ### 代码2-8 使用diag函数创建函数

# In[13]:


print('使用diag函数创建函数为：\n',np.diag([1,2,3,4]))


# ### 代码2-9 使用ones函数创建数组

# In[14]:


print('使用ones函数创建数组为：\n',np.ones((5,3)))


# ## 3.数组数据类型

# ### 代码2-10 数组数据类型转换

# In[15]:


print('转换结果：',np.float64(42)) #整型转换为浮点型


# ### 代码2-11 创建数据类型

# In[16]:


df = np.dtype([("name",np.str,40),("numitems",np.int64),("price",np.float64)])
print('数据类型为：\n',df)


# ### 代码2-12 查看数据类型

# In[17]:


print('数据类型为：',df["name"])


# ### 代码2-13 自定义数组数据

# In[18]:


itemz = np.array([("tomatos",42,4.14),("cabbages",13,1.72)],dtype = df)
print('自定义数据为：',itemz)


# ## 2.1.2 生成随机数

# ### 代码2-14 生成随机数

# In[21]:


print('生成的随机数组为：\n',np.random.random(97))


# ### 代码2-15 生成服从均匀分布的随机数组

# In[22]:


print('生成的随机数组为：\n',np.random.rand(10,5))


# ### 代码2-16 生成服从正态分布的随机数

# In[23]:


print('生成的随机数组为：\n',np.random.randn(10,5))


# In[ ]:




