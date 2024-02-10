import matplotlib.pyplot as plt
import numpy as np

class Curve:
    def __init__(self, start, stop, nbr_points=5432):
        self.start = start
        self.stop = stop
        self.nbr_points = nbr_points
        self.x_values = np.linspace(start, stop, nbr_points)
        self.y_values = self._compute_y_values()

    def _compute_y_values(self):
        return self.x_values ** 5

    def plot_curve(self):
        plt.plot(self.x_values, self.y_values, label=r'$x^5$')

    def point_position(self, x, y):
        if y > x**5:
            return "above"
        elif y < x**5:
            return "below"
        else:
            return "on the curve"

    def generate_and_plot_points(self):
        for x, y in zip(self.x_values, self.y_values):
            position = self.point_position(x, y)
            if position == "above":
                plt.scatter(x, y, c='b')
            else:
                plt.scatter(x, y, c='g')

    def calculate_blue_area(self):
        blue_area = 0
        for x, y in zip(self.x_values, self.y_values):
            if y > x**5:
                blue_area += y - x**5
        return blue_area

    def calculate_green_area(self):
        green_area = 0
        for x, y in zip(self.x_values, self.y_values):
            if y <= x**5:
                green_area += x**5 - y
        return green_area


curve = Curve(0, 1)
curve.plot_curve()
curve.generate_and_plot_points()

blue_area = curve.calculate_blue_area()
green_area = curve.calculate_green_area()

print(f"Surface en bleu : {blue_area}")
print(f"Surface en vert : {green_area}")

plt.xlabel('x')
plt.ylabel(r'$x^5$')
plt.legend()
plt.grid()
plt.show()
