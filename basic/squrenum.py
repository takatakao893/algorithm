def divisors(N):
    upper_divisors,lower_divisors=[],[]
    i=1
    while i*i<=N:
        if N%i==0:
            lower_divisors.append(i)
            if i!=N//i:
                upper_divisors.append(N//i)
        i+=1
    return lower_divisors+upper_divisors[::-1]
                
n=int(input())
print("Yes" if len(divisors(n))%2==1 else "No")
