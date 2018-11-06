
# coding: utf-8

# In[1]:


import os
cwd = os.getcwd()
cwd


# In[2]:


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
img=mpimg.imread('sunflower.jpg')
get_ipython().run_line_magic('matplotlib', 'inline')

plt.subplot(20,20,4)


# In[3]:



plt.subplot(1,2,2),plt.imshow(255-img)         #  inverse burada ; 255-I 


# In[4]:


def my_histogram(image):
    
    my_H_R={}
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if(image[i,j,0] in my_H_R.keys()):
                my_H_R[image[i,j,0]]+=1
            else:
                my_H_R[image[i,j,0]]=1
    
    my_H_G={}
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if(image[i,j,1] in my_H_G.keys()):
                my_H_G[image[i,j,1]]+=1
            else:
                my_H_G[image[i,j,1]]=1
    my_H_B={}
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if(image[i,j,2] in my_H_B.keys()):
                my_H_B[image[i,j,2]]+=1
            else:
                my_H_B[image[i,j,2]]=1
    return (my_H_R,my_H_G,my_H_B)
                
        


# In[5]:


my_histogram=my_histogram(img)


# In[6]:


x=[]
y=[]
for i in my_histogram[0].keys():
    x.append(i)
    y.append(my_histogram[0][i])
plt.subplot(1,3,1),plt.plot(x,y)    

x=[]
y=[]
for i in my_histogram[1].keys():
    x.append(i)
    y.append(my_histogram[1][i])
plt.subplot(1,3,2),plt.plot(x,y)
x=[]
y=[]

for i in my_histogram[2].keys():
    x.append(i)
    y.append(my_histogram[2][i])
plt.subplot(1,3,3),plt.plot(x,y)


# In[7]:


mean=sum(img)/len(img)
mean


# In[8]:


def my_mean(image,c=0):
    s_R=0
    m=image.shape[0]
    n=image.shape[1]
    for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                s_R=s_R+image[i,j,c]
    return s_R/(m*n)


# In[9]:


my_mean(img,2)

