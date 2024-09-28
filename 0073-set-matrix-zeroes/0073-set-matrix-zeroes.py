class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        flagr, flagc = 0, 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    if i==0 or j==0:
                        if i==0:
                            flagr=1
                        if j==0:
                            flagc=1
                    else:
                        matrix[i][0]=0
                        matrix[0][j]=0
        for i in range(len(matrix)):
            if i!=0 and matrix[i][0]==0:
                for j in range(len(matrix[0])-1):
                    matrix[i][j+1]=0
        for j in range(len(matrix[0])):
            if j!=0 and matrix[0][j]==0:
                for i in range(len(matrix)-1):
                    matrix[i+1][j]=0
        if flagr==1:
            for j in range(len(matrix[0])):
                matrix[0][j]=0
        if flagc==1:
            for i in range(len(matrix)):
                matrix[i][0]=0