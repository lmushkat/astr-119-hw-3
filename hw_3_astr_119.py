#!/usr/bin/env python
# coding: utf-8

# Find the roots of
# # f(x)=1.01x^2-3.04x+2.07
# using Bisection Search root finding.
# Use tolorence of 1e-6 for f(x)=0

# In[79]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt


# ### Define function for root finding

# In[80]:


def function_for_roots(x):
    a=1.01
    b=-3.04
    c=2.07
    return a*x**2 +b*x +c


# Check validity of of initial values

# In[81]:


def check_initial_values(f, x_min, x_max, tol):
    
    #checking guesses
    y_min = f(x_min)
    y_max = f(x_max)
    
    #check x_min/x_max contain 0 crossing
    if(y_min*y_max>=0.0):
        print("No zero crossing found in the range", x_min,x_max)
        s = "f(%f) = %f, f(%f)=%f" % (x_min,y_min,x_max,y_max)
        print(s)
        return 0
    # if x_min is a root, then return flag == 1
    if(np.fabs(y_min)<tol):
        return 1
    
    # if x_max is a root, then return flag == 2
    if(np.fabs(y_max)<tol):
        return 2
    
    #if we reach this point, the bracket is valid
    #and we return 3
    return 3


# Define main work function

# In[108]:


def bisection_root_finding(f, x_min_start, x_max_start, tol):
    
    # this function uses bisection search to find a root
    
    x_min = x_min_start  #minimum x in bracket
    x_max = x_max_start  #maximum x in bracket
    x_mid = 0.0          #mid point
    
    y_min = f(x_min)
    y_max = f(x_max)
    y_mid = 0.0
    
    imax= 10000
    i = 0
    
    #check the initial values
    flag = check_initial_values(f,x_min,x_max,tol)
    if(flag==0):
        print("error in bisection_root_finding().")
        raise ValueError('initial values invalid', x_min,x_max)
    elif(flag==1):
        #lucky guess
        return x_min
    elif(flag==2):
        return x_max
    
    #if we reach here we need to conduct the search
    
    #set flag
    flag = 1
    

    
    #enter while loop
    while(flag):
        x_mid = 0.5*(x_min+x_max)
        y_mid = f(x_mid)
        
        #check x_mid as root
        if(np.fabs(y_mid)<tol):
            flag=0
        else:
            #x_mid not a root; if product of the function is >0 at midpt &1 endpt replace endpt
            if(f(x_min)*f(x_mid)>0):
                x_min = x_mid
            else:
                x_max = x_mid
                
        print(x_min,f(x_min),x_max,f(x_max))
    
        i+=1
        print(i)
        
    
    if(i>=imax):
        print("exceeded max # of iterations = ", i)
        s= "Min bracket f(%f) = %f" % (x_min,f(x_min))
        print(s)
        s= "Max bracket f(%f) = %f" % (x_max,f(x_max))
        print(s)
        s= "Mid bracket f(%f) = %f" % (x_mid,f(x_mid))
        print(s)
        raise StopIteration('Stopping iterations after ',i)
    return x_mid
    


# In[125]:


x_min = 0.75
x_max = 1.5
tolerance = 1.0e-6

print(x_min,function_for_roots(x_min))
print(x_max,function_for_roots(x_max))

x_root = bisection_root_finding(function_for_roots,x_min,x_max,tolerance)
y_root = function_for_roots(x_root)

s = "root found with y(%f) = %f" % (x_root,y_root)
print(s)

x_min2 = 1.5
x_max2 = 2.5
tolerance = 1.0e-6

print(x_min2,function_for_roots(x_min2))
print(x_max2,function_for_roots(x_max2))

x_root2 = bisection_root_finding(function_for_roots,x_min2,x_max2,tolerance)
y_root2 = function_for_roots(x_root)

s = "root found with y(%f) = %f" % (x_root,y_root)
print(s)


# it takes 18 iterations to find our roots

# In[ ]:


x=np.linspace(0,3,1000)

plt.plot(x,function_for_roots(x))
plt.xlim(0,3)
plt.ylim(-0.5,2.1)

plt.axhline(0)

plt.plot(x_root,y_root, 'o')
plt.plot(x_root2,y_root2, 'o')
plt.plot(x_min,0,'o')
plt.plot(x_max,0, 'o')
plt.plot(x_max2,0, 'o')


# In[ ]:





# In[ ]:




