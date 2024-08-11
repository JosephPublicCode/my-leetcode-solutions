# leetcode 543

# Diameter of Binary Tree

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def diameterOfBinaryTree(self, root: list[TreeNode]) -> int:
        res = [0]

        def dfs(root):
            if not root: 
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            res[0] = max(res[0],2 + left + right)

            return 1 + max(left,right)
        
        dfs(root)
        return res 
# O(N) Time complexeity
# O(N) Space complexeity 

'''
Method: 
recursive dfs helper function. post order style implementation
1. base case returns -1: 
- this is so the maths of adding up the nodes 
    to get the diameter works
2. left and right dfs
3. return max of current and previous
- current  = left height and right height + 1 

'''








class Solution:
    def diameterOfBinaryTree(self, root: list[TreeNode]) -> int:
        return self.diameterOfBinaryTreeActual(root) -1
        
        
    def diameterOfBinaryTreeActual(self, root: list[TreeNode]) -> int:
        if not root: 
            return 0  
        lheight = self.maxHeight(root.left)
        rheight = self.maxHeight(root.right)

        lDiameter = self.diameterOfBinaryTreeActual(root.left)
        rDiameter = self.diameterOfBinaryTreeActual(root.right)

        return max(lheight + rheight + 1, max(lDiameter,rDiameter))

   
    def maxHeight(self,root:list[TreeNode]) -> int: 
        if not root: 
            return 0 
        return 1 + max(self.maxHeight(root.left),self.maxHeight(root.right))
    



