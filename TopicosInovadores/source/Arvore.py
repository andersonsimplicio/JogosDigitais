class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current_node, key):
        if key < current_node.val:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert_recursive(current_node.left, key)
        else:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert_recursive(current_node.right, key)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, current_node, key):
        if current_node is None or current_node.val == key:
            return current_node
        if key < current_node.val:
            return self._search_recursive(current_node.left, key)
        return self._search_recursive(current_node.right, key)

    def inorder_traversal(self):
        return self._inorder_traversal_recursive(self.root)

    def _inorder_traversal_recursive(self, current_node):
        res = []
        if current_node:
            res = self._inorder_traversal_recursive(current_node.left)
            res.append(current_node.val)
            res = res + self._inorder_traversal_recursive(current_node.right)
        return res

# Exemplo de uso
if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(7)
    bst.insert(3)
    bst.insert(9)
    bst.insert(1)
    bst.insert(5)

    print("Inorder Traversal:", bst.inorder_traversal())
    print("Buscar 5:", bst.search(5) is not None)
    print("Buscar 10:", bst.search(10) is not None)