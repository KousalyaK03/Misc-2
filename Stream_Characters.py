# Approach:
# We use a Trie (prefix tree) to store the reversed words so we can efficiently check suffixes.
# Instead of searching forward, we store words in reverse order in the Trie.
# As each character is queried, we keep track of the recent characters and check for matches in the Trie.
# This ensures we can efficiently determine if a suffix matches any word in the given list.

# Time Complexity: 
# - Initialization: O(M), where M is the total number of characters in all words.
# - Query: O(L), where L is the length of the longest word in the list.
# Space Complexity: O(M), since we store all words in the Trie.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False  # Marks the end of a word

class StreamChecker:
    def __init__(self, words: List[str]):
        self.trie = TrieNode()  # Initialize Trie
        self.stream = []  # Store the characters from the query in reverse order

        # Insert words into the Trie in reverse order
        for word in words:
            node = self.trie
            for char in reversed(word):  # Store words in reverse order
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end = True  # Mark the end of a word
        
    def query(self, letter: str) -> bool:
        self.stream.append(letter)  # Add character to the stream

        node = self.trie
        # Check if any suffix matches a word in the Trie
        for char in reversed(self.stream):  # Check in reverse order
            if char not in node.children:
                return False  # No matching suffix
            node = node.children[char]
            if node.is_end:  # Found a complete word match
                return True
        
        return False  # No matching suffix found
