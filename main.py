from latex2sympy2 import latex2sympy
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt  # Corrected import

# Define the LaTeX equation
latex_eq = r'\sin(x) + \cos(2x)'

# Define the symbol
x = sp.symbols('x')

# Convert LaTeX to a SymPy expression
expr = latex2sympy(latex_eq)

# Convert the SymPy expression to a numerical function
y_func = sp.lambdify(x, expr, 'numpy')  # Corrected lambdify usage

# Generate data for plotting
x_vals = np.linspace(-10, 10, 400)  # Generate x values
y_vals = y_func(x_vals)  # Compute corresponding y values

# Plot the equation using matplotlib
plt.plot(x_vals, y_vals)  # Use raw string for LaTeX label
plt.xlabel('x')
plt.ylabel('y')
plt.title(expr)
plt.legend()
plt.grid(True)
plt.show()