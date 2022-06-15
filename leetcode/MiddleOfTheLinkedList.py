# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:


def middleNode(head, n):
  tmp = head
  while tmp and tmp.next:
    head = head.next
    tmp =tmp.next.next
  return head

