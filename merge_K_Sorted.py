# Leetcode 23. Merge k Sorted Lists

# Time Complexity :  O(nk.log k) where n is the average size of the input lists, where k is the size of the heap

# Space Complexity : O(k) where k is the size of the heap

# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Approach: Using a custom comparator for ListNodes, add all the nodes into the min heap, pop the 
# smallest one and add the next element into the heap. Add the popped node to the result list. 
# Repeat until the heap is empty

# Your code here along with comments explaining your approach

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from heapq import heappush as push
from heapq import heappop as pop

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        # custom less than comparator using lambda function taking ListNode objects x & y as params
        ListNode.__lt__ = lambda x, y: x.val < y.val
        # Min heap
        hq = []
        dummy = ListNode(-1)
        result = dummy
        # Adding elements to min heap with custom comparator for list nodes
        for node in lists:
            if node:
                push(hq,node)
        
        # Removing the smallest element from the min heap and adding to the result list
        # Adding the next element of min into the heap for next round of comparisions
        while len(hq) > 0:
            minn = pop(hq)
            dummy.next = minn
            dummy = dummy.next
            if minn.next:
                push(hq,minn.next)
                
        return result.next