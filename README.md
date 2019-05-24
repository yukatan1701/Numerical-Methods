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
#### Heat (diffusion)
The script *heat.py* demonstrates the heat equation visually. Click the mouse button to "heat up" the plate on the screen. It will gradually cool.<br>
**Note 1**: since a long press of the mouse is difficult to implement technically using pure PyQt5 only, it is made artificially. During 10 update cycles (variable `heat_duration`), the program will generate the effect of external forces independently.<br>
**Note 2**: use the command line arguments to adjust the pressing force and change the size of the spot. The default pressing force is 2000 (variable `force`).<br><br>
Example:
```
python3 heat.py 500
```
The result with default value `force = 2000`:
![](images/heat.png)
#### Waves
The script *wave.py* demonstrates the transfer equation visually. Click on the screen to make a wave! <br>
**Note 2**: use the command line arguments to adjust the pressing force and change the brightness of waves. The default pressing force is 400 (variable `force`).<br><br>
Example:
```
python3 waves.py 500
```
The result with default value `force = 400`:
![](images/waves.png)

