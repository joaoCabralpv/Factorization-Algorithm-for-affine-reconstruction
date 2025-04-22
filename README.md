# Factorization-Algorithm-for-affine-reconstruction
Implementation of the Factorization Algorithm described in the paper "Shape and motion from image streams under orthography: A
factorization approach" by C. Tomasi and T. Kanade

# How to use
On the affineReconstruction.py file, put the points' coordinates in the image from each camera in the c1,c2,c3 lists. Corresponding points should have the same index on the different camera lists. The algorithm also works with a different number of cameras; Make a list with the points of that camera and then add that list to the list a.
