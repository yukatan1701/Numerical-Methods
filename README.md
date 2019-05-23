## H1: Cholesky, Gauss and sweep
Running:
```
python3 cholesky-full.py
python3 gauss-full.py
python3 sweep-full.py
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
Every directory contains own **train.dat**, **train.ans** and **test.dat** files. Scripts generate the 4-th **test.ans** file. <br><br>
*Note*: every script can demonstrate you the result if you want. Use `-p` flag to see the plot. **Test points** are the x values (**test.dat** file) and the y values calculated for them (**test.ans** file).<br><br>
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
*In development.*
