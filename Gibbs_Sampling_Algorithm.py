from sklearn.mixture import GMM
import numpy as np
from math import *
import pandas as pd
import matplotlib.pyplot as plt

from scipy import stats, integrate
import seaborn as sns
sns.set(color_codes=True)

#Data Generation
gmm = GMM(2,covariance_type='diag')
gmm.means_ = np.array([[1], [4]])
gmm.weights_ = np.array([0.5, 0.5])
gmm.covars_ = np.array([[1], [1]]) 
X = gmm.sample(1000)

#Histogram
num_bins =50
n, bins, patches = plt.hist(X, num_bins, normed=1, facecolor='green', alpha=0.5)
plt.show()

#################################################
Gibbs Sampling Algorithm
#################################################
poids=0.5


#Initialization
theta_p=[]
theta_p.append(-0.2)
theta_p.append(0.1)

t_1=[]
t_2=[]

def proba(x,mu,poids):
    a=pow((x-mu),2)
    res=poids*exp((-1/2)*a)
    return res


n_iter=10000

for t in range(0,n_iter):
    
    n1=0
    n2=0
    s1=0
    s2=0
    
    for i in X:
        
        i=float(i)
        
        u=np.random.uniform()
        p=proba(i,theta_p[0],poids)
        p2=proba(i,theta_p[1],poids)
        p=p/(p+p2)
        #print(p,p2)
        if u<=p:
            
            s1+=i
            n1+=1
        else:
           
            s2+=i
            n2+=1
        
    esp1=(s1/(0.01+n1))
    sigma1=1/(0.01+n1)
    esp2=(s2/(0.01+n2))
    sigma2=1/(0.01+n2)
        
    theta_p[0]=np.random.normal(esp1,pow(sigma1,2))
    theta_p[1]=np.random.normal(esp2,pow(sigma2,2))

    if t>0:
        t_1.append(theta_p[0])
        t_2.append(theta_p[1])

#Descritpive staitsticlq analyse on the samples
df=pd.DataFrame() 
df["theta1"]=t_1
df["theta2"]=t_2
df.describe() 

#Histogram
plt.hist(t_1, num_bins, normed=1, facecolor='green', alpha=0.5)
plt.show()
plt.hist(t_2, num_bins, normed=1, facecolor='green', alpha=0.5)
plt.show()

sns.jointplot(x="theta1", y="theta2", data=df)

