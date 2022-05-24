# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        head = root
        
        while head:
            if -2 < Solution().heightOfNode(head.left) - Solution().heightOfNode(head.right) < 2 and Solution().isBalanced(head.left) and Solution().isBalanced(head.right):
                return True
            else: return False
                
        return True
        
    def heightOfNode(self, node):
        if node: 
            return max(Solution().heightOfNode(node.left), Solution().heightOfNode(node.right)) + 1
        else: return 0