class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        def search(arr):
            low = 0
            high = len(arr)-1
            while low<=high:
                mid = (low+high)//2
                if arr[mid]==target:
                    return True
                if arr[mid]>target:
                    high = mid-1
                else:
                    low = mid+1
            return False
        
        for i in range(len(matrix)):
            if matrix[i][0]<=target:
                if search(matrix[i]):
                    return True
        return False