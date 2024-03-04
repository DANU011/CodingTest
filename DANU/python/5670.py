import sys
input_func = sys.stdin.readline

class Node:
    def __init__(self, character):
        self.character = character
        self.children = {}
        self.count = 0
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = Node('R')

    def insert(self, string):
        current = self.root

        for char in string:
            if not current.children.get(char):
                current.children[char] = Node(char)
            
            current = current.children[char]
            current.count += 1

        current.is_end = True

    def dfs(self, node, type_count):
        if node.count == 1:
            return type_count

        res = 0
        if node.is_end:
            res += type_count

        for next_node in node.children.values():
            if node.count == next_node.count:
                next_type_count = type_count
            else:
                next_type_count = type_count + 1

            res += self.dfs(next_node, next_type_count)

        return res

if __name__ == '__main__':
    while True:
        try:
            n = int(input_func())  
        except:
            break

        trie = Trie()    
        for _ in range(n):               
            trie.insert(str(input_func().rstrip()))

        print('%0.2f' % (trie.dfs(trie.root, 0) / n))
