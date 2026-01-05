import math

class Solution:
    def maxMatrixSum(self, matrix: list[list[int]]) -> int:
        min_abs = math.inf
        abs_sum = 0
        neg_count = 0
        
        for row in matrix:
            for num in row:
                if num < 0:
                    neg_count += 1
                abs_val = abs(num)
                abs_sum += abs_val
                if abs_val < min_abs:
                    min_abs = abs_val
        
        if neg_count % 2 == 0:
            return abs_sum
        else:
            return abs_sum - 2 * min_abs

