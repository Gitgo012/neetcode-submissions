import numpy as np
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr=np.array(matrix)
        rows,cols=np.shape(arr)
        left=0
        right=(rows*cols)-1
        while left<=right:
            mid=left+(right-left)//2
            mid_row=mid//cols
            mid_col=mid%cols
            if matrix[mid_row][mid_col]==target:
                return True
            elif matrix[mid_row][mid_col]<target:
                left=mid+1
            elif matrix[mid_row][mid_col]>target:
                right=mid-1
        return False
