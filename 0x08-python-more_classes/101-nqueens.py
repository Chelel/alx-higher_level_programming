import sys


def solve_n_queens(N):
    """solves the N queens problem."""
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)
    elif N < 4:
        print("N must be at least 4")
        sys.exit(1)

    def is_valid(queens, new_queen):
        row, col = new_queen
        for r, c in queens:
            if col == c or row + col == r + c or row - col == r - c:
                return False
            return True

    def backtrack(queens, row):
        if row == N:
            solutions.append(queens[:])
            return
        for col in range(N):
            new_queen = (row, col)
            if is_valid(queens, new_queen):
                queens.append(new_queen)
                backtrack(queens, row + 1)
                queens.pop()

    solutions = []
    queens = []
    backtrack(queens, 0)
    return solutions
