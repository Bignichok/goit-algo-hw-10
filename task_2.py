import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначення функції
def f(x):
    return x ** 2

# Метод Монте-Карло для обчислення інтегралу
def monte_carlo_integration(func, a, b, num_points=10000):
    x_random = np.random.uniform(a, b, num_points)
    y_random = func(x_random)
    integral_mc = (b - a) * np.mean(y_random)
    return integral_mc

# Межі інтегрування
a = 0
b = 2

# Аналітичний інтеграл за допомогою функції quad
result_quad, error = spi.quad(f, a, b)
print("Інтеграл (quad): ", result_quad)

# Обчислення інтегралу методом Монте-Карло
integral_mc = monte_carlo_integration(f, a, b)
print("Інтеграл (Монте-Карло): ", integral_mc)

# Графічне зображення
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()
