## H1: Cholesky, Gauss and sweep
Running:
```
python3 cholesky-full.py
python3 gauss-full.py
python3 sweep-full.py
```
Scripts generate matrices with random values and draw graphs of time versus size automatically.

![Cholesky]
(images/cholesky.png)

![Gauss]
(images/gauss.png)

![Sweep]
(images/sweep.png)

## H2: Jacobi and Seidel
Running:
```
python3 jacobi.py
python3 seidel.py
```
These scripts work similarly to the previous ones.

![Jacobi]
(images/jacobi.png)

![Seidel]
(images/seidel.png)

## H3: Linear interpolation, splines and Lagrange
Running:
```
python3 linear.py
python3 lagrange.py
python3 spline.py
```
Every directory contains own **train.dat**, **train.ans** and **test.dat** files. Scripts generate the 4-th **test.ans** file. <br>
*Note*: **lagrange.py** and **spline.py** also generate the **plot.txt** file to demonstrate the result. Use **gnuplot** to show it:
```
gnuplot -p -e 'plot "plot.txt" with lines'
```
#### <span style="color:red">Bonus task</span>: grid splines
Run it and click on the window to see splines:
```
python3 spline_map.py
```
![Spline bonus]
(images/spline-bonus.png)

## H4: Heat and waves
*In development.*
