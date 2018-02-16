
# coding: utf-8

# In[44]:


#Implement a userdefined function myreduce() 
def myreduce(list):
    y=1
    for n in list:
        y=y*int(n)
    return(y)

l=input("Enter a list with number\n")
l=l.split(',')
myreduce(l)


# In[126]:


#Implement a userdefined filter function myfilter()
def myfilter(list):
    z=[]
    for n in list:
        if(int(n) % 10 == 0):    
             z.append(n)
    return(z)    
l=input("Enter a list with number\n")
l=l.split(',')
myfilter(l)

