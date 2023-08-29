import timeit

mycode='''
class Node:
    def __init__(self, letter=None, parent=None):
        self.letter = letter
        self.parent = parent
        self.fail_link = None
        self.children = {}
        self.pattern_indexes = []

class CommentzWalter:
    def __init__(self, patterns):
        self.patterns = patterns
        self.trie = self.build_trie()

    def build_trie(self):
        root = Node()
        for pattern_idx, pattern in enumerate(self.patterns):
            current_node = root
            for letter in pattern:
                if letter not in current_node.children:
                    current_node.children[letter] = Node(letter, current_node)
                current_node = current_node.children[letter]
            current_node.pattern_indexes.append(pattern_idx)
        return root

    def set_fail_links(self):
        root = self.trie
        root.fail_link = None
        node_queue = [root]

        while node_queue:
            current_node = node_queue.pop(0)
            for letter, child_node in current_node.children.items():
                fail_node = current_node.fail_link

                while fail_node is not None and letter not in fail_node.children:
                    fail_node = fail_node.fail_link

                if fail_node is None:
                    child_node.fail_link = root
                else:
                    child_node.fail_link = fail_node.children[letter]

                child_node.pattern_indexes += child_node.fail_link.pattern_indexes
                node_queue.append(child_node)

    def search(self, text):
        positions = [-1] * len(self.patterns)
        current_node = self.trie

        for i, letter in enumerate(text):
            while current_node is not None and letter not in current_node.children:
                current_node = current_node.fail_link

            if current_node is None:
                current_node = self.trie
                continue

            current_node = current_node.children[letter]

            for pattern_idx in current_node.pattern_indexes:
                start_pos = i - len(self.patterns[pattern_idx]) + 1
                if start_pos >= 0:
                    positions[pattern_idx] = start_pos

        return positions

text = "ababcbababacbab"
patterns = ["ababaca", "acbab"]
cw = CommentzWalter(patterns)
cw.set_fail_links()
positions = cw.search(text)
for i, pattern in enumerate(patterns):
    print(f"{pattern} found at position {positions[i]}")
'''

exec_time = timeit.timeit(stmt=mycode,number=1) * 10**3
print(f"The time of execution of above program is : {exec_time:.03f}ms")


