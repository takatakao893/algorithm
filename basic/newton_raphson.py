# 2^(1/10)の値を求める y=x^10-2を解く
x=[0]*51
n=int(input())
x[0]=2
for i in range(1,n):
    x[i]=(9*x[i-1]+2/x[i-1]**9)/10
print(x)