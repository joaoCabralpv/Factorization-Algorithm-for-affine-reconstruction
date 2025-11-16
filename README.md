# Factorization-Algorithm-for-affine-reconstruction
Implementation of the Factorization Algorithm for affine reconstruction from parallel projection as described in Multiple View Geometry in Computer Vision.

This algorithm was firt discribed in the paper "Shape and motion from image streams under orthography: A factorization approach" by C. Tomasi and T. Kanade

# How to use
On the affineReconstruction.py file, put the points' coordinates in the image from each camera in the `c1`,`c2`,`c3` arrays. Corresponding points should have the same index on different  lists. The algorithm also works with a different number of views; Make an array with the points of that view and then add that list to the list `cameras`.

The script will print the coordinates of the points in 3D space in the order that they were put in the camara arrays and the the inhomogineous camera matricies and translations correspoinding to each view in the order that they were put in `cameras`