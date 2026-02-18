# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: # edge case: empty tree
            return False
        
        targetSum -= root.val # subtract current node's value from targetSum

        if not root.left and not root.right: # check if it's a leaf node
            return targetSum == 0 # if targetSum is 0, we found a valid path
        
        # recursively check left and right subtrees
        if self.hasPathSum(root.left, targetSum):
            return True
        if self.hasPathSum(root.right, targetSum):
            return True
        
        return False # if neither subtree has a valid path, return False