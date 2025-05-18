# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        temp= ListNode(0)
        temp.next = head
        first = temp
        second = temp

        for _ in range(n + 1):
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next
        return temp.next