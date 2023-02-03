from collections import deque
m,n,s=map(int,input().split())
A=[[1]*n for _ in range(m)]
B=[[1]*m for _ in range(n)]
C=[[0]*m for _ in range(m)]

cache=deque([])

cnt_m=0 # 全体の読み出し回数
cnt_c=0 # キャッシュの読み出し回数
# LRU(Leat Recently Used) 最も長く使われていない要素を取り出し破棄する
for i in range(m):
    for j in range(m):
        for k in range(n):
            C[i][j]+=A[i][k]*B[k][j]
            cnt_m+=2
            if ["A",i,k] in cache:
                cnt_c+=1
                cache.append(cache.remove(["A",i,k]))
            else:
                if len(cache)<s:
                    cache.append(["A",i,k])
                else:
                    cache.popleft()
                    cache.append(["A",i,k])
            if ["B",k,j] in cache:
                cnt_c+=1
                cache.append(cache.remove(["B",k,j]))
            else:
                if len(cache)<s:
                    cache.append(["B",k,j])
                else:
                    cache.popleft()
                    cache.append(["B",k,j])
# メインメモリからの読み出し回数
print(cnt_m-cnt_c)

# キャッシュヒット率はキャッシュヒット数/(キャッシュヒット数+キャッシュミス数)
