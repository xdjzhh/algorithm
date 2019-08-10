class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 0


class AVLTree:
    def __init__(self):
        self.root = None

    def find(self, key):
        if self.root is None:
            return None
        else:
            return self._find(key, self.root)

    def _find(self, key, node):
        if node is None:
            return None
        elif key < node.key:
            return self._find(key, self.left)
        elif key > node.key:
            return self._find(key, self.right)
        else:
            return node

    def findMin(self):
        if self.root is None:
            return None
        else:
            return self._findMin(self.root)

    def _findMin(self, node):
        if node.left:
            return self._findMin(node.left)
        else:
            return node

    def findMax(self):
        if self.root is None:
            return None
        else:
            return self._findMax(self.root)

    def _findMax(self, node):
        if node.right:
            return self._findMax(node.right)
        else:
            return node

    def height(self, node):
        if node is None:
            return -1
        else:
            return node.height

    # 前序遍历
    def Preorder(self):
        if self.root:
            self.preorder(self.root)
            print()

    def preorder(self, node):
        if node:
            print(node.key, end="")
            self.preorder(node.left)
            self.preorder(node.right)

    # 右旋
    def rotate_right(self, node):
        k = node.left
        node.left = k.right
        k.right = node
        node.height = max(self.height(node.left), self.height(node.right)) + 1
        k.height = max(self.height(k.left), node.height) + 1
        return k

    # 左旋
    def rotate_left(self, node):
        k = node.right
        node.right = k.left
        k.left = node
        node.height = max(self.height(node.left), self.height(node.right)) + 1
        k.height = max(self.height(k.right), node.height) + 1
        return k

    # 左右双旋
    def rotate_le_ri(self, node):
        node.left = self.rotate_left(node.left)
        return self.rotate_right(node)

        # 右左双旋

    def rotate_ri_le(self, node):
        node.right = self.rotate_right(node.right)
        return self.rotate_left(node)

    def Insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self.root = self.insert(key, self.root)

    def insert(self, key, node):
        if not node:
            node = Node(key)
        elif key < node.key:
            node.left = self.insert(key, node.left)
            if self.height(node.left) - self.height(node.right) == 2:
                if key < node.left.key:
                    # 左左
                    node = self.rotate_right(node)
                else:
                    # 左右
                    node = self.rotate_le_ri(node)
        elif key > node.key:
            node.right = self.insert(key, node.right)
            if self.height(node.right) - self.height(node.left) == 2:
                if key > node.right.key:
                    node = self.rotate_left(node)
                else:
                    node = self.rotate_ri_le(node)
        node.height = max(self.height(node.left), self.height(node.right)) + 1
        return node

    def Remove(self, key):
        if self.root is None:
            raise KeyError("No such key found!")
        else:
            self.root = self.remove(key, self.root)

    def remove(self, key, node):
        if node is None:
            print("No such key found!")
        elif key < node.key:
            node.left = self.remove(key, node.left)
            if self.height(node.right) - self.height(node.left) == 2:
                if self.height(node.right.right) >= self.height(node.right.left):
                    node = self.rotate_left(node)
                else:
                    node = self.rotate_ri_le(node)
            node.height = max(self.height(node.left), self.height(node.right)) + 1
        elif key > node.key:
            node.right = self.remove(key, node.right)
            if self.height(node.left) - self.height(node.right) == 2:
                if self.height(node.left.right) > self.height(node.left.left):
                    node = self.rotate_le_ri(node)
                else:
                    node = self.rotate_right(node)
            node.height = max(self.height(node.left), self.height(node.right)) + 1
        elif node.left and node.right:
            # 左右孩子都有
            if self.height(node.left) >= self.height(node.right):
                # 左比右高，那么右子树找最小的放上来做根
                k = self._findMin(node.right)
                node.key = k.key
                node.right = self.remove(k.key, node.right)
            else:
                # 左比右低，那么左子树找最大的放上来做根
                k = self._findMax(node.left)
                node.key = k.key
                node.left = self.remove(k.key, node.left)
            node.height = max(self.height(node.left), self.height(node.right)) + 1
        else:
            # 只有左孩子或右孩子或都没有
            if node.left:
                node = node.left
            else:
                # 叶子节点也算在此情况
                node = node.right
        return node


p=AVLTree()
p.Insert(5)
p.Preorder()
p.Insert(4)
p.Preorder()
p.Insert(6)
p.Preorder()
p.Insert(1)
p.Preorder()
p.Insert(3)
p.Preorder()
p.Remove(6)
p.Preorder()
