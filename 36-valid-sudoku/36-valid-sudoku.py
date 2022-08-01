import numpy as np


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check vertically and horizontally using transpose function
        # check within a box using voxel gather
        
        box=[]
        l=len(board)
        bl=len(board)//3
        
        for r in range(0,l,3):
            for c in range(0,l,3):
                for i in range(r,r+bl,1):
                    for j in range(c,c+bl,1):
                        if board[i][j]!=".":
                            box.append(board[i][j])
                if len(set(box))!=len(box):
                    return False
                box=[]
              
        #vertical transpose
        vertical=np.transpose(board)
        
        row=[]
        col=[]
        
        for r in range(0,l):
            for c in range(0,l):
                if board[r][c]!=".":
                    row.append(board[r][c])
                    print(row)
                    if len(set(row))!=len(row):
                        return False
                if vertical[r][c]!=".":
                    col.append(vertical[r][c])
                    print(col)
                    if len(set(col))!=len(col):
                        return False
            row=[]
            col=[]
                
        return True    
        