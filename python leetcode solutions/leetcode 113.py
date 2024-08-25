# leetcode 133 

# Path Sum II 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> list[list[int]]:
        self.paths = []

        if not root: 
            return self.paths

        
        def dfs(node, order,cur_sum): 

            cur_sum += node.val
            order.append(node.val)

            if not node.left and not node.right: 
                
                if cur_sum == targetSum: 
                    self.paths.append(order[:])
                cur_sum -= node.val
                order.pop()
                return


            if node.left: 
                dfs(node.left, order, cur_sum)
            if node.right: 
                dfs(node.right, order, cur_sum)
            
            cur_sum -= node.val
            order.pop()

            
        
        dfs(root, [], 0)
        return self.paths
    
# Time Complexeity: O(N)
# Space Complexeity: O(N)

'''
Method: 
recursive dfs with backtracking - alternative use list copies
 1. check if root and initialize the self.path variable
 2. create helper dfs function
 3. add to current sum and path 
 4. if not left and not right, if cur sum == tatget the append a copy and remove from list and current sum
5. run the dfs where appropriate
6. remove and pop from sum and list
7. run dfs and return the final list


'''

# same complexeity more elegant as it uses list copying by declaring a new variable. 
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> list[list[int]]:
        self.paths = []

        if not root: 
            return self.paths

        
        def dfs(node, orders,cur_sum): 

            cur_sum += node.val
            order = orders + [node.val]

            
            if node.left: 
                dfs(node.left, order, cur_sum)
            if node.right: 
                dfs(node.right, order, cur_sum)
            if not node.left and not node.right: 
                if cur_sum == targetSum: 
                    self.paths.append(order)
        
        dfs(root, [], 0)
        return self.paths
    
# iterative stack approach


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> list[list[int]]:
        paths = []
        stack = [] 
        if root: 
            stack.append((root,False, root.val, [root.val])) # node, visited, cur_sum, path
        else: 
            return paths
            
        while len(stack) != 0: 
            node, visited, cur_sum, path = stack.pop()

            if node: 
                if visited == True: 
                    if not node.right and not node.left: 
                        if cur_sum == targetSum: 
                            paths.append(path)
                else: 
                    stack.append((node, True, cur_sum, path))

                    if node.right: 
                        stack.append((node.right, False, cur_sum+node.right.val, path+[node.right.val]))
                             
                    if node.left: 
                        stack.append((node.left, False, cur_sum+node.left.val, path+[node.left.val]))
        
        return paths
        

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> list[list[int]]:
        paths = []
        stack = [] 
        visited = set()
        if root: 
            stack.append((root, root.val, [root.val])) # node, visited, cur_sum, path
        else: 
            return paths
            
        while len(stack) != 0: 
            node, visited, cur_sum, path = stack.pop()

            if node: 
                if node in visited: 
                    if not node.right and not node.left: 
                        if cur_sum == targetSum: 
                            paths.append(path)
                else: 
                    visited.add(node)
                    stack.append((node,cur_sum,path))

                    if node.right: 
                        stack.append((node.right, False, cur_sum+node.right.val, path+[node.right.val]))
                             
                    if node.left: 
                        stack.append((node.left, False, cur_sum+node.left.val, path+[node.left.val]))
        
        return paths
        

# using a visited set instead
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> list[list[int]]:
        paths = []
        stack = [] 
        visited = set()
        if root: 
            stack.append((root, root.val, [root.val])) # node, visited, cur_sum, path
        else: 
            return paths
            
        while len(stack) != 0: 
            node, cur_sum, path = stack.pop()

            if node: 
                if node in visited: 
                    if not node.right and not node.left: 
                        if cur_sum == targetSum: 
                            paths.append(path)
                else: 
                    visited.add(node)
                    stack.append((node,cur_sum,path))

                    if node.right: 
                        stack.append((node.right, cur_sum+node.right.val, path+[node.right.val]))
                             
                    if node.left: 
                        stack.append((node.left, cur_sum+node.left.val, path+[node.left.val]))
        
        return paths
        