"""
A Suffix Array is a data structure that provides a sorted array of all suffixes of a given text. 
It is useful for efficient string searching, substring queries, and text processing.

Operations:
1. **Initialization of Suffix Array**: Constructs the suffix array by sorting all suffixes of the text lexicographically.
2. **Initialization of LCP Array**: Constructs the Longest Common Prefix (LCP) array for the suffix array.
    The LCP array indicates the length of the longest common prefix between each pair of consecutive suffixes.
3. **Search**: Searches for the given pattern in the text using binary search on the suffix array.
    Returns the starting index of the first occurrence of the pattern if found, otherwise -1.
4. **Print Suffix Array**: Prints the suffix array.
5. **Print LCP Array**: Prints the LCP array.

Time Complexity:
    - **Initialization of Suffix Array**: O(n log n), where n is the length of the text.
    - **Initialization of LCP Array**: O(n), where n is the length of the text.
    - **Search**: O(m log n), where m is the length of the pattern and n is the length of the text.

Applications:
    - Efficient substring search and pattern matching.
    - Text indexing and retrieval in search engines.
    - Data compression algorithms and bioinformatics for DNA sequence analysis.
"""


class SuffixArray:
    """
    A Suffix Array is a data structure that provides a sorted array of all suffixes of a given text. 
    It is useful for efficient string searching, substring queries, and text processing.

    Attributes:
        text (str): The input text for which the suffix array is constructed.
        n (int): The length of the input text.
        suffix_array (list[int]): The sorted array of starting indices of all suffixes of the text.
    """
    def __init__(self, text: str):
        """
        Initializes the SuffixArray with the given text.
        """
        self.text = text
        self.n = len(text)
        self.suffix_array = self.build_suffix_array()
    
    def build_suffix_array(self) -> list[int]:
        """
        Constructs the suffix array by sorting all suffixes of the text lexicographically.

        Returns:
            list[int]: The sorted array of starting indices of all suffixes of the text.
        """
        suffixes = [(self.text[i:], i) for i in range(self.n)]
        suffixes.sort()  # Sort suffixes lexicographically
        suffix_array = [suffix[1] for suffix in suffixes]
        return suffix_array

    def build_lcp_array(self) -> list[int]:
        """
        Constructs the Longest Common Prefix (LCP) array for the suffix array.

        Returns:
            list[int]: The LCP array, where lcp[i] indicates the length of the longest common prefix 
            between the suffixes starting at self.suffix_array[i] and self.suffix_array[i-1].
        """
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

    def search(self, pattern: str) -> int:
        """
        Searches for the given pattern in the text using binary search on the suffix array.

        Args:
            pattern (str): The pattern to search for in the text.

        Returns:
            int: The starting index of the first occurrence of the pattern if found, otherwise -1.
        """
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

    def print_suffix_array(self) -> None:
        """
        Prints the suffix array.
        """
        print("Suffix Array:", self.suffix_array)

    def print_lcp_array(self) -> None:
        """
        Prints the LCP array.
        """
        print("LCP Array:", self.build_lcp_array())