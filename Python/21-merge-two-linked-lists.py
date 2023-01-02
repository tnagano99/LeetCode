# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curnode = merged = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                curnode.next = list1
                list1, curnode = list1.next, list1
            else:
                curnode.next = list2
                list2, curnode = list2.next, list2
        
        if list1 or list2:
            curnode.next = list1 if list1 else list2
        
        return merged.next
                

        
        return merged