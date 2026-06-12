class PrefixTree:
    class TrieNode:
        def __init__(self, value=None, is_word = False):
            self.value = value
            self.children = []
            self.is_word = is_word
    def __init__(self):
        self.root = self.TrieNode()

    def in_children(self, trie_node: TrieNode, c: str) -> TrieNode:
        for child in trie_node.children:
            if child.value == c:
                return child
        
        return None
    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            node_to_go = self.in_children(cur, c)
            if node_to_go:
                cur = node_to_go
            else:
                next_node = self.TrieNode(c)
                cur.children.append(next_node)
                cur = next_node
        cur.is_word = True
    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            node_to_go = self.in_children(cur, c)
            if node_to_go:
                cur = node_to_go
            else:
                return False
        
        return cur.is_word

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            node_to_go = self.in_children(cur, c)
            if node_to_go:
                cur = node_to_go
            else:
                return False
        
        return True
        