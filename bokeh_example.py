
# coding: utf-8

# In[10]:

import numpy as np
from bokeh.plotting import figure, show
from bokeh.io import output_notebook


# In[11]:

N=4000


# In[13]:

x = np.random.random(size=N)*100
y = np.random.random(size=N)*100
radii = np.random.random(size=N)*1.5
colors = ["#%02x%02x%02x" % (r,g,150) for r,g in zip(np.floor(50+2*x),np.floor(30+2*y))]


# In[14]:

output_notebook()


# In[15]:

p = figure()
p.circle(x,y, radius=radii, fill_color=colors, fill_alpha=0.6, line_color=None)


# In[16]:

show(p)


# In[ ]:



