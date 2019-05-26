## H1: Exact methods for solving a system of linear equations
**Problem**: using exact solution methods, solve a system of linear equations.<br>
**Note**: all scripts generate matrices with random values and draw graphs of time versus size automatically.
### Solution 1: Gaussian elimination
Gaussian elimination is performed in two steps: a forward elimination and a back substitution.<br>
**Step 1**. By elementary row operations, bring the matrix to the upper triangular form. First step reduces a given system to *row echelon* form, from which one can tell whether there are no solutions, a unique solution, or infinitely many solutions.<br>
**Step 2**. Continue to use row operations until the solution is found; in other words, second step puts the matrix into *reduced row echelon* form.<br>
**Code**:
```python
# A is a square matrix;
# f is a vector of numbers on the right side of equalities;
# x is a solution vector.
def gauss(A, f):
    for k in range(n):
        A[k, k + 1:] /= A[k, k]
        f[k] /= A[k][k]
        for i in range(k + 1, n):
            A[i, k + 1:] -= A[i][k] * A[k, k + 1:]
            f[i] -= A[i][k] * f[k]
        A[k + 1:, k] = np.zeros(n - k - 1)
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = f[i]
        for j in range(i + 1, n):
            x[i] -= A[i][j] * x[j]
    return x
```
Running:
```
python3 gauss.py
```
Comparison of the speed of the self-writing function and the library function:<br>
![](images/gauss.png)
### Solution 2: tridiagonal matrix algorithm (Thomas algorithm, sweep)
This algorithm is a simplified form of Gaussian elimination that can be used to solve tridiagonal systems of equations. A tridiagonal system for *n* unknowns may be written as<br>
![equation](https://wikimedia.org/api/rest_v1/media/math/render/svg/2960afa763dced3c58f7ebd67c60b7a9efdc1e1d)<br>
where ![equation](https://wikimedia.org/api/rest_v1/media/math/render/svg/aebbedb9930c85592194b452369f51249f307871) and ![equation](https://wikimedia.org/api/rest_v1/media/math/render/svg/f65f76a2897d21124e5471dad54b1af0ded54eee).<br>
![equation](https://wikimedia.org/api/rest_v1/media/math/render/svg/66abee37b2bc74f82fb79e7e1f0b5475be9f9632)
<br>
**Step 1.** Find the coefficients through which all ![equation](https://latex.codecogs.com/gif.latex?x_i) are expressed linearly through each other:<br>
![equation](https://latex.codecogs.com/gif.latex?x_%7Bi-1%7D%3D%5Calpha_i%20x_i&plus;%5Cbeta_i%2C%20i%3D1%2C%5Cldots%2Cn&plus;1)<br>
After some calculations we get the formulas:<br>
![equation](https://latex.codecogs.com/gif.latex?%5Cbegin%7Bcases%7D%20%26%20%5Calpha_1%3D0%2C%20%5Cbeta_1%3D0%2C%20%5C%5C%20%26%20%5Calpha_%7Bi&plus;1%7D%3D%20%5Cfrac%7B-c_i%7D%7Ba_i%5Calpha_i&plus;b_i%7D%2C%20i%20%3D%201%2C%5Cldots%2Cn%20%5C%5C%20%26%20%5Cbeta_%7Bi&plus;1%7D%3D%20%5Cfrac%7Bd_i-a_i%5Cbeta_i%7D%7Ba_i%5Calpha_i&plus;b_i%7D%20%5Cend%7Bcases%7D)<br>
**Step 2.** Use back substitution to find an answer:<br>
![equation](https://latex.codecogs.com/gif.latex?%5Cbegin%7Bcases%7D%20%26%20x_%7Bn&plus;1%7D%3D0%20%5C%5C%20%26%20x_i%3D%20%5Calpha_%7Bi&plus;1%7Dx_%7Bi&plus;1%7D&plus;%5Cbeta_%7Bi&plus;1%7D%2C%20i%20%3D%20%5Coverline%7Bn%2C1%7D%20%5Cend%7Bcases%7D)<br>
**Code:**<br>
```python
def sweep(a, b, c, d):
    alpha = np.zeros(n + 1)
    beta = np.zeros(n + 1)
    for i in range(n):
        k = a[i] * alpha[i] + b[i]
        alpha[i + 1] = -c[i] / k
        beta[i + 1] = (d[i] - a[i] * beta[i]) / k
    x = np.zeros(n)
    x[n - 1] = beta[n]
    for i in range(n - 2, -1, -1):
        x[i] = alpha[i + 1] * x[i + 1] + beta[i + 1]
    return x
```
Running:
```
python3 sweep.py
```
Comparison of the speed of the self-writing function and the library function:<br>
![](images/sweep.png)
### Solution 3: Cholesky decomposition
The solution of ![equation](https://latex.codecogs.com/gif.latex?Ax%3Df) is reduced to the solution ![equation](https://latex.codecogs.com/gif.latex?S%5ETy%3Df) and ![equation](https://latex.codecogs.com/gif.latex?Sx%3Dy).<br>
**Step 1**. Matrix ![equation](https://latex.codecogs.com/gif.latex?S) is first filled with zeros, and then filled with values and becomes upper triangular through the formula:<br>
![equation](https://latex.codecogs.com/gif.latex?s_%7B11%7D%3D%5Csqrt%7Ba_%7B11%7D%7D%2C%20s_%7B1j%7D%3D%5Cfrac%7Ba_%7B1j%7D%7D%7Bs_%7B11%7D%7D)<br>
![equation](https://latex.codecogs.com/gif.latex?s_%7Bii%7D%3D%5Csqrt%7Ba_%7Bii%7D-%5Csum_%7Bk%3D1%7D%5E%7Bi-1%7Ds_%7Bki%7D%5E2%7D%2C%5C%3Bs_%7Bij%7D%3D%5Cfrac%7Ba_%7Bij%7D-%5Csum%5Climits_%7Bk%3D1%7D%5E%7Bi-1%7Ds_%7Bki%7D%5Ccdot%20s_%7Bkj%7D%7D%7Bs_%7Bii%7D%7D%2C%5C%3Bj%20%3E%20i)<br>
**Step 2**. Then two systems, given at the beginning, are solved using back substitution. <br>
**Code (calculating matrix S):**<br>
```python
def get_s(a, n):
    s = np.zeros((n, n))
    for i in range(n):
        sq_sum = 0.0
        for k in range(i):
            sq_sum += s[k, i] ** 2
        s[i, i] = (a[i, i] - sq_sum) ** 0.5
        for j in range(i + 1, n):
            s_sum = 0.0
            for k in range(i):
                s_sum += s[k, i] * s[k, j]
            s[i, j] = (a[i, j] - s_sum) / s[i, i]
    return s
```
Running:
```
python3 cholesky.py
```
Comparison of the speed of the self-writing function and the library function:<br>
![](images/cholesky.png)

## H2: Iterative methods for solving a system of linear equations
**Problem**: using iterative solution methods, solve a system of linear equations.<br>
**Note**: all scripts generate matrices with random values and draw graphs of time versus size automatically.<br><br>
The canonical form of the approximate solution of equation ![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20Ax%3Df):<br>
![equation](https://latex.codecogs.com/gif.latex?B%5Cfrac%7Bx%5E%7Bk&plus;1%7D-x%5Ek%7D%7B%5Ctau%7D&plus;Ax%5Ek%3Df)<br>
where ![equation](https://latex.codecogs.com/gif.latex?B) is a non-degenerate method dependent matrix, ![equation](https://latex.codecogs.com/gif.latex?%5Ctau) is an iteration parameter. Choosing arbitrarily these quantities, we obtain different methods of solution. ![equation](https://latex.codecogs.com/gif.latex?x%5Ek) converges to a solution.<br>
Let ![equation](https://latex.codecogs.com/gif.latex?A%3DL&plus;D&plus;U), where ![equation](https://latex.codecogs.com/gif.latex?L) is a strictly lower triangular matrix, ![equation](https://latex.codecogs.com/gif.latex?D) is diagonal, ![equation](https://latex.codecogs.com/gif.latex?U) is strictly upper triangular.
### Solution 1: Seidel method
**Idea**: ![equation](https://latex.codecogs.com/gif.latex?%5Ctau%3D1).<br>
**Result**: ![equation](https://latex.codecogs.com/gif.latex?%28L&plus;D%29x%5E%7Bk&plus;1%7D&plus;Ux%5Ek%3Df)<br>
**Code:**
```python
# get new approximate answer
def seidel(a, f, x):
    xnew = np.zeros(n)
    for i in range(n):
        s = 0
        for j in range(i - 1):
            s = s + a[i][j] * xnew[j]
        for j in range(i + 1, n):
            s = s + a[i][j] * x[j]
        xnew[i] = (f[i] - s) / a[i][i]
    return xnew

# choose suitable answer
def seidel_solve(a, f):
    eps = 0.000001
    xnew = np.zeros(n)
    while True:
        x = xnew
        xnew = seidel(a, f, x)
        if diff(x, xnew) <= eps:
            break
    return xnew

```
Running:
```
python3 seidel.py
```
Comparison of the speed of the self-writing function and the library function:<br>
![](images/seidel.png)

### Solution 2: Jacobi method
**Idea**: ![equation](https://latex.codecogs.com/gif.latex?B%3DD).<br>
**Result**: ![equation](https://latex.codecogs.com/gif.latex?Dx%5E%7Bk&plus;1%7D&plus;%28L&plus;U%29x%5Ek%3Df)<br>
**Code:**
```python
# get new approximate answer
def jacobi(a, f, x):
    xnew = np.zeros(n)
    for i in range(n):
        s = 0
        for j in range(i - 1):
            s = s + a[i][j] * x[j]
        for j in range(i + 1, n):
            s = s + a[i][j] * x[j]
        xnew[i] = (f[i] - s) / a[i][i]
    return xnew

# choose suitable answer
def jacobi_solve(a, f):
    eps = 0.000001
    xnew = np.zeros(n)
    while True:
        x = xnew
        xnew = jacobi(a, f, x)
        if diff(x, xnew) <= eps:
            break
    return xnew
```
Running:
```
python3 jacobi.py
```
Comparison of the speed of the self-writing function and the library function:<br>
![](images/jacobi.png)

## H3: Interpolation and approximation
**Problem**: Given a grid of order n (*train.dat* file):<br>
![equation](https://latex.codecogs.com/gif.latex?x_0%3Cx_1%3C%5Cldots%3Cx_n)<br>
Given a set of measurements (*train.ans* file):<br>
![equation](https://latex.codecogs.com/gif.latex?y_i%3Df%28x_i%29)<br>
It is necessary to restore the value of function ![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20f) in another set of points ![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20z_0%3Cz_1%3C%5Cldots%3Cz_m) (*test.dat* file) and save it to *test.ans* file.<br>
**Note**: every script can demonstrate you the result if you want. Use `-p` flag to see the plot. *Test points* are the *x* values (*test.dat* file) and the *y* values calculated for them (*test.ans* file).<br>
### Solution 1: linear interpolation
**Idea**:<br>![equation](https://latex.codecogs.com/gif.latex?f%28x%29%20%3D%20%5Cfrac%7By_%7Bi&plus;1%7D-y_i%7D%7Bx_%7Bi&plus;1%7D-x_i%7D%28x-x_i%29&plus;y_i%2C%5C%3Bx%5Cin%5Bx_i%3Bx_%7Bi&plus;1%7D%29)<br>
**Running**:
```
python3 linear.py -p
```
**Result**:<br>
![](images/linear.png)
### Solution 2: Lagrange polynomial
**Idea**:<br>
Build ![equation](https://latex.codecogs.com/gif.latex?P%28x%29) — the nth degree polynomial that will pass through the given points ![equation](https://latex.codecogs.com/gif.latex?%28x_i%2Cy_i%29).<br>
Decompose on the basis of polynomial ![equation](https://latex.codecogs.com/gif.latex?%5Cvarphi_i%28x%29):<br>
![equation](https://latex.codecogs.com/gif.latex?P%28x%29%3D%5Csum%5Climits_%7Bi%3D0%7D%5Eny_i%5Cvarphi_i%28x%29)<br>
![equation](https://latex.codecogs.com/gif.latex?%5Cvarphi_i%28x%29%3D%5Cfrac%7B%5Cprod_%7Bj%5Cneq%20i%7D%28x-x_j%29%7D%7B%5Cprod_%7Bj%5Cneq%20i%7D%28x_i-x_j%29%7D)<br>
**Running**:
```
python3 lagrange.py -p
```
**Result**:<br>
![](images/lagrange.png)
### Solution 3: spline interpolation (regular grid)
**Idea**:<br>
![equation](https://latex.codecogs.com/gif.latex?P_i%28x%29%3DA_i*%28x-x_i%29%5E3&plus;B_i*%28x-x_i%29%5E2&plus;C_i*%28x-x_i%29&plus;D_i%2C%5C%3Bi%3D%5Coverline%7B0%2Cn-1%7D)<br>
The vector of coefficients *B* is obtained from the solution of the system of equations *As = f* by the sweep method, and the remaining vectors of coefficients are obtained by the formulas:<br>
![equation](https://latex.codecogs.com/gif.latex?%5Cbegin%7Bcases%7D%20%26%20B_i%3Ds_i%20%5C%5C%20%26%20A_i%3D%5Cfrac%7BB_%7Bi&plus;1%7D-B_i%7D%7B3h%7D%20%5C%5C%20%26%20C_i%3D%5Cfrac%7By_%7Bi&plus;1%7D-y_i%7D%7Bh%7D-%28B_%7Bi&plus;1%7D&plus;2B_i%29%5Cfrac%7Bh%7D%7B3%7D%20%5C%5C%20%26%20D_i%3Dy_i%20%5Cend%7Bcases%7D)<br>
**Running**:
```
python3 spline.py -p
```
**Result**:<br>
![](images/spline.png)
### Bonus task: spline interpolation (irregular grid)
**Idea**: similar to the previous task, but with modified formulas.<br>
![equation](https://latex.codecogs.com/gif.latex?P_i%28x%29%3DA_i%28x-x_i%29%5E3&plus;B_i%28x-x_i%29%5E2&plus;C_i%28x-x_i%29&plus;D_i%2C%5C%3Bi%3D%5Coverline%7B0%2Cn-1%7D)<br>
Let's enter the notation:<br>
![equation](https://latex.codecogs.com/gif.latex?x_%7Bi&plus;1%7D-x_i%3Dh_i)<br>
Continuity conditions:<br>
![equation](https://latex.codecogs.com/gif.latex?%5Cbegin%7Bcases%7D%20%26%20P_i%28x_i%29%3Dy_i%2C%5C%3Bi%3D%5Coverline%7B0%2Cn-1%7D%20%5C%5C%20%26%20P_i%28x_%7Bi&plus;1%7D%29%3Dy_%7Bi&plus;1%7D%2C%5C%3Bi%3D%5Coverline%7B1%2Cn%7D%20%5C%5C%20%26%20P_i%27%28x_%7Bi&plus;1%7D%29%3DP_%7Bi&plus;1%7D%27%28x_%7Bi&plus;1%7D%29%2C%5C%3Bi%3D%5Coverline%7B0%2Cn-2%7D%20%5C%5C%20%26%20P_i%27%27%28x_%7Bi&plus;1%7D%29%3DP_%7Bi&plus;1%7D%27%27%28x_%7Bi&plus;1%7D%29%2C%5C%3Bi%3D%5Coverline%7B0%2Cn-2%7D%20%5C%5C%20%26%20P_0%27%27%28x_0%29%3D0%2CP_%7Bn-1%7D%27%27%28x_n%29%3D0%20%5Cend%7Bcases%7D)<br>
After substitution:<br>
![equation](https://latex.codecogs.com/gif.latex?%5Cbegin%7Bcases%7D%20%26%20D_i%3Dy_i%2C%5C%3Bi%3D%5Coverline%7B0%2Cn-1%7D%20%5C%5C%20%26%20A_ih_i%5E3&plus;B_ih_i%5E2&plus;C_ih_i&plus;y_i%3Dy_%7Bi&plus;1%7D%2C%5C%3Bi%3D%5Coverline%7B0%2Cn-1%7D%20%5C%5C%20%26%203A_ih_i%5E2&plus;2B_ih_i&plus;C_i%3DC_%7Bi&plus;1%7D%2C%5C%3Bi%3D%5Coverline%7B0%2Cn-2%7D%20%5C%5C%20%26%206A_ih_i&plus;2B_i%3D2B_%7Bi&plus;1%7D%2C%5C%3Bi%3D%5Coverline%7B0%2Cn-2%7D%20%5C%5C%20%26%202B_0%3D0%20%5C%5C%20%26%206A_%7Bn-1%7Dh_%7Bn-1%7D&plus;2B_%7Bn-1%7D%3D0%20%5Cend%7Bcases%7D)<br>
Add a dummy element:<br>
![equation](https://latex.codecogs.com/gif.latex?B_n%3D0)<br>
Express *A* through *B*:<br>
![equation](https://latex.codecogs.com/gif.latex?A_i%3D%5Cfrac%7BB_%7Bi&plus;1%7D-B_%7Bi%7D%7D%7B3h_i%7D%2C%5C%3Bi%3D%5Coverline%7B0%2Cn-1%7D)<br>
Substitute *A* in the remaining equations:
![equation](https://latex.codecogs.com/gif.latex?%5Cbegin%7Bcases%7D%20%26%20%28B_%7Bi&plus;1%7D-B_i%29%5Cfrac%7Bh_i%5E2%7D%7B3%7D&plus;B_ih_i%5E2&plus;C_ih_i&plus;y_i%3Dy_%7Bi&plus;1%7D%2C%5C%3Bi%3D%5Coverline%7B0%2Cn-1%7D%20%5C%5C%20%26%20%28B_%7Bi&plus;1%7D-B_i%29h_i&plus;2B_ih_i&plus;C_i%3DC_%7Bi&plus;1%7D%2C%5C%3Bi%3D%5Coverline%7B0%2Cn-2%7D%20%5C%5C%20%26%20B_0%3D0%20%5C%5C%20%26%20B_n%3D0%20%5Cend%7Bcases%7D)<br>
Express *C* through *B*:<br>
![equation](https://latex.codecogs.com/gif.latex?C_i%3D%5Cfrac%7By_%7Bi&plus;1%7D-y_i%7D%7Bh_i%7D-%28B_%7Bi&plus;1%7D&plus;2B_i%29%5Cfrac%7Bh_i%7D%7B3%7D%2C%5C%3Bi%3D%5Coverline%7B0%2Cn-1%7D)<br>
Substitute and get a closed system for *B*:<br>
![equation](https://latex.codecogs.com/gif.latex?B_ih_i&plus;2B_%7Bi&plus;1%7D%28h_i&plus;h_%7Bi&plus;1%7D%29&plus;B_%7Bi&plus;2%7Dh_%7Bi&plus;1%7D%3D3%5Cleft%20%28%5Cfrac%7By_%7Bi&plus;2%7D-y_%7Bi&plus;1%7D%7D%7Bh_%7Bi&plus;1%7D%7D-%5Cfrac%7By_%7Bi&plus;1%7D-y_i%7D%7Bh_i%7D%20%5Cright%20%29)<br>
![equation](https://latex.codecogs.com/gif.latex?%5Cbegin%7Bcases%7D%20%26%20B_0%3DB_n%3D0%20%5C%5C%20%26%20B_%7Bi-1%7Dh_%7Bi-1%7D&plus;2B_%7Bi%7D%28h_%7Bi-1%7D&plus;h_%7Bi%7D%29&plus;B_%7Bi&plus;1%7Dh_%7Bi%7D%3D3%5Cleft%20%28%5Cfrac%7By_%7Bi&plus;1%7D-y_%7Bi%7D%7D%7Bh_%7Bi%7D%7D-%5Cfrac%7By_%7Bi%7D-y_%7Bi-1%7D%7D%7Bh_%7Bi-1%7D%7D%20%5Cright%20%29%2C%5C%3Bi%3D%5Coverline%7B1%2Cn-1%7D%20%5Cend%7Bcases%7D)<br>
It is reduced to a system of linear equations of order *n + 1* with a three-diagonal matrix:
![equation](https://latex.codecogs.com/gif.latex?%5Cbegin%7Bpmatrix%7D%20b_0%20%26%200%20%26%200%20%26%200%20%26%20%5Cldots%20%26%200%20%26%200%20%26%200%20%5C%5C%20a_1%20%26%20b_1%20%26%20c_1%20%26%200%20%26%20%5Cldots%20%26%200%20%26%200%20%26%200%20%5C%5C%200%20%26%20a_2%20%26%20b_2%20%26%20c_2%20%26%20%5Cldots%20%26%200%20%26%200%20%26%200%20%5C%5C%200%20%26%200%20%26%20a_3%20%26%20b_3%20%26%20%5Cldots%20%26%200%20%26%200%20%26%200%20%5C%5C%20%5Cvdots%20%26%20%5Cvdots%20%26%20%5Cvdots%20%26%20%5Cvdots%20%26%20%5Cddots%20%26%20%5Cvdots%20%26%20%5Cvdots%20%26%20%5Cvdots%20%5C%5C%200%20%26%200%20%26%200%20%26%200%20%26%20%5Cldots%20%26%20b_%7Bn-2%7D%20%26%20c_%7Bn-2%7D%20%26%200%20%5C%5C%200%20%26%200%20%26%200%20%26%200%20%26%20%5Cldots%20%26%20a_%7Bn-1%7D%20%26%20b_%7Bn-1%7D%20%26%20c_%7Bn-1%7D%20%5C%5C%200%20%26%200%20%26%200%20%26%200%20%26%20%5Cldots%20%26%200%20%26%200%20%26%20b_n%20%5Cend%7Bpmatrix%7D%20%5Cbegin%7Bpmatrix%7D%20B_0%5C%5C%20B_1%5C%5C%20B_2%5C%5C%20B_3%5C%5C%20%5Cvdots%5C%5C%20B_%7Bn-2%7D%5C%5C%20B_%7Bn-1%7D%5C%5C%20B_n%20%5Cend%7Bpmatrix%7D%3D%5Cbegin%7Bpmatrix%7D%200%5C%5C%203y_%7Bxx%2C1%7D%5C%5C%203y_%7Bxx%2C2%7D%5C%5C%203y_%7Bxx%2C3%7D%5C%5C%20%5Cvdots%5C%5C%203y_%7Bxx%2Cn-2%7D%5C%5C%203y_%7Bxx%2Cn-1%7D%5C%5C%200%20%5Cend%7Bpmatrix%7D)<br>
where<br>
![equation](https://latex.codecogs.com/gif.latex?y_%7Bxx%2Ci%7D%3D%5Cfrac%7By_%7Bi&plus;1%7D-y_i%7D%7Bh_i%7D-%5Cfrac%7By_i-y_%7Bi-1%7D%7D%7Bh_%7Bi-1%7D%7D)<br>
Diagonals:<br>
![equation](https://latex.codecogs.com/gif.latex?c_i%3D%280%2C%5C%3Bh_0%2C%5C%3Bh_1%2C%5C%3B%5Cldots%2C%5C%3Bh_%7Bn-2%7D%2C%5C%3B0%29)<br>
![equation](https://latex.codecogs.com/gif.latex?b_i%3D%281%2C%5C%3B2%28h_0&plus;h_1%29%2C%5C%3B2%28h_1&plus;h_2%29%2C%5C%3B%5Cldots%2C%5C%3B2%28h_%7Bn-2%7D&plus;%20h_%7Bh-1%7D%29%2C%5C%3B1%29)<br>
![equation](https://latex.codecogs.com/gif.latex?c_i%3D%280%2C%5C%3Bh_1%2C%5C%3Bh_2%2C%5C%3B%5Cldots%2C%5C%3Bh_%7Bn-1%7D%2C%5C%3B0%29)<br>
![equation](https://latex.codecogs.com/gif.latex?f%3D3%5Ccdot%280%2C%5C%3By_%7Bxx%2C1%7D%2C%5C%3By_%7Bxx%2C2%7D%2C%5C%3By_%7Bxx%2C3%7D%2C%5C%3B%5Cldots%2C%5C%3By_%7Bxx%2Cn-2%7D%2C%5C%3By_%7Bxx%2Cn-1%7D%2C%5C%3B0%29)<br>
Solve system *As = f* by the sweep method and obtain the vector of coefficients *B*. The remaining coefficients are determined by the formulas:<br>
![equation](https://latex.codecogs.com/gif.latex?%5Cbegin%7Bcases%7D%20%26%20B_i%3Ds_i%20%5C%5C%20%26%20A_i%3D%5Cfrac%7BB_%7Bi&plus;1%7D-B_i%7D%7B3h_i%7D%20%5C%5C%20%26%20C_i%3D%5Cfrac%7By_%7Bi&plus;1%7D-y_i%7D%7Bh_i%7D-%28B_%7Bi&plus;1%7D&plus;2B_i%29%5Cfrac%7Bh_i%7D%7B3%7D%20%5C%5C%20%26%20D_i%3Dy_i%20%5Cend%7Bcases%7D)<br>
**Running**:
```
python3 irregular-spline.py -p
```
**Result**:<br>
![](images/irregular-spline.png)
### Super bonus task: 2D splines
This is a two-dimensional spline interpolation using PyQt. Use `-p` flag to set line density (default value is 100). Run it and click on the window to see splines:
```
python3 spline_map.py
```
![](images/splines-bonus.png)

## H4: Heat and waves
### Heat (diffusion)
**Problem:** given a function of the initial profile ![equation](https://latex.codecogs.com/gif.latex?u_0%28x%2Cy%29) and the coefficient of thermal conductivity ![equation](https://latex.codecogs.com/gif.latex?%5Cmu). Find the position of the profile at an arbitrary time ![equation](https://latex.codecogs.com/gif.latex?T).<br>
![equation](https://latex.codecogs.com/gif.latex?%5Cbegin%7Bcases%7D%20%26%20%5Cfrac%7B%5Cpartial%20u%28x%2Cy%2Ct%29%29%7D%7B%5Cpartial%20t%7D%20-%20%5Cmu%28%5Cfrac%7B%5Cpartial%5E2%20u%28x%2Cy%2Ct%29%29%7D%7B%5Cpartial%20x%5E2%7D%20&plus;%20%5Cfrac%7B%5Cpartial%5E2%20u%28x%2Cy%2Ct%29%29%7D%7B%5Cpartial%20y%5E2%7D%29%20%3D%20f%28x%2Cy%2Ct%29%2C%20x%2C%20y%20%5Cin%20%5Cmathbb%7BR%7D%2C%20t%20%3E%200%5C%5C%20%26%20u%28x%2Cy%2C0%29%20%3D%20u_0%28x%2Cy%29%2C%20x%2C%20y%20%5Cin%20%5Cmathbb%7BR%7D%20%5Cend%7Bcases%7D)<br>
**Solution**: we will calculate the values for the matrix of size ![equation](https://latex.codecogs.com/gif.latex?n%5Ctimes%20n) using numerical methods. It is necessary after each update cycle to recalculate the values in all cells according to the formula:<br>
![equation](https://latex.codecogs.com/gif.latex?%5Ctilde%20y_%7Bij%7D%20%3D%20y_%7Bij%7D%20&plus;%20%5Cfrac%7B%5Cmu%5Ctau%7D%7Bh%5E2%7D%28y_%7Bi-1%2Cj%7D&plus;y_%7Bi&plus;1%2Cj%7D&plus;y_%7Bi%2Cj-1%7D&plus;y_%7Bi%2Cj&plus;1%7D-4y_%7Bi%2Cj%7D%29&plus;%5Ctau%20f_%7Bij%7D)<br>
where the coefficients ![equation](https://latex.codecogs.com/gif.latex?%5Cmu%2C%20%5Ctau%2C%20h) satisfy the stability (Courant) condition:<br>
![equation](https://latex.codecogs.com/gif.latex?%5Ctau%20%3C%20%5Cfrac%7Bh%5E2%7D%7B2%5Cmu%7D)<br>
The script *heat.py* demonstrates the heat equation visually. Click the mouse button to "heat up" the plate on the screen. It will gradually cool.<br>
**Note 1**: since a long press of the mouse is difficult to implement technically using pure PyQt5 only, it is made artificially. During 10 update cycles (variable `heat_duration`), the program will generate the effect of external forces independently.<br>
**Note 2**: use the command line arguments to adjust the pressing force and change the size of the spot. The default pressing force is 2000 (variable `force`).<br><br>
Example:
```
python3 heat.py 500
```
The result with default value `force = 2000`:<br>
![](images/heat.png)
<br>
### Waves
**Problem:** given a function of the initial profile ![equation](https://latex.codecogs.com/gif.latex?u_0%28x%2Cy%29) and the transport velocity ![equation](https://latex.codecogs.com/gif.latex?C). Find the position of the profile at an arbitrary time ![equation](https://latex.codecogs.com/gif.latex?T).<br>
![equation](https://latex.codecogs.com/gif.latex?%5Cbegin%7Bcases%7D%20%26%20%5Cfrac%7B%5Cpartial%5E2%20u%28x%2Cy%2Ct%29%29%7D%7B%5Cpartial%20t%5E2%7D%20-%20C%5E2%28%5Cfrac%7B%5Cpartial%5E2%20u%28x%2Cy%2Ct%29%29%7D%7B%5Cpartial%20x%5E2%7D%20&plus;%20%5Cfrac%7B%5Cpartial%5E2%20u%28x%2Cy%2Ct%29%29%7D%7B%5Cpartial%20y%5E2%7D%29%20%3D%20f%28x%2Cy%2Ct%29%2C%20x%2C%20y%20%5Cin%20%5Cmathbb%7BR%7D%2C%20t%20%3E%200%5C%5C%20%26%20u%28x%2Cy%2C0%29%20%3D%20u_0%28x%2Cy%29%2C%20x%2C%20y%20%5Cin%20%5Cmathbb%7BR%7D%20%5Cend%7Bcases%7D)<br>
**Solution**: we will calculate the values for the matrix of size ![equation](https://latex.codecogs.com/gif.latex?n%5Ctimes%20n) using numerical methods. It is necessary after each update cycle to recalculate the values in all cells according to the formula (we will use 3 layers to calculate; upper index is a layer):<br>
![equation](https://latex.codecogs.com/gif.latex?y_%7Bij%7D%5E2%20%3D%20y_%7Bij%7D%5E1%20-%20y_%7Bij%7D%5E0%20&plus;%20%5Cleft%20%28%20%5Cfrac%7B%5Ctau%20C%7D%7Bh%7D%20%5Cright%20%29%5E2%20%28y_%7Bi-1%2Cj%7D%5E1&plus;y_%7Bi&plus;1%2Cj%7D%5E1&plus;y_%7Bi%2Cj-1%7D%5E1&plus;y_%7Bi%2Cj&plus;1%7D%5E1-4y_%7Bi%2Cj%7D%5E1%29&plus;%5Ctau%5E2%20f_%7Bij%7D)<br>
where the coefficients ![equation](https://latex.codecogs.com/gif.latex?%5Ctau%2C%20h%2C%20C) satisfy the stability (Courant) condition:<br>
![equation](https://latex.codecogs.com/gif.latex?%5Ctau%20%3C%20%5Cfrac%7Bh%7D%7B2C%7D)<br>
The script *waves.py* demonstrates the transport equation visually. Click on the screen to make a wave! <br>
**Note**: use the command line arguments to adjust the pressing force and change the brightness of waves. The default pressing force is 400 (variable `force`).<br><br>
Example:
```
python3 waves.py 500
```
The result with default value `force = 400`:<br>
![](images/waves.png)

