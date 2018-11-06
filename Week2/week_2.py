
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
img=mpimg.imread('sunflower.jpg')
get_ipython().run_line_magic('matplotlib', 'inline')
plt.imshow(img)


# In[2]:


img.shape


# In[3]:


img.ndim,img.shape
plt.imshow(-img)


# In[4]:


def my_function_1(my_img):
    
    print("eksen sayısı : ",my_img.ndim)
    print(" eksen değerleri : ",my_img.shape)
    
    print(" en küçük kırmızı renk değeri : ",np.min(my_img[:,:,0]))
    print(" en büyük kırmızı renk değeri : ",np.max(my_img[:,:,0]))
    
    print(" en küçük yeşil renk değeri : ",np.min(my_img[:,:,1]))
    print(" en büyük yeşil renk değeri : ",np.max(my_img[:,:,1]))
    
    print(" en küçük mavi renk değeri : ",np.min(my_img[:,:,2]))
    print(" en büyük mavi renk değeri : ",np.max(my_img[:,:,2]))
    


# In[5]:


my_function_1(img)

