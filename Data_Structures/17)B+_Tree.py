class BPlusTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t  # Minimum degree
        self.leaf = leaf  # True if leaf node, False otherwise
        self.keys = []  # List of keys
        self.children = []  # List of child BPlusTreeNodes
        self.next = None  # Pointer to the next leaf node (for linked list of leaves)

class BPlusTree:
    def __init__(self, t):
        self.root = BPlusTreeNode(t, True)  # Initialize the root as a leaf node
        self.t = t  # Minimum degree of the B+ tree

    def search(self, k, x=None):
        if x is None:
            x = self.root
        
        i = 0
        while i < len(x.keys) and k > x.keys[i]:
            i += 1

        if i < len(x.keys) and x.keys[i] == k:
            if x.leaf:
                return True
            else:
                return self.search(k, x.children[i])
        
        if x.leaf:
            return False
        
        return self.search(k, x.children[i])

    def insert(self, k):
        root = self.root
        if len(root.keys) == (2 * self.t - 1):
            s = BPlusTreeNode(self.t, False)
            self.root = s
            s.children.append(root)
            self.split_child(s, 0)
            self.insert_non_full(s, k)
        else:
            self.insert_non_full(root, k)

    def insert_non_full(self, x, k):
        if x.leaf:
            i = len(x.keys) - 1
            x.keys.append(None)
            while i >= 0 and k < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            i = len(x.keys) - 1
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            if len(x.children[i].keys) == (2 * self.t - 1):
                self.split_child(x, i)
                if k > x.keys[i]:
                    i += 1
            self.insert_non_full(x.children[i], k)

    def split_child(self, x, i):
        t = self.t
        y = x.children[i]
        z = BPlusTreeNode(t, y.leaf)
        x.children.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t: (2 * t - 1)]
        y.keys = y.keys[0: t - 1]
        if not y.leaf:
            z.children = y.children[t: (2 * t)]

        if y.leaf:
            z.next = y.next
            y.next = z

    def delete(self, k):
        self.delete_node(self.root, k)
        if len(self.root.keys) == 0 and not self.root.leaf:
            self.root = self.root.children[0]

    def delete_node(self, x, k):
        t = self.t
        idx = self.find_key(x, k)
        if idx < len(x.keys) and x.keys[idx] == k:
            if x.leaf:
                x.keys.pop(idx)
            else:
                self.delete_internal_node(x, idx)
        else:
            if x.leaf:
                return
            flag = (idx == len(x.keys))
            if len(x.children[idx].keys) < t:
                self.fill(x, idx)
            if flag and idx > len(x.keys):
                self.delete_node(x.children[idx - 1], k)
            else:
                self.delete_node(x.children[idx], k)

    def delete_internal_node(self, x, idx):
        t = self.t
        k = x.keys[idx]
        if len(x.children[idx].keys) >= t:
            pred = self.get_predecessor(x, idx)
            x.keys[idx] = pred
            self.delete_node(x.children[idx], pred)
        elif len(x.children[idx + 1].keys) >= t:
            succ = self.get_successor(x, idx)
            x.keys[idx] = succ
            self.delete_node(x.children[idx + 1], succ)
        else:
            self.merge(x, idx)
            self.delete_node(x.children[idx], k)

    def get_predecessor(self, x, idx):
        cur = x.children[idx]
        while not cur.leaf:
            cur = cur.children[-1]
        return cur.keys[-1]

    def get_successor(self, x, idx):
        cur = x.children[idx + 1]
        while not cur.leaf:
            cur = cur.children[0]
        return cur.keys[0]

    def fill(self, x, idx):
        t = self.t
        if idx != 0 and len(x.children[idx - 1].keys) >= t:
            self.borrow_from_prev(x, idx)
        elif idx != len(x.keys) and len(x.children[idx + 1].keys) >= t:
            self.borrow_from_next(x, idx)
        else:
            if idx != len(x.keys):
                self.merge(x, idx)
            else:
                self.merge(x, idx - 1)

    def borrow_from_prev(self, x, idx):
        t = self.t
        child = x.children[idx]
        sibling = x.children[idx - 1]
        child.keys.insert(0, x.keys[idx - 1])
        x.keys[idx - 1] = sibling.keys.pop()
        if not child.leaf:
            child.children.insert(0, sibling.children.pop())

    def borrow_from_next(self, x, idx):
        t = self.t
        child = x.children[idx]
        sibling = x.children[idx + 1]
        child.keys.append(x.keys[idx])
        x.keys[idx] = sibling.keys.pop(0)
        if not child.leaf:
            child.children.append(sibling.children.pop(0))

    def merge(self, x, idx):
        t = self.t
        child = x.children[idx]
        sibling = x.children[idx + 1]
        child.keys.append(x.keys[idx])
        child.keys.extend(sibling.keys)
        if not child.leaf:
            child.children.extend(sibling.children)
        x.keys.pop(idx)
        x.children.pop(idx + 1)

    def find_key(self, x, k):
        idx = 0
        while idx < len(x.keys) and x.keys[idx] < k:
            idx += 1
        return idx

    def traverse(self):
        def _traverse(node):
            if node:
                if node.leaf:
                    for key in node.keys:
                        print(key, end=" ")
                    print()
                else:
                    i = 0
                    while i < len(node.keys):
                        _traverse(node.children[i])
                        print(node.keys[i], end=" ")
                        i += 1
                    _traverse(node.children[i])

        _traverse(self.root)
        print()
