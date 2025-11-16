import numpy as np
from sys import exit

# create arrays with the images of the points for each camera
# they have to be np arrays
c1=np.array([
[969,526],
[969,467],
[658.0,582.0],
[1088.0,648.0],
[708.0,593.0],
[1089.0,590.0]
])

c2=np.array([
[458,669],
[457,608],
[543.0,785.0],
[754.0,641.0],
[571.0,768.0],
[754.0,581.0]
])

c3=np.array([
[712,455],
[712,394],
[533.0,554.0],
[972.0,512.0],
[586.0,552.0],
[972.0,451.0]
])


#put the arrays that you made before in this list (don't change the name)
cameras=[c1,c2,c3]

# check if each point has two coordinates
n_points=-1
for camera in cameras:
    for point in camera:
        print(point)
        if len(point) != 2:
            print("Error, each point should have 2 coordinates")
            exit(1)
    if n_points==-1:
        n_points=len(camera)
    elif n_points != len(camera):
        print("Each camera should have the same number of points")
        print(camera)
        exit(2)

# compute centroids
centroids=[]

for camera in cameras:
    sum=np.array([0.0,0.0])
    for points in camera:
        sum+=points
    centroid=sum/len(camera)
    centroids.append(centroid)

for i in range(len(cameras)):
    for j in range(len(cameras[i])):
        cameras[i][j]-=centroids[i]

# create the measurment matrix W
# M[i][j] -> i indexes rows j indexes element of row M[:,j] indexes columns and returns row vector  M[:,[j]] indexes columns and returns colums vector
W=np.empty((2*len(cameras),len(c1)))

cameras_transpose=[]
for camera in cameras:
    cameras_transpose.append(camera.T)

w=np.concatenate(cameras_transpose)

# SVD of W
U,D,V = np.linalg.svd(w,full_matrices=False)


leters=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

# Extract and print reconstruction of the points. The points are given in the same order as they appeared in the camera arrays
points=[]
for i in range(len(c1)):
    x=(V).T[i]
    x=[float(x[0]),float(x[1]),float(x[2])]
    points.append(x)
    text=str(x).replace("[","(").replace("]",")")
    empty=""
    print(f"{leters[i%26]+ ((str(int(i/26))) if len(c1) > 26 else empty) }={text}")

# Print the centroids (t_i)
for i in range(len(centroids)):
    print(f"t_{i}={centroids[i]}")

# Extract and print camera matricies
DU=U@np.diag(D)
print(DU)
mlist=[]
for i in range(len(cameras)):
    mi1=DU[2*i][0:3]
    mi2=DU[2*i+1][0:3]
    mi=np.array([mi1,mi2])
    mlist.append(mi)
    print(f"M{i}={mi}")
