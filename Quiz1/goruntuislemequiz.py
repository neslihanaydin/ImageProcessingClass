
# coding: utf-8

# In[16]:


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


# In[39]:


def get_distance(v, w= [1/3, 1/3, 1/3]):
    a,b,c = v[0],v[1],v[2]
    w1,w2,w3 = w[0],w[1],w[2]
    d = ((a**2)*w1+(b**2)*w2+(c**2)*w3)**.5
    return d


# In[40]:


def convert_rgb_to_gray_level(im_1):
    m = im_1.shape[0]
    n = im_1.shape[1]
    im_2 = np.zeros((m,n))
    for i in range (m):
        for j in range(n):
            im_2[i,j] = get_distance(im_1[i,j,:])
    return im_2


# In[47]:


def convert_gray_level_to_bw(image_gray_level):
    m = image_gray_level.shape[0]
    n = image_gray_level.shape[1]
    im_bw = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            if image_gray_level[i,j]>120:
                im_bw[i,j] = 1
            else:
                im_bw[i,j] = 0
    return im_bw


# In[48]:


im_1 = mpimg.imread('sunflower.jpg')
im_2 = convert_rgb_to_gray_level(im_1)
im_3 = convert_gray_level_to_bw(im_2)
get_ipython().run_line_magic('matplotlib', 'inline')
plt.subplot(1,3,1),plt.imshow(im_1)
plt.subplot(1,3,2),plt.imshow(im_2,cmap='gray')
plt.subplot(1,3,3),plt.imshow(im_3,cmap='gray')



# In[33]:


def soru_iki(img):
    m = img.shape[0]
    n = img.shape[1]
    my_hash = {}
    sayac = 0
    for i in range(m):
        for j in range(n):
            if(img[i][j] == 1. ):
                sayac = sayac +1
                
    sonuc = sayac/(m*n)
    
    if ( sonuc ):
        for i in range(m):
            for j in range(n):
                if(img[i][j] == 1.):
                    ifade = (str(i)+","+str(j))
                    my_hash[ifade] = 1.
    print(img)
    print(my_hash)


# In[34]:


soru_iki(im_3)

