
# class MyLinkedList:

#     def __init__(self):
      
#         self.next = None
        

#     def get(self, index: int) -> int:
#         current  = self.head
#         count = 0
#         while current:
#             if count == index:
#                 return current.val
#             current = current.next
#             count += 1
#         return -1
        

#     def addAtHead(self, val: int) -> None:
#         new_node = Node(val)
#         if not self.head:
#             self.head = new_node
#         else:
#             current = self.head
#             while current:
#                 current = current.next
#             current.next = new_node
            
#     def addAtTail(self, val: int) -> None:
#         new_node = Node(val)
#         if self.head is Nonde:
#             self.head = new_node
#         else:
#             temp = self.head
#             while temp.next is not None:
#                 temp = temp.next
#             temp.next = new_node
        

#     def addAtIndex(self, index: int, val: int) -> None:
#         new_node = Node(val)
#         if index == 0:
#             new_node.next = self.head
#             self.head = new_node
#         else:
#             temp = self.head
#             for _ in range(index -1):
#                 if temp is None:
#                     raise IndexError("index out of range")
#                 temp = temp.next
#             new_node.next = temp.next
#             temp.next = new_node
        

#     def deleteAtIndex(self, index: int) -> None:
#         if index < 0:
#             return
#         if index == 0:
#             self.head = self.head.next
#             return
#         current = self.head
#         prev = None
#         count = 0
#         while current and count != index:
#             prev = current
#             current = current.next
#             count += 1
#         if current is None:
#             return 
#         prev.next = current.next
        
        


# # Your MyLinkedList object will be instantiated and called as such:
# # obj = MyLinkedList()
# # param_1 = obj.get(index)
# # obj.addAtHead(val)
# # obj.addAtTail(val)
# # obj.addAtIndex(index,val)
# # obj.deleteAtIndex(index)

class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None


class MyLinkedList:
  def __init__(self):
    self.length = 0
    self.dummy = ListNode(0)

  def get(self, index: int) -> int:
    if index < 0 or index >= self.length:
      return -1
    curr = self.dummy.next
    for _ in range(index):
      curr = curr.next
    return curr.val

  def addAtHead(self, val: int) -> None:
    curr = self.dummy.next
    self.dummy.next = ListNode(val)
    self.dummy.next.next = curr
    self.length += 1

  def addAtTail(self, val: int) -> None:
    curr = self.dummy
    while curr.next:
      curr = curr.next
    curr.next = ListNode(val)
    self.length += 1

  def addAtIndex(self, index: int, val: int) -> None:
    if index > self.length:
      return
    curr = self.dummy
    for _ in range(index):
      curr = curr.next
    temp = curr.next
    curr.next = ListNode(val)
    curr.next.next = temp
    self.length += 1

  def deleteAtIndex(self, index: int) -> None:
    if index < 0 or index >= self.length:
      return
    curr = self.dummy
    for _ in range(index):
      curr = curr.next
    temp = curr.next
    curr.next = temp.next
    self.length -= 1