class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        SIZE = 9
        visited = set()

        for row in range(SIZE):
            for col in range(SIZE):
                n = board[row][col]
                if n != '.':
                    r = f'r{row}{n}'
                    c = f'c{col}{n}'
                    b = f'b{(row // 3) * 3 + (col // 3)}{n}'

                    if r in visited or c in visited or b in visited:
                        return False
                    visited.add(r)
                    visited.add(c)
                    visited.add(b)
        return True
