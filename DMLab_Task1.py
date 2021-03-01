#!/usr/bin/env python
# coding: utf-8

# In[41]:


import pandas as pd
from scipy.spatial import distance
from scipy.spatial.distance import cityblock
from tabulate import tabulate 

dataframe=pd.read_csv("dataset_review.csv")
print(dataframe)


# In[42]:


df=dataframe.replace('-',float("Nan"))
df


# In[43]:


#P1-P2 Distance


# In[44]:


df1_p1p2=df.drop(["p3","p4","p5","p6","p7","p8"],axis=1)
df2_p1p2=df1_p1p2[df1_p1p2["p1"].notnull()]
df2_p1p2=df2_p1p2[df2_p1p2["p2"].notnull()]


# In[45]:


manhattanDistance_p1p2 = distance.cityblock(df2_p1p2['p1'].astype(float),df2_p1p2['p2'].astype(float))
eucDistance_p1p2 = distance.euclidean(df2_p1p2['p1'].astype(float),df2_p1p2['p2'].astype(float))
minkDistance_p1p2 = distance.minkowski(df2_p1p2['p1'].astype(float),df2_p1p2['p2'].astype(float),p=3)


# In[46]:


#P1-P3 Distance


# In[47]:


df1_p1p3=df.drop(["p2","p4","p5","p6","p7","p8"],axis=1)
df2_p1p3=df1_p1p3[df1_p1p3["p1"].notnull()]
df2_p1p3=df2_p1p3[df2_p1p3["p3"].notnull()]


# In[48]:


manhattanDistance_p1p3 = distance.cityblock(df2_p1p3['p1'].astype(float),df2_p1p3['p3'].astype(float))
eucDistance_p1p3 = distance.euclidean(df2_p1p3['p1'].astype(float),df2_p1p3['p3'].astype(float))
minkDistance_p1p3 = distance.minkowski(df2_p1p3['p1'].astype(float),df2_p1p3['p3'].astype(float),p=3)


# In[49]:


#P1-P4 Distance


# In[50]:


df1_p1p4=df.drop(["p2","p3","p5","p6","p7","p8"],axis=1)
df2_p1p4=df1_p1p4[df1_p1p4["p1"].notnull()]
df2_p1p4=df2_p1p4[df2_p1p4["p4"].notnull()]


# In[51]:


manhattanDistance_p1p4 = distance.cityblock(df2_p1p4['p1'].astype(float),df2_p1p4['p4'].astype(float))
eucDistance_p1p4 = distance.euclidean(df2_p1p4['p1'].astype(float),df2_p1p4['p4'].astype(float))
minkDistance_p1p4 = distance.minkowski(df2_p1p4['p1'].astype(float),df2_p1p4['p4'].astype(float),p=3)


# In[52]:


#P1-P5 Distance


# In[53]:


df1_p1p5=df.drop(["p2","p3","p4","p6","p7","p8"],axis=1)
df2_p1p5=df1_p1p5[df1_p1p5["p1"].notnull()]
df2_p1p5=df2_p1p5[df2_p1p5["p5"].notnull()]


# In[54]:


manhattanDistance_p1p5 = distance.cityblock(df2_p1p5['p1'].astype(float),df2_p1p5['p5'].astype(float))
eucDistance_p1p5 = distance.euclidean(df2_p1p5['p1'].astype(float),df2_p1p5['p5'].astype(float))
minkDistance_p1p5 = distance.minkowski(df2_p1p5['p1'].astype(float),df2_p1p5['p5'].astype(float),p=3)


# In[55]:


#P1-P6 Distance


# In[56]:


df1_p1p6=df.drop(["p2","p3","p4","p5","p7","p8"],axis=1)
df2_p1p6=df1_p1p6[df1_p1p6["p1"].notnull()]
df2_p1p6=df2_p1p6[df2_p1p6["p6"].notnull()]


# In[57]:


manhattanDistance_p1p6 = distance.cityblock(df2_p1p6['p1'].astype(float),df2_p1p6['p6'].astype(float))
eucDistance_p1p6 = distance.euclidean(df2_p1p6['p1'].astype(float),df2_p1p6['p6'].astype(float))
minkDistance_p1p6 = distance.minkowski(df2_p1p6['p1'].astype(float),df2_p1p6['p6'].astype(float),p=3)


# In[58]:


#P1-P7 Distance


# In[59]:


df1_p1p7=df.drop(["p2","p3","p4","p5","p6","p8"],axis=1)
df2_p1p7=df1_p1p7[df1_p1p7["p1"].notnull()]
df2_p1p7=df2_p1p7[df2_p1p7["p7"].notnull()]


# In[60]:


manhattanDistance_p1p7 = distance.cityblock(df2_p1p7['p1'].astype(float),df2_p1p7['p7'].astype(float))
eucDistance_p1p7 = distance.euclidean(df2_p1p7['p1'].astype(float),df2_p1p7['p7'].astype(float))
minkDistance_p1p7 = distance.minkowski(df2_p1p7['p1'].astype(float),df2_p1p7['p7'].astype(float),p=3)


# In[61]:


#P1-P8 Distance


# In[62]:


df1_p1p8=df.drop(["p2","p3","p4","p5","p6","p7"],axis=1)
df2_p1p8=df1_p1p8[df1_p1p8["p1"].notnull()]
df2_p1p8=df2_p1p8[df2_p1p8["p8"].notnull()]


# In[63]:


manhattanDistance_p1p8 = distance.cityblock(df2_p1p8['p1'].astype(float),df2_p1p8['p8'].astype(float))
eucDistance_p1p8 = distance.euclidean(df2_p1p8['p1'].astype(float),df2_p1p8['p8'].astype(float))
minkDistance_p1p8 = distance.minkowski(df2_p1p8['p1'].astype(float),df2_p1p8['p8'].astype(float),p=3)


# In[64]:


pip install tabulate


# In[68]:


print("----------Manhattan Distance Table----------")
manhattan_table = [("P1","P2",manhattanDistance_p1p2),
                   ("P1","P3",manhattanDistance_p1p3),
                   ("P1","P4",manhattanDistance_p1p4),
                   ("P1","P5",manhattanDistance_p1p5),
                   ("P1","P6",manhattanDistance_p1p6),
                   ("P1","P7",manhattanDistance_p1p7),
                   ("P1","P8",manhattanDistance_p1p8),]
man_header = ["Distance From", "Distance to", "Value"]
print(tabulate(manhattan_table,headers=man_header,tablefmt="grid"))


# In[69]:


print("----------Euclidean Distance Table----------")
euc_table =       [("P1","P2",eucDistance_p1p2),
                   ("P1","P3",eucDistance_p1p3),
                   ("P1","P4",eucDistance_p1p4),
                   ("P1","P5",eucDistance_p1p5),
                   ("P1","P6",eucDistance_p1p6),
                   ("P1","P7",eucDistance_p1p7),
                   ("P1","P8",eucDistance_p1p8),]
euc_header = ["Distance From", "Distance to", "Value"]
print(tabulate(euc_table,headers=euc_header,tablefmt="grid"))


# In[70]:


print("----------Minkowski Distance Table----------")
mink_table =      [("P1","P2",minkDistance_p1p2),
                   ("P1","P3",minkDistance_p1p3),
                   ("P1","P4",minkDistance_p1p4),
                   ("P1","P5",minkDistance_p1p5),
                   ("P1","P6",minkDistance_p1p6),
                   ("P1","P7",minkDistance_p1p7),
                   ("P1","P8",minkDistance_p1p8),]
mink_header = ["Distance From", "Distance to", "Value"]
print(tabulate(mink_table,headers=mink_header,tablefmt="grid"))


# In[ ]:




