## H1: Cholesky, Gauss and sweep
Running:
```
python3 cholesky.py
python3 gauss.py
python3 sweep.py
```
Scripts generate matrices with random values and draw graphs of time versus size automatically.

![](images/cholesky.png)

![](images/gauss.png)

![](images/sweep.png)

## H2: Jacobi and Seidel
Running:
```
python3 jacobi.py
python3 seidel.py
```
These scripts work similarly to the previous ones.

![](images/jacobi.png)

![](images/seidel.png)

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
![equation](https://latex.codecogs.com/gif.latex?%5Ctau%20%3C%20%5Cfrac%7Bh%7D%7B2c%7D)<br>
The script *waves.py* demonstrates the transport equation visually. Click on the screen to make a wave! <br>
**Note**: use the command line arguments to adjust the pressing force and change the brightness of waves. The default pressing force is 400 (variable `force`).<br><br>
Example:
```
python3 waves.py 500
```
The result with default value `force = 400`:<br>
![](images/waves.png)

