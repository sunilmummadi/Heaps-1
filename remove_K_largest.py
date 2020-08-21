# Leetcode 215. Kth Largest Element in an Array

# Time Complexity :  O(n log k) where n is the size of the array

# Space Complexity : O(k) where k is the size of the heap

# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Approach: Add elements in the list to the min heap untill size matches k, remove the top if min heap
# size exceeds k. Return the peek of the heap when the entire array is traversed. Since its a min heap 
# of size k, the peek element is the k th largest in the heap

# Your code here along with comments explaining your approach

from heapq import heappush as push
from heapq import heappop as pop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # list to act as min heap
        hq = []
        # adding k elements to the heap
        for i in range(len(nums)):
            push(hq,nums[i])
            # if elements in heap exceed k remove the smallest
            if len(hq) > k:
                pop(hq)
        # returning the smallest element        
        return hq[0]