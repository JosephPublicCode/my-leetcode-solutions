# leetcode 450 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution: 
    def deleteNode(self, root: TreeNode, key:int) -> TreeNode:
        if not root: 
            return root
        
        if key > root.val: 
            root.right = self.deleteNode(root.right,key)
        elif key < root.val: 
            root.left = self.deleteNode(root.left, key)
        else: 

            if not root.right: 
                return root.left
            elif not root.left: 
                return root.right
            
            else: 
                cur = root.right

                while cur.left: 
                    cur = cur.left 
                root.val = cur.val
                root.right = self.deleteNode(root.right, root.val)

        return root

# Time Complexeity: O(h)
# Space Complexeity: O(N)


'''
Method: 

See algorithm on finding a node - leetcode 700

recursive dfs

1. search for the node using leetcode 700 
2. if found
3. if no left node then return the right node
4. if no right node then return the left
5. else find the leftmost node on the right side.
6. assign the root to this value then recursively delete the copy of the new assignment
7. step 6 involves reassigning the target to root.val 


'''