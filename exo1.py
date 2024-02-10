import matplotlib.pyplot as plt
import numpy as np

def equation(x):
    return x**5 + 0.5

y_ticks = [0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4]
x_ticks = [0, 0.2, 0.4, 0.6, 0.8, 1.0]

x_values = np.linspace(0, 1, 1000)
y_values = equation(x_values)

plt.plot(x_values, y_values, label=r'$x^5 + 0.5$')

plt.fill_between(x_values, y_values, where=((x_values <= 1) & (y_values <= 1)),color='blue', alpha=0.2)
plt.fill_between(x_values, y_values, 1, where=(y_values <= 1), color='green', alpha=0.2)

plt.xticks(x_ticks)
plt.yticks(y_ticks)

# Ajouter des labels et une légende et afficher le graphique
plt.xlabel('x')
plt.ylabel(r'$x^5 + 0.5$')
plt.legend()
plt.grid()
plt.show()
