with open("mat1.txt") as f:
    data=f.readline().rstrip('.')
    data=data.split(',')
    for i in range(len(data)):
        data[i]=data[i].split(' ')
    print('行数:',len(data),'列数:',len(data[0]))