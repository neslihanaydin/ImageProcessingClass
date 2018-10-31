
# coding: utf-8

# In[185]:

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import numpy.core.defchararray as npd


# In[ ]:

def get_distance(v, w= [1/3, 1/3, 1/3]):
    a,b,c = v[0],v[1],v[2]
    w1,w2,w3 = w[0],w[1],w[2]
    d = ((a**2)*w1+(b**2)*w2+(c**2)*w3)**.5
    return d


# In[194]:

def convert_rgb_to_gray_level(im_1):
    m = im_1.shape[0]
    n = im_1.shape[1]
    im_2 = np.zeros((m,n))
    for i in range (m):
        for j in range(n):
            im_2[i,j] = get_distance(im_1[i,j,:])
    return im_2


# In[187]:

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


# In[205]:

def piksel_compare1(img_1,i,j):#dis kenar fonksiyon, external
    a=b=c=d = False
    e = 0
    s = 0
    im_block = img_1[i:i+2, j:j+2]
    im_block = im_block.reshape(1,4)
    im_block.shape
    
    for i in range(4):
        if(im_block[0,i] == 0):
            s = s+2**i
    if s == 8 or s == 4 or s == 2 or s == 1:
        return True
    else:
        return False
    


# In[206]:

def piksel_compare2(img_1,i,j):#dis kenar fonksiyon, internal
    a=b=c=d = False
    e = 0
    s = 0
    im_block = img_1[i:i+2, j:j+2]
    im_block = im_block.reshape(1,4)
    im_block.shape
    
    for i in range(4):
        if(im_block[0,i] == 1):
            s = s+2**i
    if s == 8 or s == 4 or s == 2 or s == 1:
        return True
    else:
        return False
    


# In[207]:

#masks of external
m1 = [[1,1],[1,0]]
m2 = [[1,1],[0,1]]
m3 = [[1,0],[1,1]]
m4 = [[0,1],[1,1]]

#masks of internal
m_1 = [[0,0],[0,1]]
m_2 = [[0,0],[1,0]]
m_3 = [[0,1],[0,0]]
m_4 = [[1,0],[0,0]]

#list of external
list_ext_mask = [m1,m2,m3,m4]

#list of internal
list_int_mask = [m_1,m_2,m_3,m_4]

im_2 = mpimg.imread('tc.jpg')
im_3 = convert_rgb_to_gray_level(im_2)
im_1 = convert_gray_level_to_bw(im_3)
plt.subplot(1,2,2), plt.imshow(im_1,cmap='gray')
plt.show()

ex_counter = 0
int_counter = 0
m = im_1.shape[0]
n = im_1.shape[1] 
for i in range(1,m-1):
    for j in range(1,n-2):
        if(piksel_compare1(im_1,i,j)):
            ex_counter = ex_counter + 1
        if(piksel_compare2(im_1,i,j)):
            int_counter = int_counter + 1
print(( ex_counter - int_counter )/4)
       
            
            
        
        
        


# In[ ]:

def hocanin_kodu():
    s = 0
    for i in range(4):
        if(my_block[i] == 1):
            s = s + 2**i
    if s == 8 or s == 4 or s == 2 or s == 1:
        return True
    else:
        return False


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



