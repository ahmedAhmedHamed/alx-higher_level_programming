#!/usr/bin/python3
""" this is my solution to the n_queens problem"""
import sys


def n_queens(row, valid, board, n):
    if row == n:
        fill_valid(board, valid, n)
        return

    for col in range(n):

        if placeable(row, col, board, n):
            board[row][col] = "X"
            n_queens(row + 1, valid, board, n)
            board[row][col] = "#"


def fill_valid(board, valid, n):
    temp = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == "X":
                temp.append([i, j])
    valid.append(temp)


def placeable(row, col, board, n):
    x = row
    y = col
    while x >= 0:
        if board[x][y] == "X":
            return False
        else:
            x -= 1
    x = row
    y = col
    while y < n and x >= 0:
        if board[x][y] == "X":
            return False
        else:
            y += 1
            x -= 1
    x = row
    y = col
    while y >= 0 and x >= 0:
        if board[x][y] == "X":
            return False
        else:
            x -= 1
            y -= 1
    return True


if __name__ == "__main__":

    if len(sys.argv) != 1:
        print("Usage: nqueens N")
        exit(1)
    n = sys.argv[0]

    if not isinstance(n, int):
        print("N must be a number")
        exit(1)

    if n < 4:
        print("N must be at least 4")
        exit(1)

    board = [["#" for i in range(n)] for j in range(n)]

    valid = []
    n_queens(0, valid, board, n)

    for i in range(len(valid)):
        print(valid[i])
