# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        head = root
        maxVal = max(p.val, q.val)
        minVal = min(p.val, q.val)
        
        while head:
            if head.val < minVal:
                head = head.right
            elif head.val > maxVal:
                head = head.left
            else:
                return head
        
        return None