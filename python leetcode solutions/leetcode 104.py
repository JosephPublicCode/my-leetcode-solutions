# leetcode 104 

# Maximum Depth of Binary Tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def maxHeight(self,root:list[TreeNode]) -> int: 
        if not root: 
            return 0 
        return 1 + max(self.maxHeight(root.left),self.maxHeight(root.right))
    
# O(n) Time Complexeity
# O(1) Space Complexeity

'''
Method: 
recursive dfs or iterative BFS with queue or iterative dfs with stack. 

'''

# BFS - Iterative appraoch
# uses a queue

class Solution:

    def maxHeight(self,root:list[TreeNode]) -> int: 
        if not root: 
            return 0
        level = 1 
        queue = [root]
        while queue: 

            for i in range(len(queue)):
                node = queue.pop(0)
                if node.left: 
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return level
    
# DFS - Iterative approach 
# using a stack 

class Solution:

    def maxHeight(self,root:list[TreeNode]) -> int: 
        stack = [[root,1]]
        res = 0 
        while stack: 

            node, depth = stack.pop()
            if node: 
                res = max(res,depth)

                stack.append([node.left,depth + 1])
                stack.append([node.right, depth +1])
        return res