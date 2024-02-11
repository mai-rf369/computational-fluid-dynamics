# Computational-Fluid-Dynamics - Forward-in-Time-and-Centered-in-Space-Scheme
## Algorithm
$$
	u_{t, x} = c \frac{dt}{2 dx} (u_{t - 1, x + 1} - u_{t - 1, x - 1})
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
