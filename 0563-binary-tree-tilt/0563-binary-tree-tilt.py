# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTilt(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.total_tilt = 0  

        def dfs(node):
            if not node:
                return 0 

            left_sum = dfs(node.left)     
            right_sum = dfs(node.right)   

            
            node_tilt = abs(left_sum - right_sum)
            self.total_tilt += node_tilt  

            return node.val + left_sum + right_sum  

        dfs(root)
        return self.total_tilt