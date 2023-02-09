prime=[True]*201
prime[0]=False
prime[1]=False
for p in range(15):
    if prime[p]:
        for i in range(p*p,201,p):
            prime[i]=False
            
for index,bool in enumerate(prime):
    if bool==True:
        print(index)