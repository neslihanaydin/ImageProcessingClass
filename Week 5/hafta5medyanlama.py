
# coding: utf-8

# In[96]:


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


# In[117]:


def get_median(poi):
    s_1 = poi.reshape(1,36)
    s_1.sort()
    return (s_1[0,4])


# In[118]:


def get_distance(v, w= [1/3, 1/3, 1/3]):
    a,b,c = v[0],v[1],v[2]
    w1,w2,w3 = w[0],w[1],w[2]
    d = ((a**2)*w1+(b**2)*w2+(c**2)*w3)**.5
    return d
def get_default_mask_for_mean():
    return np.array([1,1,1,1,1,1,1,1,1]).reshape(3,3)/9 

def apply_mask(part_of_image):
    mask = get_default_mask_for_mean()
    return sum(sum(part_of_image*mask))
def convert_rgb_to_gray_level(im_1):
    m = im_1.shape[0]
    n = im_1.shape[1]
    im_2 = np.zeros((m,n))
    for i in range (m):
        for j in range(n):
            im_2[i,j] = get_distance(im_1[i,j,:])
    return im_2
def get_mean_filter(img_1):
   # im_1 = mpimg.imread(r'c:\sunflower.jpg')
    m = im_1.shape[0]
    n = im_1.shape[1]
    im_2 = np.zeros((m,n))
    for i in range(1, m-1):
        for j in range(1, n-1):
            poi = im_1[i-1:i+2,j-1:j+2]
          #  im_2[i,j] = apply_mask(poi)
            im_2[i,j] = get_median(poi)
        
    return im_2


# In[119]:


im_1 = mpimg.imread(r'c:\testmedian.png')
im_2 = convert_rgb_to_gray_level(im_1)
get_ipython().run_line_magic('matplotlib', 'inline')
plt.subplot(1,3,1),plt.imshow(im_1)
plt.subplot(1,3,2),plt.imshow(im_2,cmap='gray')


# In[120]:


im_55 = get_mean_filter(im_2)
plt.imshow(im_55,cmap='gray')


# In[ ]:


#mask_1 [:,1] 1.sutun gelir
mask0 = np.array([1,1,1,1,1,1,1,1,1]).reshape(3,3)
mask1 = np.random.randint(5, size = 9).reshape(3,3)
mask2 = np.random.randint(5, size = 9).reshape(3,3)
mask1[:,0 : 2] # satırlar önemli değil 0 ile 2 arasındaki sütunlar geliyor(2 dahildegil)
print(mask1)
print("---------------")
print(mask2)
print("***************")
print(mask1*mask0)
sum(mask1*mask0)
sum(sum(mask1*mask0))

