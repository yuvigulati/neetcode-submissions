class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]  # 9 boxes total

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue  # skip empty cells

                # Compute box index (0–8)
                box_index = (r // 3) * 3 + (c // 3)

                # Check duplicates
                if (val in rows[r]) or (val in cols[c]) or (val in boxes[box_index]):
                    return False

                # Record the value in the sets
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_index].add(val)

        return True
