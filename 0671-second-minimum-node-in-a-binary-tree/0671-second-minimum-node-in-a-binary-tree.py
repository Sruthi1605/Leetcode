# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        min_val = root.val
        self.second_min = float('inf')

        def dfs(node):
            if not node:
                return
            if min_val < node.val < self.second_min:
                self.second_min = node.val
            elif node.val == min_val:
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return self.second_min if self.second_min < float('inf') else -1