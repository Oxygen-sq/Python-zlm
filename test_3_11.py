#!/usr/bin/env python
# coding: utf-8

# # 附加： 数组转置

# In[1]:


import numpy as np


# In[2]:


n = np.arange(24).reshape(4,6)


# In[3]:


print(n)
print(n.T)


# In[4]:


n = np.array([['A',100],['B',200],['C',300],['D',400],['E',500]])
print(n)
print(n.T)


# In[5]:


n = np.array([['A',100],['B',200],['C',300],['D',400],['E',500]]) #transpose函数实现数组转置
print(n.transpose())


# # 附加：删除数组

# In[6]:


n1 = np.array([[1,2],[3,4],[5,6]])
print(n1)
n2 = np.delete(n1,2,axis = 0)
n3 = np.delete(n1,0,axis = 1)
n4 = np.delete(n1,(1,2),0)
print('删除第三行后的数组：\n',n2)
print('删除第一列后的数组：\n',n3)
print('删除第二行和第三行后的数组：\n',n4)


# # 附加：数组的修改

# In[7]:


n1 = np.array([[1,2],[3,4],[5,6]])
print(n1)
n1[1] = [30,43]
n1[2][1] = 88
print('修改后的数组为：\n',n1)


# # 附加：数组的查询 numpy.where(condition,x,y)

# In[8]:


n1 = np.arange(10)
print(n1)
print(np.where(n1>5,2,0)) #大于5输出2，不大于输出0


# In[9]:


n2 = n1[np.where(n1>5)]
print(n2)


# ## 2.2.1 创建NumPy矩阵

# #### mat函数创建矩阵 (用mat函数创建的矩阵才能进行一些线性代数的操作)

# In[10]:


a = np.mat('5 6;7 8')
b = np.mat([[1,2],[3,4]])
print(a)
print(b)
print(type(a))
print(type(b))
n1 = np.array([[1,2],[3,4]])
print(n1)
print(type(n1))


# ### 代码  2-30

# In[11]:


matr1 = np.mat('1 2 3;4 5 6;7 8 9')
print('创建的矩阵为：\n',matr1)


# In[12]:


matr2 = np.matrix([[1,2,3],[4,5,6],[7,8,9]])
print('创建的矩阵为：\n',matr2)


# In[13]:


data1 = np.mat(np.zeros((3,3))) #创建一个3*3的0矩阵
print(data1)


# In[14]:


data2 = np.mat(np.ones((2,4))) #创建一个2*4的1矩阵
print(data2)


# In[16]:


data3 = np.mat(np.random.rand(3,3))
print(data3)


# In[18]:


data4 = np.mat(np.random.randint(1,8,size = (3,5)))
print(data4)


# ### bmat函数创建矩阵，分块矩阵

# #### 代码 3-31

# In[24]:


matr1 = np.eye(3)
print('创建的矩阵为：\n',matr1)
matr2 = 3*matr1
print('创建的矩阵为：\n',matr2)
print('创建的矩阵为：\n',np.bmat('matr1 matr2;matr2 matr2'))


# ### 矩阵的加法运算

# In[25]:


data1 = np.mat([[1,2],[3,4],[5,6]])
data2 = np.mat([1,2])
print(data1 + data2) #矩阵的加法运算 ppt79页


# ### 矩阵的减法、除法运算

# In[26]:


data1 = np.mat([[1,2],[3,4],[5,6]])
data2 = np.mat([1,2])
print(data1 - data2) #矩阵的加法运算
print(data1 / data2) #矩阵的除法运算 ppt 80页


# ### 矩阵的乘法运算

# In[27]:


data1 = np.mat('1 2;3 4;5 6')
data2 = np.mat('1 2;3 4')
print(data1 * data2) #矩阵的乘法运算


# ### 矩阵元素之间的相乘运算，使用multiply函数

# In[28]:


data1 = np.mat('1 2 3;3 4 5;5 6 7')
data2 = np.mat( '7 7 9;9 7 7 ;9 7 9')
print('矩阵相乘结果为：\n',data1 * data2)
print('矩阵对应元素相乘结果为：\n',np.multiply(data1,data2))


# ### 代码 2-33 查看矩阵的属性

# In[29]:


data1 = np.mat('1 2 3;3 4 5;5 6 7')
print('元矩阵为：\n',data1)
print('矩阵的转置结果为：\n',data1.T)


# In[ ]:




