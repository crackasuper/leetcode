# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None or list2 is None:
            return list1 or list2

        #comparing two values of lists to sort

        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)

            return list1

        else:
            list2.next = self.mergeTwoLists(list1, list2.next)

            return list2
        