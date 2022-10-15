""" Numpy is the fundamental package for numeric computing with Python. 
It provides powerful ways to create, store, and / or manipulate data, which makes it able to seamlessly and speedily integrate with a wide variety of databases. 
This is also the foundation that Pandas is built on, which is a high-performance data-centric package that we will learn later in the course.

In this lecture, we will talk about creating array with certain data types, manipulating array, selecting elements from arrays, and loading dataset into array. 
Such functions are useful for manipulating data and understanding the functionalities of other common Python data packages.
 """

import numpy as np
import math
# Arrays are displayed as a list or list of lists and can be created through list as well. When creating an
# array, we pass in a list as an argument in numpy array
a = np.array([1, 2, 3])
print(a)
# We can print the number of dimensions of a list using the ndim attribute
print(a.ndim)

a = np.array([1, 3, 5, 7])
a[2]
# For multidimensional array, we need to use integer array indexing, let's create a new multidimensional array
a = np.array([[1, 2], [3, 4], [5, 6]])
print(a)

# runthru
print("code completed successfully")
