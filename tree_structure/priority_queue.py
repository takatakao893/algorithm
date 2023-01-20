from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def insert(A, x):
    x *= -1
    heappush(A, x)

def extractMax(A):
    x = heappop(A)
    return x * -1

q=[]

while True:
    com, *arg = input().split()
    if com == "insert":
        insert(q,int(arg[0]))
    elif com == "extract":
        print(extractMax(q))
    else:
        exit()
        