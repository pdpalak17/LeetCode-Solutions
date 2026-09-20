import heapq

class Solution:
    def findKthLargest(self, nums, k):
        heap = []

        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            elif num > heap[0]:
                heapq.heapreplace(heap, num)  # pop min, push num in one step

        return heap[0]  # root = kth largest