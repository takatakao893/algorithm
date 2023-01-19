x_max=10**5
X=int(input())
values=[100,101,102,103,104,105]
dp=[0]*(x_max+1)
dp[100]=1
dp[101]=1
dp[102]=1
dp[103]=1
dp[104]=1
dp[105]=1
for i in range(10**5):
    if dp[i]:
        for value in values:
            if i+value<=X:
                dp[i+value]=dp[i]
print(dp[X])
