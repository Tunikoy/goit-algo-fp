# Жадібний алгоритм
def greedy_algorithm(items, budget):
    # Сортуємо страви за співвідношенням калорій до вартості
    items_sorted = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    total_calories = 0
    selected_items = []

    for item, info in items_sorted:
        if info['cost'] <= budget:
            selected_items.append(item)
            total_calories += info['calories']
            budget -= info['cost']
    
    return selected_items, total_calories

# Алгоритм динамічного програмування
def dynamic_programming(items, budget):
    # Ініціалізуємо таблицю для динамічного програмування
    dp = [0] * (budget + 1)
    selected_items_by_cost = [[] for _ in range(budget + 1)]

    # Обчислюємо максимальні калорії для кожної вартості
    for item, info in items.items():
        cost = info['cost']
        calories = info['calories']
        for b in range(budget, cost - 1, -1):
            if dp[b - cost] + calories > dp[b]:
                dp[b] = dp[b - cost] + calories
                selected_items_by_cost[b] = selected_items_by_cost[b - cost] + [item]

    # Повертаємо оптимальні страви і максимальну кількість калорій
    return selected_items_by_cost[budget], dp[budget]

# Дані про страви
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Заданий бюджет
budget = 100

# Використовуємо жадібний алгоритм
selected_items_greedy, total_calories_greedy = greedy_algorithm(items, budget)
print(f"Жадібний алгоритм: обрані страви {selected_items_greedy}, сумарні калорії: {total_calories_greedy}")

# Використовуємо динамічне програмування
selected_items_dp, total_calories_dp = dynamic_programming(items, budget)
print(f"Динамічне програмування: обрані страви {selected_items_dp}, сумарні калорії: {total_calories_dp}")
