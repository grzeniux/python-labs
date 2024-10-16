# Zadanie 6
# Zaimplementuj klasę, która będzie realizowała strukturę drzewa 
# (powinna posiadać funkcję przechodzenia wszystkich węzłów drzewa, 
# węzły powinny mieć możliwość przechowywania wartości, 
# krawędzie także mogą zawierać wartości lub być oznaczone), klasa powinna mieć zdefiniowaną funkcję __str__

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = {}

    def add_child(self, child_node, edge_value=None):
        """Dodajemy dziecko do węzła z opcjonalną wartością krawędzi."""
        self.children[child_node] = edge_value

    def __str__(self, level=0):
        """Rekurencyjna funkcja do wypisywania drzewa w czytelnej formie."""
        ret = "  " * level + repr(self.value) + "\n"
        for child, edge_value in self.children.items():
            if edge_value is not None:
                ret += "  " * (level + 1) + f"(krawędź: {edge_value})" + "\n"
            ret += child.__str__(level + 1)
        return ret

class Tree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

    def dfs_traversal(self):
        """Przechodzenie drzewa w głąb (DFS)."""
        visited_nodes = []
        self._dfs(self.root, visited_nodes)
        return visited_nodes

    def _dfs(self, node, visited):
        """Rekurencyjna funkcja przechodzenia w głąb."""
        visited.append(node.value)
        for child in node.children:
            self._dfs(child, visited)

    def __str__(self):
        """Zwraca czytelną reprezentację drzewa."""
        return str(self.root)


tree = Tree("Audi")
sedan_audi = TreeNode("Sedan")
kombi_audi = TreeNode("Kombi")
tree.root.add_child(sedan_audi)
tree.root.add_child(kombi_audi)

diesel_audi_sedan = TreeNode("Diesel")
petrol_audi_sedan = TreeNode("Benzyna")
sedan_audi.add_child(diesel_audi_sedan)
sedan_audi.add_child(petrol_audi_sedan)

diesel_audi_kombi = TreeNode("Diesel")
petrol_audi_kombi = TreeNode("Benzyna")
kombi_audi.add_child(diesel_audi_kombi)
kombi_audi.add_child(petrol_audi_kombi)

print(tree)

visited_nodes = tree.dfs_traversal()
print(f"Odwiedzone węzły (DFS): {visited_nodes}")