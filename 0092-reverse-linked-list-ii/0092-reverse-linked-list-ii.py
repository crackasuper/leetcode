# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """

        if not head or not head.next:
            return head

        if left == right:
            return head

        dummy = ListNode(0, head)

        before_reverse = dummy
        for _ in range(left - 1):

            before_reverse = before_reverse.next
        first_reversed = before_reverse.next

        prev = before_reverse
        current = first_reversed

        for _ in range(right - left + 1):
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp

        before_reverse.next = prev
        first_reversed.next = current
        
        return dummy.next
        
        