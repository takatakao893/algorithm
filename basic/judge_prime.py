def judge_prime(N):
    if N<=1:
        return False
    if N==2:
        return True
    i=2
    while i*i<=N:
        if N%i==0:
            return False
        i+=1
    return True

n=int(input())
print("Yes" if judge_prime(n) else "No")
    