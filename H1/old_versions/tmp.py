import scipy.linalg as sl

A = [ [0 , 3 , 1] ,
      [4 , 3 , 2] ,
      [1 , 1 , 0] ]
f = [10 , 10 , 8]
x = sl.solve_banded ((1 , 1) , A , f )
print ( x )
