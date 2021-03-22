
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
plt.plot([1,2,3,4,5])
plt.show()


# In[4]:


plt.plot([1,2,3,4,5],[2,5,8,12,18],'ro')
plt.show()


# In[5]:


x = range(1,15,1)
y = range(1,42,3)
plt.plot(x,y)
plt.show()


# In[6]:


import matplotlib.pyplot as plt
fig = plt.figure(figsize = (5,3),facecolor = 'yellow')


# In[7]:


import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
df = pd.read_excel('体温.xls')
x = df['日期']
y = df['体温']
plt.plot(x,y,color = 'm',linestyle = '-',marker = 'o',mfc = 'w')
plt.xlabel('2020年2月')
plt.ylabel('基础体温')
plt.show()


# In[8]:


import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
df = pd.read_excel('体温.xls')
x = df['日期']
y = df['体温']
plt.plot(x,y,color = 'm',linestyle = '-',marker = 'o',mfc = 'w')
plt.xlabel('2020年2月')
plt.ylabel('基础体温')
plt.xticks(range(1,15,1)) #设置x的刻度
plt.show()


# In[24]:


import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
df = pd.read_excel('体温.xls')
x = df['日期']
y = df['体温']
plt.plot(x,y,color = 'm',linestyle = '-',marker = 'o',mfc = 'w')
plt.xlabel('2020年2月')
plt.ylabel('基础体温')
dates = ['1日','2日','3日','4日','5日','6日','7日','8日','9日','10日','11日','12日','13日','14日']
plt.xticks(range(1,15,1),dates) 
plt.show()


# In[15]:


import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
df = pd.read_excel('体温.xls')
x = df['日期']
y = df['体温']
plt.plot(x,y,color = 'm',linestyle = '-',marker = 'o',mfc = 'w')
plt.xlabel('2020年2月')
plt.ylabel('基础体温')
# plt.yticks([35.4,35.6,35.8,36.0,36.2,36.4,36.6,36.8,37.0,37.2,37.4,37.6,37.8,38.0])
plt.xticks(range(1,15,1)) #设置x的刻度
plt.xlim(1,14)  # 设置轴的范围
plt.ylim(35,45)
plt.show()


# In[18]:


import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
df = pd.read_excel('体温.xls')
x = df['日期']
y = df['体温']
plt.plot(x,y,color = 'm',linestyle = '-',marker = 'o',mfc = 'w')
plt.xlabel('2020年2月')
plt.ylabel('基础体温')
plt.yticks([35.4,35.6,35.8,36.0,36.2,36.4,36.6,36.8,37.0,37.2,37.4,37.6,37.8,38.0])
plt.xticks(range(1,15,1)) #设置x的刻度
plt.xlim(1,14)  # 设置轴的范围
plt.grid(color = '0.5',linestyle = '--',linewidth = 1)
# plt.ylim(35,45)
plt.show()

