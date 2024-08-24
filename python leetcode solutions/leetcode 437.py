# leetcode 437

# Path Sum III 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        self.count = 0 
        self.key = {0:1}

        def dfs(node,run_sum): 
            if not node: 
                return
            
            run_sum += node.val
            x = run_sum - targetSum
            self.count += self.key.get(x,0)
            
            self.key[run_sum] = self.key.get(run_sum,0) + 1 
            dfs(node.left, run_sum)
            dfs(node.right, run_sum)
            self.key[run_sum] = self.key.get(run_sum,0) - 1 
        
        dfs(root,0)
        return self.count
    
# O(N) time and space complexeity

'''
Method: 
dfs with dictionary and backtracking
1. setup a counter and a dictionary
2. populate the dictionary with {0:1}
3. create a helper dfs function
4. increment the run sum by the node value
5. check the dictionary for the run_sum-targetSum
6. increment the count depending on the value of the key in the dictionary if found
7. add run sum to the dictionary, 
8. run dfs on left and right
9. remove the run sum - backtracking component
10. run the dfs and return the count. 
'''

# recursive brute force approach. 

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        self.count = 0 

        def helper(node, cur_sum): 
            if not node: 
                return 
            if cur_sum == targetSum: 
                self.count += 1 
            
            helper(node.left, cur_sum + node.val)
            helper(node.right, cur_sum + node.val)

            

        def dfs(node): 
            if not node: 
                return
        
            helper(node, 0)
            dfs(node.left)
            dfs(node.right)

        dfs(root,0)
        return self.count
# O(N^2) time complexeity


# approach using a default dictionary.  
from collections import defaultdict

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        self.count = 0 
        self.key = defaultdict(int)
        self.key[0] += 1 

        def dfs(node,run_sum): 
            if not node: 
                return
            
            run_sum += node.val
            x = run_sum - targetSum
            self.count += self.key[x]
            
            self.key[run_sum] += 1 
            dfs(node.left, run_sum)
            dfs(node.right, run_sum)
            self.key[run_sum] -= 1 
        
        dfs(root,0)
        return self.count