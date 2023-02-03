with open('mat1.txt') as f1:
    data1=f1.readline().rstrip('.')
    data1=data1.split(',')
    for i in range(len(data1)):
        data1[i]=data1[i].split(' ')

with open('mat2.txt') as f2:
    data2=f2.readline().split(',')
    for i in range(len(data2)):
        data2[i]=data2[i].lstrip(' ')
        data2[i]=data2[i].split(' ')

mat=[[] for _ in range(len(data1))]
for i in range(len(data1)):
    for j in range(len(data2[0])):
        total=0
        for k in range(len(data1[0])):
            total += int(data1[i][k])*int(data2[k][j])
        mat[i].append(total)

sum=0
# 対角成分の和
for i in range(len(data1)):
    sum+=mat[i][i]
print(sum)

    