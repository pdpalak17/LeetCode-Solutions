class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        max_area = 0

        for row in matrix:
            # Update histogram heights
            for j in range(cols):
                if row[j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0

            # Find largest rectangle in histogram
            stack = []

            for j in range(cols + 1):
                curr_height = heights[j] if j < cols else 0

                while stack and heights[stack[-1]] > curr_height:
                    h = heights[stack.pop()]

                    width = j if not stack else j - stack[-1] - 1

                    max_area = max(max_area, h * width)

                stack.append(j)

        return max_area