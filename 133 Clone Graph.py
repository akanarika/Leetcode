# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None
            
        new_root = UndirectedGraphNode(node.label)
        s = [node]
        d = {node: new_root}
        while s:
            u = s.pop()
            for i in u.neighbors:
                if i not in d:
                    new_node = UndirectedGraphNode(i.label)
                    d[i] = new_node
                    s.append(i)
                d[u].neighbors.append(d[i])
        
        return new_root
                