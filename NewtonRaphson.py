import sympy as sp

# Mendefinisikan simbol dan fungsi
x = sp.symbols('x')
f = x**3 - 2*x**2 + x - 3

# Menghitung turunan pertama
f_prime = sp.diff(f, x)

# Fungsi untuk metode Newton-Raphson
def newtonRaphson(initial_guess, tolerance=1e-6):
    x_n = initial_guess
    max_iterations = 100

    for i in range(max_iterations):
        f_value = f.subs(x, x_n)
        f_prime_value = f_prime.subs(x, x_n)

        x_n1 = x_n - f_value / f_prime_value
        
        if abs(x_n1 - x_n) < tolerance:
            print(f"Converged to root {x_n1} in {i} iterations.")
            return x_n1

        x_n = x_n1

    print(f"Newton-Raphson did not converge after {max_iterations} iterations.")
    return None

    print(f"Newton-Raphson did not converge after {max_iterations} iterations.")
    return None

# Mencoba metode Newton-Raphson dengan tebakan awal x0
x0 = 4.0
result = newtonRaphson(x0)
if result is not None:
    print("The value of the root is:", result)
