import numpy as np

c1=[
[812,505],
[812,546],
[850,402],
[850,444],
[601,490],
[601,531],
]

c2=[
[530,438],
[530,454],
[582,220],
[582,236],
[317,394],
[317,410],
]

c3=[
[549,394],
[549,456],
[873,393],
[874,456],
[542,370],
[542,434],
]

a=[c1,c2,c3]
""""
for i in range(3):
    for j in range(len(a[i])):
       a[i][j][1]=1031-a[i][j][1]
       #print(f"{a[i][j][0]},{a[i][j][1]}") 
"""
c=[]

for i in range(len(a)):
    x=0
    y=0
    for j in range(len(a[i])):
        x+=a[i][j][0]
        y+=a[i][j][1]
    x=x/len(a[i])
    y=y/len(a[i])
    c.append([x,y])
    #print(f"centroid{i+1}=[{x},{y}]")

for i in range(len(a)):
    for j in range(len(a[i])):
        a[i][j][0]-=c[i][0]
        a[i][j][1]-=c[i][1]
    #print(f"c{i+1}={a[i]}")


W=np.empty((len(a)*2,len(c1)))

for i in range(len(a)):
    for j in range(len(c1)):
        W[2*i,j]=a[i][j][0]
        b=a[i][j][1]
        W[(2*i)+1,j]=b

U,D,V = np.linalg.svd(W)
vt=V.T
#print(np.linalg.matrix_transpose(vt))

#t=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

for i in range(len(c1)):
    p=[float(vt[i][0]),float(vt[i][1]),float(vt[i][2])]
    s=f"X{i}={p}".replace("[","(").replace("]",")")
    print(s)

u1=(U[:,0]*D[0])
u2=U[:,1]*D[1]
u3=U[:,2]*D[2]

MMatrix=np.array([u1,u2,u3]).transpose()


for i in range(len(a)):
    m=MMatrix[i*2:(i*2)+2,0:3]
    print(f"M{i+1}={m}")

for i in range(len(a)):
    print(f"t{i+1}={c[i]}")