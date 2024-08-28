# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root,maxVal):
            if not root: 
                return 0 
            res = 1 if root.val >= maxVal else 0 
            maxVal = max(root.val, maxVal)
            res += dfs(root.left,maxVal)
            res += dfs(root.right,maxVal)
            return res
           
        return dfs(root,root.val)


#O(N) time complexeity and O(N) space complexeity

# Multiple similar solutions that I have implemented as I have done this question multiple times.

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root:TreeNode,maximum):
            if not root:
                return 0
            if root.val >= maximum:
                maximum = max(root.val, maximum)
                res = 1
            else:
                res = 0
            res += dfs(root.left,maximum)
            res += dfs(root.right,maximum)
            return res
        return dfs(root,root.val)

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0

        def dfs(node, cur_max):
            if not node:
                return
            if node.val >= cur_max:
                cur_max = node.val
                self.count += 1
            dfs(node.left, cur_max)
            dfs(node.right,cur_max)

        dfs(root,root.val)
        return self.count
