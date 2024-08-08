# leetcode 226 

# invert binary tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution():
    def invertTree(self, root: list[TreeNode]) -> list[TreeNode]:
        if not root: 
            return None
        tmp = root.left
        root.left = root.right
        root.right = tmp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

# Time Complexeity O(n)
# Space Complexeity O(1)
    
    
'''
method:
1. recursive call of invert tree. 
2. swap left and right with use of tmp variable. 
3. base case is not root. 

'''