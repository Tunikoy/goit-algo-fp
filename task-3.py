import heapq

def dijkstra(graph, start):
    # Ініціалізація: всі відстані ставимо дуже великими
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  # Відстань до стартової вершини = 0
    priority_queue = [(0, start)]  # Купа, починаємо зі стартової вершини (відстань, вершина)
    shortest_path_tree = {}  # Відстежуємо шляхи для кожної вершини

    while priority_queue:
        # Витягуємо вершину з найменшою відстанню
        current_distance, current_node = heapq.heappop(priority_queue)

        # Якщо поточна відстань більша, ніж та, що вже збережена, пропускаємо цю вершину
        if current_distance > distances[current_node]:
            continue

        # Оновлюємо відстані до сусідів поточного вузла
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Якщо знайдений шлях коротший
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))  # Додаємо сусіда до купи
                shortest_path_tree[neighbor] = current_node  # Зберігаємо шлях

    return distances, shortest_path_tree

# Приклад графа у вигляді словника
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Запуск алгоритму Дейкстри
start_node = 'A'  # Стартуємо з вершини A
distances, shortest_path_tree = dijkstra(graph, start_node)

# Виведення результатів
print(f"Відстані від стартової вершини {start_node}: {distances}")
print(f"Шляхи: {shortest_path_tree}")