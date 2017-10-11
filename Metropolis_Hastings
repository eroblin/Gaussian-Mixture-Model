mu1=[]
mu2=[]
#iterations
n=20000

mu1.append(1)
mu2.append(5)

mu1.append(1)
mu2.append(5)

#mu1.append(np.random.normal(mu1[0],1))
#mu2.append(np.random.normal(mu2[0],1))

############ Algorithm #############

for t in range(1,n):
    
    #Generate new temporary parameters
    a1=np.random.normal(mu1[t],0.01)
    a2=np.random.normal(mu2[t],0.01)
    #print(a1,a2)
    
    a=norm.pdf(a1,mu1[t],1)*norm.pdf(a2,mu2[t],1)
    b=norm.pdf(mu1[t],mu1[t-1],1)*norm.pdf(mu2[t],mu2[t-1],1)
    
    f=a/b

    for i in X:
        i=float(i)
        num=(norm.pdf(i,a1,1)+norm.pdf(i,a2,1))
        #print("num :",num)
        denom=(norm.pdf(i,mu1[t],1)+norm.pdf(i,mu2[t],1))
        #print("denom :",denom)
        f=f*num/denom
       

    #Generate new parameters
    #print("f :",f)
    
    u=np.random.uniform()
    #print("u :",u)
    if f>u :
        mu1.append(a1)
        mu2.append(a2)
    else:
        mu1.append(mu1[t])
        mu2.append(mu2[t])
        
print("mu1 :",mu1[len(mu1)-1])
print("mu2 :",mu2[len(mu2)-1])
        
