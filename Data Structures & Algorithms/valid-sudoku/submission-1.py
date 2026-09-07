class Solution:

    def gather_squares(self, board: List[List[str]]):
        sqrs = defaultdict(list)
        
        # get 3x3 square numbers
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                idx = (i // 3) * 3 + (j // 3)
                sqrs[idx].append(cell)
            
        return sqrs


    def has_duplicates(self, row: List[str]) -> bool:
        seen = set()
        
        # looks for already seen elements (excluding .)
        for elem in row:
            if elem == ".":
                continue
        
            if elem in seen:
                return True
        
            seen.add(elem)
        
        return False
        
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # 3x3 check        
        sqrs = self.gather_squares(board)
        if any(self.has_duplicates(row) for row in sqrs.values()):
            return False
    
        # row check
        if any(self.has_duplicates(row) for row in board):
            return False
        
        # cols
        cols = list(zip(*board))
        if any(self.has_duplicates(col) for col in cols):
            return False
        
        return True