# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: list[TreeNode]) -> bool:
        if root is None: 
            return True
        leftTree = self.getTreeHeight(root.left)
        rightTree = self.getTreeHeight(root.right)
        return abs(leftTree-rightTree) <= 1  and self.isBalanced(root.left)\
                                             and self.isBalanced(root.right)
    
    def getTreeHeight(self,root:list[TreeNode]) -> int: 
        if root is None:
            return 0 
        
        return 1 + max(self.getTreeHeight(root.left),self.getTreeHeight(root.right))

# Time Complexeity: O(n)
# Space complexeity: O(n)

'''
Method: 

1. recursive dfs solution.
2. check criteria for a balanced BT recursively and \
    the height difference betweent the left and right trees
3. tree helper height function. 


Requirements for a balanced binary tree: 
- the height difference between the left and right subtrees must be at most one. 
- each subtree must also be balanced. 
'''