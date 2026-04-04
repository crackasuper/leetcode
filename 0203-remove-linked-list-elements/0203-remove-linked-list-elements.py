# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]

        """
        dummy = ListNode(-1, head)

        prev = dummy
        while prev.next:
            
            if prev.next.val != val:
                prev = prev.next

            else:
                prev.next = prev.next.next
          
        return dummy.next



        




        