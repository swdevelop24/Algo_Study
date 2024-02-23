"""
Time complexity: O(1)
Space complexity: O(1)

"""


class Solution:

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        square = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                cur = board[i][j]
                if cur == ".":
                    continue
                if (
                    (cur in rows[i])
                    or (cur in cols[j])
                    or (cur in square[i // 3][j // 3])
                ):
                    return False
                rows[i].add(cur)
                cols[j].add(cur)
                square[i // 3][j // 3].add(cur)

        return True


print(
    Solution.isValidSudoku(
        Solution,
        [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ],
    )
)
