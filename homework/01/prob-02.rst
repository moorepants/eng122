Problem 2
=========

In a Jupyter notebook use NumPy to solve the following:

1. Create a uniform subdivision of the interval -1.3 to 2.5 with 64
   subdivisions.
2. Generate an array of length :math:`3n` filled with the cyclic pattern 1, 2,
   3.
3. Create an array of the first 10 odd integers.
4. Create a 10 x 10 arrays of zeros and then "frame" it with a border of ones.
5. Create an 8 x 8 array with a checkerboard pattern of zeros and ones using a
   slicing + striding approach.
6. Try using the dot function on a vector-vector, matrix-vector and
   matrix-matrix example. (This may seem simple but it's good to see how the
   results differ in each case.)
7. Create a function which creates an n×n array with (i,j)-entry equal to i+j.
8. Evaluate cos and sin on the interval [0, 1] and then stack the results into
   a tall array with rows being the (cos(x), sin(x)) entries.
9. Create a random 3x5 array using the ``np.random.rand(3, 5)`` function and
   compute: the sum of all the entries, the sum of the rows and the sum of the
   columns. (*Just like sorted had an optional key= argument, many Numpy
   functions have an optional axis= argument!*)
10. Create a random 5x5 array using the function ``np.random.rand(5, 5)``. We want
    to sort the rows according to the second column. Try combining array
    slicing + argsort + indexing to do this.

Refer to the `NumPy documentation`_ and `SciPy Lecture Notes`_ for help.

.. _NumPy documentation: http://docs.scipy.org/doc/numpy-1.10.0/
.. _SciPy Lecture Notes: http://www.scipy-lectures.org/
