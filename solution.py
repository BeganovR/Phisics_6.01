import numpy as np
import matplotlib.pyplot as plt

def electric_field_lines(q1, q2, title):
    # Параметры сетки
    x_min, x_max = -0.5, 1.5
    y_min, y_max = -1.0, 1.0
    density = 1.5  # Плотность линий

    Y, X = np.mgrid[y_min:y_max:200j, x_min:x_max:200j]

    # Координаты зарядов (безразмерные)
    x1_pos, y1_pos = 0.0, 0.0
    x2_pos, y2_pos = 1.0, 0.0

    # r1 и r2 - расстояния от каждой точки сетки до 1-го и 2-го заряда
    r1 = np.sqrt((X - x1_pos)**2 + (Y - y1_pos)**2)
    r2 = np.sqrt((X - x2_pos)**2 + (Y - y2_pos)**2)

    r1[r1 == 0] = 1e-10
    r2[r2 == 0] = 1e-10

    # E = k * q / r^2. Проекция Ex = E * (dx/r) = k * q * dx / r^3
    Ex = q1 * (X - x1_pos) / r1**3 + q2 * (X - x2_pos) / r2**3
    Ey = q1 * (Y - y1_pos) / r1**3 + q2 * (Y - y2_pos) / r2**3

    plt.figure(figsize=(10, 6))
    
    plt.streamplot(X, Y, Ex, Ey, color='black', linewidth=1, density=density, arrowstyle='->')

    c1 = 'red' if q1 > 0 else 'blue'
    c2 = 'red' if q2 > 0 else 'blue'
    plt.plot(x1_pos, y1_pos, marker='o', color=c1, markersize=10, label=f'q1={q1}')
    plt.plot(x2_pos, y2_pos, marker='o', color=c2, markersize=10, label=f'q2={q2}')

    plt.title(title)
    plt.xlabel('x / l')
    plt.ylabel('y / l')
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.grid(True)
    plt.legend()
    plt.gca().set_aspect('equal')
    plt.show()

# 1. Одноименные заряды (отталкивание)
electric_field_lines(q1=1, q2=1, title="Силовые линии одноименных зарядов")

# 2. Разноименные заряды (притяжение)
electric_field_lines(q1=1, q2=-1, title="Силовые линии разноименных зарядов")
