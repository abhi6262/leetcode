from heapq import heappush, heappop
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        heap = []
        for i in range(k):
            if lists[i]:
                heappush(heap, (lists[i].val, i))
        head, curr = None, None
        while heap:
            v, i = heappop(heap)
            if not head:
                head = lists[i]
                curr = head
            else:
                curr.next = lists[i]
                curr = curr.next
            lists[i] = lists[i].next
            if lists[i]:
                heappush(heap, (lists[i].val, i))
        return head
