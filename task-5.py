import uuid
import networkx as nx
import matplotlib.pyplot as plt
import random

# Клас вузла дерева
class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

# Додавання ребер для побудови графа
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

# Функція для візуалізації дерева
def draw_tree(tree_root, visited_nodes, title):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [visited_nodes.get(node[0], node[1]['color']) for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Функція для обходу в глибину (DFS) з використанням стека
def dfs_traversal(root):
    stack = [root]
    visited_nodes = {}
    step = 0

    while stack:
        node = stack.pop()
        if node is not None:
            # Генеруємо колір на основі порядку обходу
            visited_nodes[node.id] = f"#{hex(0x1296F0 + step * 1000)[2:]}"
            step += 1
            stack.append(node.right)
            stack.append(node.left)

            draw_tree(root, visited_nodes, title=f"DFS: Крок {step}")
    return visited_nodes

# Функція для обходу в ширину (BFS) з використанням черги
def bfs_traversal(root):
    queue = [root]
    visited_nodes = {}
    step = 0

    while queue:
        node = queue.pop(0)
        if node is not None:
            # Генеруємо колір на основі порядку обходу
            visited_nodes[node.id] = f"#{hex(0x1296F0 + step * 1000)[2:]}"
            step += 1
            queue.append(node.left)
            queue.append(node.right)

            draw_tree(root, visited_nodes, title=f"BFS: Крок {step}")
    return visited_nodes

# Створення дерева для прикладу
def build_tree():
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)
    return root

# Головна функція для виконання
def main():
    root = build_tree()

    # Обхід в глибину (DFS)
    print("Обхід в глибину (DFS):")
    dfs_traversal(root)

    # Обхід в ширину (BFS)
    print("Обхід в ширину (BFS):")
    bfs_traversal(root)

if __name__ == "__main__":
    main()
