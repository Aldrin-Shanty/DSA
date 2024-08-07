"""
Trie Data Structure

A Trie, also known as a prefix tree, is a specialized tree-like data structure used for storing and querying strings,
where each node represents a single character of a string. It is particularly efficient for operations related to prefixes and is commonly used in
applications that involve searching for words or prefixes.

Operations:
1. **Insert**: Inserts a word into the Trie. Each character of the word is stored in a separate node, and the end of the word is marked in the final node.
2. **CountWordsWithPrefix**: Counts the number of words in the Trie that start with the given prefix. It navigates to the end of the prefix and counts all words that can be formed from this point.

Time Complexity:
    - **Insert**: O(m), where m is the length of the word being inserted. 
        Each character is processed once, and each insertion operation involves creating nodes for new characters if they do not already exist.
    - **CountWordsWithPrefix**: O(m + k), where m is the length of the prefix and k is the number of words with that prefix. 
        The method first traverses the Trie to find the end of the prefix, then recursively counts all words starting from that node.

Applications:
    - **Autocomplete Systems**: Tries are used in search engines and text editors to provide suggestions based on user input.
    - **Spell Checking**: Tries can efficiently verify if a word is present in a dictionary.
    - **IP Routing**: Used in networking to efficiently match IP addresses and prefixes.
    - **Pattern Matching**: Useful in various algorithms and systems for efficient pattern matching and substring search.
"""

class TrieNode:
    """
    A node in the Trie data structure.

    Attributes:
        children (dict): A dictionary mapping characters to child TrieNodes.
        is_end_of_word (bool): A flag indicating if the node marks the end of a word.
    """
    def __init__(self):
        """
        Initialize a new TrieNode.
        """
        self.children = {}
        self.is_end_of_word = False


class Trie:
    """
    A Trie (prefix tree) data structure for storing and querying words.

    Attributes:
        root (TrieNode): The root node of the Trie.
    """
    def __init__(self):
        """
        Initialize an empty Trie.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Insert a word into the Trie.

        Args:
            word (str): The word to be inserted into the Trie.

        Returns:
            None
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def count_words_with_prefix(self, prefix: str) -> int:
        """
        Count the number of words in the Trie that start with the given prefix.

        Args:
            prefix (str): The prefix to search for.

        Returns:
            int: The number of words that start with the given prefix.
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return self._count_words_from_node(node)

    def _count_words_from_node(self, node: TrieNode) -> int:
        """
        Recursively count the number of words starting from a given TrieNode.

        Args:
            node (TrieNode): The starting TrieNode.

        Returns:
            int: The number of words starting from the given TrieNode.
        """
        count = 0
        if node.is_end_of_word:
            count += 1
        for child in node.children.values():
            count += self._count_words_from_node(child)
        return count

if __name__ == "__main__":
     # Create a new Trie
    trie = Trie()

    # Insert words into the Trie
    trie.insert("apple")
    trie.insert("app")
    trie.insert("applet")
    trie.insert("bat")
    trie.insert("batch")

    # Test count_words_with_prefix
    print("Count words with prefix 'app':", trie.count_words_with_prefix("app"))     # Expected output: 3
    print("Count words with prefix 'appl':", trie.count_words_with_prefix("appl"))   # Expected output: 2
    print("Count words with prefix 'bat':", trie.count_words_with_prefix("bat"))     # Expected output: 2
    print("Count words with prefix 'b':", trie.count_words_with_prefix("b"))         # Expected output: 2
    print("Count words with prefix 'x':", trie.count_words_with_prefix("x"))         # Expected output: 0