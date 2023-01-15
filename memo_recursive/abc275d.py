# memo-recursive
memo={}
def func(N):
    if N in memo:
        return memo[N]
    if N==0:
        return 1
    else:
        memo[N] = func(N//2) + func(N//3)
        return memo[N]
N=int(input())
print(func(N))
