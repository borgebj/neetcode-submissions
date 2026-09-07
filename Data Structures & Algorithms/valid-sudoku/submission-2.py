from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for row in range(9):
            for col in range(9):
                cell = board[row][col]

                # ignore empty spots
                if cell == ".":
                    continue

                # get square index
                square = (row // 3) * 3 + (col // 3)

                # check for duplicates
                if cell in rows[row] or cell in cols[col] or cell in squares[square]:
                    return False

                # add to seen
                rows[row].add(cell)
                cols[col].add(cell)
                squares[square].add(cell)

        return True