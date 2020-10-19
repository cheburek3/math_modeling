M=4
N=3
a=[]
for i in range(N):
    z=[]
    for j in range(M):
        z.append(int(input()))
    a.append(z)
b=[]
for i in range(N):
    z=[]
    for j in range (M):
        z.append(int(input()))
    b.append(z)
c=b[0:]
for i in range(M):
    for j in range(M):
        if a [i][j]> b [i][j]:
            c[i][j]=a[i][j]
print("первая матрица:")
for i in a:
    print(i)
print("вторая матрица:")
for i in b:
    print(i)
print("третья матрица:")
for i in c:
    print(i)
    
        