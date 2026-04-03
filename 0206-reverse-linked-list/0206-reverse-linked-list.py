# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        previous, current = None, head

        while current:
            temp_node = current.next
            current.next = previous

            current, previous = temp_node, current

        return previous


        