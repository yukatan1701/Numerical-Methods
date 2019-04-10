## H1: Cholesky, Gauss and sweep
Running:
```
python3 cholesky-full.py
python3 gauss-full.py
python3 sweep-full.py
```
Scripts generate matrices with random values and draw graphs of time versus size automatically.

## H2: Jacobi and Seidel
Running:
```
python3 jacobi.py
python3 seidel.py
```
These scripts work similarly to the previous ones.

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

## H4: Heat and waves
*In development.*
