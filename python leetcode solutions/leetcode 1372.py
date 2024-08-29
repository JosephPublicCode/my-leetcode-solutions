# leetcode 1372

# Longest ZigZag Path in a Binary Tree. 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        self.res = 0 

        def dfs(node, dir, count): 
            if not node: 
                return
            self.res = max(self.res, count)
            
            if dir == 'left': 
                dfs(node.right, 'right', count + 1)
                dfs(node.left, 'left', 1)
                
            if dir == 'right':
                dfs(node.left, 'left', count + 1)
                dfs(node.right, 'right', 1)
                

            
        dfs(root,'right',0)
        dfs(root,'left',0)
        return self.res
    
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        self.res = 0 

        def dfs(node, go_left, count): 
            if not node: 
                return
            self.res = max(self.res, count)
            
            if go_left: 
                dfs(node.right, 'right', count + 1)
                dfs(node.left, 'left', 1)
                
            else:
                dfs(node.left, 'left', count + 1)
                dfs(node.right, 'right', 1)
                

            
        dfs(root,True,0)
        dfs(root, False,0)
        return self.res


        