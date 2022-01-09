class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        for i in range(n):
            for j in range(i+1,n): #transpose opertion
                matrix[i][j],matrix[j][i]= matrix[j][i],matrix[i][j]
        
        for i in range(n): #reverse each row 
            matrix[i]=matrix[i][::-1]
            
        