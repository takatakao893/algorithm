import math
prime_num=[]
n=int(input())
search_list=list(range(2,n+1))
while search_list[0]<=math.sqrt(n):
    head_num=search_list.pop(0)
    prime_num.append(head_num)
    search_list=[x for x in search_list if x%head_num!=0]
    prime_num.extend(search_list)
print(prime_num)