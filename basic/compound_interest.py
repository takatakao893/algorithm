# 複利の計算 元金を10,000とし利率をr=1%とする
p=10000
r=0.01
def f(n):
    if n==0:
        return p
    else:
        return f(n-1)*(1+r)

print(f(5))
