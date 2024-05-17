# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        slow = fast = dummy

        for _ in range(k):
            fast = fast.next

        first = fast
        second = dummy

        while fast:
            fast = fast.next
            second = second.next

        first.val, second.val = second.val, first.val

        return dummy.next
        