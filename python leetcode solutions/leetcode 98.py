# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: list[TreeNode]) -> bool:
        max,min  = root.val, root.val
        
        def dfs(root, left, right):
            if not root: 
                return True
            if not (root.val < right and root.val > left):
                return False
            return (dfs(root.left, left, root.val) and 
            dfs(root.right,root.val,right))
        return dfs(root,float('-inf'),float('inf'))
    
# Time Complexeity: O(N)
# Space Complexeity: O(N)

'''
Defintion of a BST:
- the left subtree of a given node contains only nodes with keys less than that nodes key.
- the right subtree of a given node contains only nodes with keys greater than taht nodes key.
- both left and right subtrees must themselves be BSTs.

Note: an empty tree is itself a BST. 

Method:
recursive dfs helper function. 
1. check the root.val is less than right and root.val is greater than left
2. return dfs on the left and right nodes, updating the left and right where appropriate.
left and right start at -inf and +inf respectively as no limitations for left and right
have yet been placed on the tree. 

As you run through this algorithm, rather than checking 
all values in the subtree we use boundaries that we adjust as we continue running the algorithm. 
'''
