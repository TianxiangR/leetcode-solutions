#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#
from typing import *
# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows: list[set[int]] = [set() for _ in range(9)]
        cols: list[set[int]] = [set() for _ in range(9)]
        boxes: list[list[set[int]]] = [set() for _ in range(9)]
        
        get_box_index: Callable[[int, int], int] = lambda i, j: (i // 3) * 3 + (j // 3)
        
        # init records
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val != ".":
                    rows[i].add(int(val))
                    cols[j].add(int(val))
                    boxes[get_box_index(i, j)].add(int(val))
        
        def can_place(num: int, i: int, j: int) -> bool:
            return num not in rows[i] \
                and num not in cols[j] \
                    and num not in boxes[get_box_index(i, j)]
        
        def place_num(num: int, i: int, j: int):
            rows[i].add(num)
            cols[j].add(num)
            boxes[get_box_index(i, j)].add(num)
            board[i][j] = str(num)
        
        def remove_num(i: int, j: int):
            num = int(board[i][j])
            board[i][j] = "."
            rows[i].remove(num)
            cols[j].remove(num)
            boxes[get_box_index(i, j)].remove(num)
        
        def next_step(i: int, j: int) -> tuple[int, int]:
            if j == 8:
                return (i + 1, 0)
            return (i, j + 1)
        
        def fill(i: int = 0, j: int = 0) -> bool:
            val = board[i][j]
            if val == ".":
                for num in range(1, 10):
                    if can_place(num, i, j):
                        place_num(num, i, j)
                        if i == 8 and j == 8:
                            # board filled
                            return True
                        next_i, next_j = next_step(i, j)
                        is_finished = fill(next_i, next_j)
                        if is_finished:
                            return True
                        remove_num(i, j)
            elif i == 8 and j == 8:
                # board already filled
                return True
            else:
                next_i, next_j = next_step(i, j)
                is_finished = fill(next_i, next_j)
                if is_finished:
                    return True

            # board cannot be filled
            return False
        
        fill()

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    solution.solveSudoku(board)
    print(board)
    