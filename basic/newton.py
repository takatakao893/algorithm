def f(x):
    return x**2.0-2

def newton(x0,eps=1e-7,error=1e-7,max_loop=100,cnt=0):
    while True:
        df_x=(f(x0+eps)-f(x0-eps))/(2*eps)
        if df_x <= error:
            print("slope is too small")
            exit()
        
        x1=x0-f(x0)/df_x
        cnt+=1
        if abs(x1-x0)<=error or cnt>=max_loop:
            break
        x0=x1
        print(x0)
    return x0
print(3.0)
print(newton(3.0))
