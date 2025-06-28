# Time complexity: O(n log k)
# Space complexity: O(k)
import heapq
def findKthLargest(nums, k):
    return heapq.nlargest(k, nums)[-1]


# Time complexity: O(n) on average, O(n^2) in the worst case
# Space complexity: O(1)

import random

def findKthLargest(nums, k):
    k = len(nums) - k  # Convert to 0-based indexing from the start
    def quickselect(l, r):
        if l == r:
            return nums[l]
        pivot_index = random.randint(l, r)
        nums[pivot_index], nums[r] = nums[r], nums[pivot_index]
        pivot = nums[r]
        i = l
        for j in range(l, r):
            if nums[j] <= pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[r] = nums[r], nums[i]
        if i == k:
            return nums[i]
        elif i < k:
            return quickselect(i + 1, r)
        else:
            return quickselect(l, i - 1)
    return quickselect(0, len(nums) - 1)
