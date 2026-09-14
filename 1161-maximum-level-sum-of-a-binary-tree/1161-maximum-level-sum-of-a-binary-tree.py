# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def maxLevelSum(self, root: 'TreeNode') -> int:
        q = deque([root])
        level = 1
        ans = 1
        best = float('-inf')

        while q:
            total = 0

            for _ in range(len(q)):
                node = q.popleft()
                total += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if total > best:
                best = total
                ans = level

            level += 1

        return ans