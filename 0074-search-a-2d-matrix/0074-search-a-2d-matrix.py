class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left=0
        low=0
        high=len(matrix)-1
        right=len(matrix[0])-1
        # if len(matrix)==1 and len(matrix[0])==1 and matrix[0][0]==target:
        #     return True
        while low<=high:
            midr=(low +high)//2
            if matrix[midr][right]==target:
                return True
            elif matrix[midr][right]>target:
                if matrix[midr][left]==target:
                    return True
                elif matrix[midr][left]<target:
                    while left<=right:
                        midc=(left+right)//2
                        if matrix[midr][midc]==target:
                            return True
                        elif matrix[midr][midc]>target:
                            right=midc-1
                        else:
                            left=midc+1
                else:
                    high=midr-1

            # elif matrix[midr][right]<target:
            else:
                low=midr+1
        
        return False