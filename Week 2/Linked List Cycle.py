# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        header = head
        runner = head
        
        while runner != None and runner.next != None:
            header = header.next
            runner = runner.next.next
            
            if header == runner:
                return True
            
        return False