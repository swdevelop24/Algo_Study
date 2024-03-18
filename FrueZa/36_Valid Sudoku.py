class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows, cols, boxes = [set() for _ in range(9)], [set() for _ in range(9)], [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue

                val = board[r][c]
                box_index = (r // 3) * 3 + c // 3

                if val in rows[r] or val in cols[c] or val in boxes[box_index]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                boxes[box_index].add(val)

        return True
