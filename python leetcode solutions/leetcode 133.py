# leetcode 133 

# Clone Graph 


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        copy_store = {}

        def dfs(node): 
            
            if node in copy_store: 
                return copy_store[node]
            copy = Node(node.val)
            copy_store[node] = copy
            for neighbor in node.neighbors: 
                copy.neighbors.append(dfs(neighbor))
            return copy
        return dfs(node) if node else None
# Time Complexeity: O(n)
# Space Complexeity: O(n) 

'''
Method: 
Recursive dfs helper function solution. 
1. initialize a map for the copy graph. 
2. if node in the map then return
3. make a copy of the current node. 
4. add to the map
5. append all of the old neighbors to the copy and return the copy. 

'''

# Implement with BFS and iterative DFS