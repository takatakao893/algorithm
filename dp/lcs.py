def lcs(s, t):
    n,m = len(s), len(t)
    dp = [0 for _ in range(m+1)]
    for i in range(n):
        mem = dp[:]
        for j in range(m):
            if s[i] == t[j]:
                dp[j+1] = mem[j] + 1
            elif dp[j + 1] < dp[j]:
                dp[j+1] = dp[j]
    return dp[m]

q=int(input())
for _ in range(q):
    s=input().strip()
    t=input().strip()
    print(lcs(s, t))