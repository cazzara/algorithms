from src.node import TreeNode

class BinarySearchTree:
    """

    """
    def __init__(self):
        self.root = None
        self._h = None
        self._v = 0

    @property
    def height(self):
        if self._h:
            return self._h
        if not self.root:
            return -1
        self._h = self._height(self.root)
        return self._h

    @property
    def degree(self):
        return self._v

    def _height(self, r):
        """
        Returns height of subtree rooted at node r
        The height of the tree is the number of edges 
        on the path from the root to farthest the leaf node
        """
        if not r or (r.right is None and r.left is None):
            return 0
        left_height = self._height(r.left)
        right_height = self._height(r.right)
        bigger = left_height if left_height > right_height else right_height
        return bigger + 1

    def insert(self, val):
        self._h = None
        self._v += 1
        self._insert(val, self.root)

    def _insert(self, val, root):
        if not root:
            self.root = TreeNode(val)
            return root

        if val > root.value:
            if not root.right:
                root.right = TreeNode(val)
                root.right.parent = root
                return root.right
            return self._insert(val, root.right)
        if val <= root.value:
            if not root.left:
                root.left = TreeNode(val)
                root.left.parent = root
                return root.left
            return self._insert(val, root.left)

    def search(self, value):
        pass


    def delete(self, value):
        self._h = None
        self._v -= 1
        pass

    def _delete(self, value):
        pass

    def rotate_right(self, node):
        if not node.parent:
            return
        parent = node.parent
        grand_parent = parent.parent
        node.parent = grand_parent
        parent.parent = node
        parent.right = node.right
        node.right = parent
        if grand_parent:
            if parent == grand_parent.left:
                grand_parent.left = node
            else:
                grand_parent.right = node

    def rotate_left(self, node):
        if not node.parent:
            return
        parent = node.parent
        grand_parent = parent.parent
        node.parent = grand_parent
        parent.parent = node
        parent.left = node.left
        node.left = parent
        if grand_parent:
            if parent == grand_parent.left:
                grand_parent.left = node
            else:
                grand_parent.right = node

    def bfs(self, start, fn=print):
        """
        Breadth first traversal of the BST
        """
        if not start:
            return
        fn(start)
        self.bfs(start.left)
        self.bfs(start.right)

    def dfs(self, start, value=None, fn=print):
        """
        Depth first traversal of the BST
        if value is None, returns the full traversal
        """
        if not start:
            return
        self.dfs(start.left)
        self.dfs(start.right)
        fn(start)

    def level_order(self, start, level):
        if not start:
            return
        if level == 1:
            print(start, end=" ")
        self.level_order(start.left, level-1)
        self.level_order(start.right, level-1)

    def print_level_order(self):
        for level in range(1, self.height+2):
            self.level_order(self.root, level)
            print()

    def inorder(self, start, fn=print):
        if not start:
            return
        self.inorder(start.left)
        fn(start)
        self.inorder(start.right)



class SplayTree(BinarySearchTree):
    """
    https://en.wikipedia.org/wiki/Splay_tree
    A Binary Search Tree with the additional property that recently 
    accessed elements are quick to access again.
    """

    def insert(self, val):
        node = self._insert(self, val, self.root)
        self.splay(node)

    def splay(self, node):
        pass
