import matplotlib.pyplot as plt
import numpy as np

c = [1.0, 0.0, 0.0, -1.0, -0.0, 1.0]


def f(x, c):
    return c[0]+c[1]*x+c[2]*x**2+c[3]*x**3+c[4]*x**4+c[5]*x**5


x = np.arange(-1.5, 1.5, 0.01) #Массив значений аргумента
plt.plot(x, f(x, c)) #Построение графика
plt.xlabel(r'$x$') #Метка по оси x в формате TeX
plt.ylabel(r'$f(x)$') #Метка по оси y в формате TeX
plt.grid(True) #Сетка
plt.ylim(bottom=-0.3, top=1.5)
plt.savefig('1.svg') #Показать график