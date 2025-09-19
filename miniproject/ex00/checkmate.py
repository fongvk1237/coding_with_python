def find_king(board):
    king = None
    count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "K":
                king = (i, j)
                count += 1
    if count == 1:
        return king
    else:
        return None


def pawn_check(board, kx, ky):
    n = len(board)
    directions = [(1, -1), (1, 1)]
    for dx, dy in directions:
        x = kx + dx
        y = ky + dy
        if x >= 0 and y >= 0 and x < n and y < n:
            if board[x][y] == "P":
                return True
    return False


def rook_check(board, kx, ky):
    n = len(board)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        x = kx
        y = ky
        while True:
            x += dx
            y += dy
            if x < 0 or y < 0 or x >= n or y >= n:
                break
            if board[x][y] != ".":
                if board[x][y] == "R":
                    return True
                break
    return False


def bishop_check(board, kx, ky):
    n = len(board)
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dx, dy in directions:
        x = kx
        y = ky
        while True:
            x += dx
            y += dy
            if x < 0 or y < 0 or x >= n or y >= n:
                break
            if board[x][y] != ".":
                if board[x][y] == "B":
                    return True
                break
    return False


def queen_check(board, kx, ky):
    n = len(board)
    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1),
        (-1, -1), (-1, 1), (1, -1), (1, 1)
    ]
    for dx, dy in directions:
        x = kx
        y = ky
        while True:
            x += dx
            y += dy
            if x < 0 or y < 0 or x >= n or y >= n:
                break
            if board[x][y] != ".":
                if board[x][y] == "Q":
                    return True
                break
    return False


def checkmate(board_str):

    raw_rows = board_str.strip().split("\n")

    board = [list(r) for r in raw_rows]

    n = len(board)

    if n == 0:
        print("Error")
        return
    for r in board:
        if len(r) != n:
            print("Error")
            return

    allowed = [".", "K", "Q", "R", "B", "P"]
    for r in board:
        for c in r:
            if c not in allowed:
                print("Error")
                return

    king = find_king(board)
    if king is None:
        print("Error")
        return
    
    kx, ky = king
    if pawn_check(board, kx, ky):
        print("Success")
    elif rook_check(board, kx, ky):
        print("Success")
    elif bishop_check(board, kx, ky):
        print("Success")
    elif queen_check(board, kx, ky):
        print("Success")
    else:
        print("Fail")