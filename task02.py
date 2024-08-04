import numpy as np
import scipy.integrate as sci
import matplotlib.pyplot as plt
import scipy.integrate as spi

def f(x):
    return x ** 2

a = 0   
b = 2   

 
# Метод Монте-Карло 

def mc_method(a, b, num_samples):

    x = np.random.uniform(a, b, num_samples)
    y = np.random.uniform(0, f(b), num_samples)

    points_under_curve = np.sum(y <= f(x))

    total_area = (b - a) * f(b)
    return total_area * points_under_curve / num_samples


num_samples = [100, 1000, 10000, 100000, 1000000]
for sample in num_samples:
    print(f"Метод Монте-Карло:{mc_method(0,2,num_samples=sample)}, при кількості точок: {sample}")


quad_result, _ = spi.quad(f, a, b)
print(f"Функція quad: {quad_result}")


# Побудова графіку  
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