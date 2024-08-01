class Fenwick_Tree:
    def __init__(self, arr=[]):
        self.tree = [i for i in arr]
        self.len = len(self.tree)
        for i in range(1, self.len):
            j = i+(i & -i)
            if j < self.len:
                self.tree[j] += self.tree[i]

    def prefixsum(self, index):
        sum = 0
        while index > 0:
            sum += self.tree[index]
            # same as index&=~(index&-index) but since this has more bit manipulation, it's faster
            index -= index & -index
        return sum

    def sum(self, left, right):
        return self.prefixsum(right)-self.prefixsum(left-1)

    # add value to current value at index
    def add(self, index, value):
        while index < self.len:
            self.tree[index] += value
            index += index & -index

    def set(self, index, value):
        k = self.sum(index, index)
        self.add(index, value-k)