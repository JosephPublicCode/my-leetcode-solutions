# leetcode 872

# similar leaf nodes


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution: 
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:

        def dfs(root,order):
            if root.left == None and root.right == None: 
                order.append(root.val)
                return order
                
            if root.right: dfs(root.right,order)
            if root.left: dfs(root.left, order)
            return order

        return dfs(root1,[]) == dfs(root2,[])
    
# Time Complexeity: O(N + M)
# Space complexeity: O(N + M)