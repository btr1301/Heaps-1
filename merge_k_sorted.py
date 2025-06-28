# Time complexity: O(N log k)
# Space complexity: O(k)

import heapq

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        min_heap = []
        for node in lists:
            if node:
                heapq.heappush(min_heap, (node.val, id(node), node))
        
        dummy_node = ListNode(0)
        current_node = dummy_node
        
        while min_heap:
            val, _, node = heapq.heappop(min_heap)
            current_node.next = node
            current_node = current_node.next
            if node.next:
                heapq.heappush(min_heap, (node.next.val, id(node.next), node.next))
        
        return dummy_node.next
