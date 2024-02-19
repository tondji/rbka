# rbka
This repository contains the Python code that generates the figures in the paper "Randomized Sparse Kaczmarz with Averaging".

##### Authors:
- Lionel Tondji  (<tngoupeyou@aimsammi.org>)
- Dirk Lorenz    (<d.lorenz@tu-braunschweig.de>)

Contents
--------

##### Drivers (run these to generate figures):
	Main_Experiments.ipynb                        		notebook to generate figure 1 to 5 and 13 to 15		
	The_effect_of_the_number_of_threads_η.ipynb		notebook to generate figure 6 to 9
	The_effect_of_the_relaxation_parameter_α.ipynb          notebook to generate figure 10 and 11
	The_effect_of_the_sparsity_parameter_λ.ipynb		notebook to generate figure 12
	

##### Routines called by the drivers:
	tools.py			Python packages containing functions like the randomized sparse Kaczmarz with averaging, soft_skrinkage and sparse.
	plot_tools.py			Python packages useful for plotting the relative residual and error.			


