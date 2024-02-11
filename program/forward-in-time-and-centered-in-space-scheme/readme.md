# Computational-Fluid-Dynamics - Forward-in-Time-and-Centered-in-Space-Scheme
## Algorithm
$$
	u_{tc, xc} = c \frac{dt}{dx} (u_{tc - 1, xc + 1} - u_{tc - 1, xc - 1})
$$

|	Name	|	Value	|	Description		|
|	---	|	---	|	---			|
|	ts	|	0.0	|	Time Start		|
|	te	|	10.0	|	Time End		|
|	dt	|	0.1	|	Infinitesimal Time	|
|	xs	|	0.0	|	X Start			|
|	xe	|	1.0	|	X End			|
|	dx	|	0.01	|	Infinitesimal X		|
|	c	|	0.1	|	Transport Velocity	|

$$
Courant Number = c \frac{dt}{dx} = 1.0
$$

## Execution
```
> python ./program.py
```
