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
The canonical form of the approximate solution of equation ![equation](https://latex.codecogs.com/gif.latex?Ax%3Df):<br>
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

## H3: Linear interpolation, splines and Lagrange
Every directory contains own *train.dat*, *train.ans* and *test.dat* files. Scripts generate the 4-th *test.ans* file. <br><br>
**Note**: every script can demonstrate you the result if you want. Use `-p` flag to see the plot. *Test points* are the x values (*test.dat* file) and the y values calculated for them (*test.ans* file).<br><br>
Examples:
```
python3 linear.py -p
```
![](images/linear.png)
```
python3 lagrange.py -p
```
![](images/lagrange.png)
```
python3 spline.py -p
```
![](images/spline.png)
#### <span style="color:red">Bonus task</span>: grid splines
Run it and click on the window to see splines:
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

