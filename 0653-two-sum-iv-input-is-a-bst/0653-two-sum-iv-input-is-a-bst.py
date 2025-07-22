# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """
        def inorder(node, vals):
            if not node:
                return
            inorder(node.left, vals)
            vals.append(node.val)
            inorder(node.right, vals)
        
        vals = []
        inorder(root, vals)
        
        i, j = 0, len(vals) - 1
        while i < j:
            s = vals[i] + vals[j]
            if s == k:
                return True
            elif s < k:
                i += 1
            else:
                j -= 1
        return False