import matplotlib.pyplot as plt
import numpy as np

def draw_tree(x, y, angle, depth, ax, branch_length=100):
    if depth == 0:
        return

    # Обчислення кінцевих координат гілки
    new_x = x + branch_length * np.cos(angle)
    new_y = y + branch_length * np.sin(angle)

    # Малюємо гілку
    ax.plot([x, new_x], [y, new_y], color='brown', lw=2)

    # Виклик рекурсії для двох гілок
    new_branch_length = branch_length * 0.7  # Скорочення довжини гілок
    draw_tree(new_x, new_y, angle + np.pi / 4, depth - 1, ax, new_branch_length)  # Ліва гілка
    draw_tree(new_x, new_y, angle - np.pi / 4, depth - 1, ax, new_branch_length)  # Права гілка

# Функція для малювання фрактала "дерево Піфагора"
def pythagoras_tree(depth):
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')

    # Початкова точка дерева
    draw_tree(0, 0, np.pi / 2, depth, ax)

    plt.show()

# Виклик функції
depth = int(input("Введіть рівень рекурсії для дерева Піфагора: "))
pythagoras_tree(depth)
