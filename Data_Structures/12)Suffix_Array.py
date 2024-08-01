class SuffixArray:
    def __init__(self, text):
        self.text = text
        self.n = len(text)
        self.suffix_array = self.build_suffix_array()
    
    def build_suffix_array(self):
        suffixes = [(self.text[i:], i) for i in range(self.n)]
        suffixes.sort()  # Sort suffixes lexicographically
        suffix_array = [suffix[1] for suffix in suffixes]
        return suffix_array

    def build_lcp_array(self):
        rank = [0] * self.n
        lcp = [0] * self.n
        k = 0

        # Build rank array
        for i, suffix in enumerate(self.suffix_array):
            rank[suffix] = i

        # Build LCP array
        for i in range(self.n):
            if rank[i] > 0:
                j = self.suffix_array[rank[i] - 1]
                while (i + k < self.n) and (j + k < self.n) and self.text[i + k] == self.text[j + k]:
                    k += 1
                lcp[rank[i]] = k
                if k > 0:
                    k -= 1

        return lcp

    def search(self, pattern):
        l, r = 0, self.n - 1
        while l <= r:
            mid = (l + r) // 2
            suffix = self.text[self.suffix_array[mid]:]
            if suffix.startswith(pattern):
                return self.suffix_array[mid]
            elif suffix < pattern:
                l = mid + 1
            else:
                r = mid - 1
        return -1  # Pattern not found

    def print_suffix_array(self):
        print("Suffix Array:", self.suffix_array)

    def print_lcp_array(self):
        print("LCP Array:", self.build_lcp_array())
