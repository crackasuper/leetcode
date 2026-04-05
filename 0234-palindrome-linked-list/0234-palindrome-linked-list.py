# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev,current = None, slow.next

        while current:
            temp_val = current.next
            current.next = prev
            prev, current = current, temp_val

        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next

        return True


        