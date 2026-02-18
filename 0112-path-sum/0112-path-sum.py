# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # recursive approach

        # if not root: # edge case: empty tree
        #     return False
        
        # targetSum -= root.val # subtract current node's value from targetSum

        # if not root.left and not root.right: # check if it's a leaf node
        #     return targetSum == 0 # if targetSum is 0, we found a valid path
        
        # # recursively check left and right subtrees
        # if self.hasPathSum(root.left, targetSum):
        #     return True
        # if self.hasPathSum(root.right, targetSum):
        #     return True
        
        # return False # if neither subtree has a valid path, return False
    
        #iterative approach

        if not root:  
            return False
        stack = [(root, targetSum - root.val)] # stack to hold nodes and remaining sum
        while stack:
            node, current_sum = stack.pop()
            if not node.left and not node.right and current_sum == 0: #check if it's a leaf node and current_sum is 0
                return True
            if node.right:
                stack.append((node.right, current_sum - node.right.val))
            if node.left:
                stack.append((node.left, current_sum - node.left.val))
        return False
    