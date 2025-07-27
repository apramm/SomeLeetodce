# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # INTUITION
        #true? if there is subtree of root with same structure and node val of subRoot
        #subtree? tree consisting of a node in tree and all of node's desc

        #so basically two trees s and t are identical
        # if their root val same and left/right subtrees are identical
        
        # recursively check if isIdentical trees?
        

        # IF THE TREE HAS BEEN ITERATED  => TRUE
        # IF TREES EXISTS AND THIER VALUE EQUAL KEEP CHECKING UNTIL WE END OR THEY DON'T EQUAL OR ONE OF THEM ENDS
        def isIdentical(tree1, tree2):
            if not tree1 and not tree2:
                return True
            if tree1 and tree2 and tree1.val == tree2.val:
                return (isIdentical(tree1.left, tree2.left) and isIdentical(tree1.right, tree2.right))
            

            return False

        # KEEP CHECKING RECURSIVELY IF THE TREE IS IDENTICAL AT ANY NODE IN TREE?
        
        if not root:
            return False
        if isIdentical(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)





        #STRING SERIALIZATION?
        # provides way to check if their pattern identical and same node values exist for that!
        # O(n) time and O(n) space to store serialized strings
        # def ser(n):
        #     if not n:
        #         return ',#'
        #     return ','+str(n.val)+ser(n.left)+ser(n.right)

        # return ser(subRoot) in ser(root)


        # return False


        