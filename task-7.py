import random
import matplotlib.pyplot as plt

# Функція для симуляції кидків кубиків
def monte_carlo_dice_simulation(num_simulations):
    results = {i: 0 for i in range(2, 13)}  # Ініціалізація лічильників для сум від 2 до 12

    # Виконуємо симуляцію
    for _ in range(num_simulations):
        dice1 = random.randint(1, 6)  # Кидок першого кубика
        dice2 = random.randint(1, 6)  # Кидок другого кубика
        result_sum = dice1 + dice2
        results[result_sum] += 1  # Підраховуємо кількість появ кожної суми

    # Обчислюємо ймовірність кожної суми
    probabilities = {k: v / num_simulations for k, v in results.items()}
    return probabilities

# Теоретичні ймовірності для порівняння
theoretical_probabilities = {
    2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36,
    7: 6/36, 8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
}

# Симуляція Монте-Карло
num_simulations = 10000  # Кількість симуляцій
simulated_probabilities = monte_carlo_dice_simulation(num_simulations)

# Побудова графіка для порівняння теоретичних та симуляційних ймовірностей
sums = list(theoretical_probabilities.keys())
theoretical_values = [theoretical_probabilities[sum_val] for sum_val in sums]
simulated_values = [simulated_probabilities[sum_val] for sum_val in sums]

plt.figure(figsize=(10, 6))
plt.bar(sums, theoretical_values, alpha=0.6, label='Теоретичні ймовірності', color='blue')
plt.bar(sums, simulated_values, alpha=0.6, label='Симуляція Монте-Карло', color='orange')
plt.xlabel('Сума')
plt.ylabel('Ймовірність')
plt.title('Порівняння ймовірностей (Метод Монте-Карло vs Теоретичні)')
plt.legend()
plt.show()
