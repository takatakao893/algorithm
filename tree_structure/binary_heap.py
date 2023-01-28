def maxHeapify(i):
    l = i*2
    r = i*2+1
    if l <= H and key[l] > key[i]: # 左の子が存在し、その値が親の値よりも大きい場合
        largest = l # 親、左の子、右の子の中で最大の値を持つ節点の番号
    else:
        largest = i
    if r <= H and key[r] > key[largest]:
        largest = r
    if largest != i: # largestが親でない場合
        key[i],key[largest] = key[largest],key[i]
        maxHeapify(largest) # largestに移動

def buildMaxHeap():
    for i in range(H//2,0,-1):
        maxHeapify(i)

H=int(input())
key=[-1]+list(map(int,input().split())) # 二分ヒープを表す配列key
buildMaxHeap()
print('',*key[1:]) # max-ヒープを出力