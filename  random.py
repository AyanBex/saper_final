import random

# Функция для создания игрового поля
def create_board(rows, cols, mines):
    board = [[' ' for _ in range(cols)] for _ in range(rows)]

    for _ in range(mines):
        while True:
            row = random.randint(0, rows - 1)
            col = random.randint(0, cols - 1)
            if board[row][col] != 'X':
                board[row][col] = 'X'
                break

    for row in range(rows):
        for col in range(cols):
            if board[row][col] != 'X':
                count = 0
                for r in range(max(0, row - 1), min(rows, row + 2)):
                    for c in range(max(0, col - 1), min(cols, col + 2)):
                        if board[r][c] == 'X':
                            count += 1
                if count > 0:
                    board[row][col] = str(count)

    return board

# Функция для вывода игрового поля на экран
def print_board(board, revealed):
    rows = len(board)
    cols = len(board[0])

    print('    ', end='')
    for col in range(cols):
        print(col, end=' ')
    print()

    print('   ', end='')
    print('- ' * cols)

    for row in range(rows):
        print(row, '|', end=' ')
        for col in range(cols):
            if revealed[row][col]:
                print(board[row][col], end=' ')
            else:
                print('_', end=' ')
        print()

    print()

# Функция для открытия клетки и расширения пустых клеток
def open_cell(board, revealed, row, col):
    rows = len(board)
    cols = len(board[0])

    if row < 0 or row >= rows or col < 0 or col >= cols:
        return

    if revealed[row][col]:
        return

    revealed[row][col] = True

    if board[row][col] == 'X':
        return

    if board[row][col] != ' ':
        return

    for r in range(max(0, row - 1), min(rows, row + 2)):
        for c in range(max(0, col - 1), min(cols, col + 2)):
            open_cell(board, revealed, r, c)

# Функция для игры
def play_game(rows, cols, mines):
    board = create_board(rows, cols, mines)
    revealed = [[False for _ in range(cols)] for _ in range(rows)]
    game_over = False

    while not game_over:
        print_board(board, revealed)

        row = int(input("Введите номер строки: "))
        col = int(input("Введите номер столбца: "))

        if not revealed[row][col]:
            if board[row][col] == 'X':
                print('Вы проиграли!')
                game_over = True
            else:
                open_cell(board, revealed, row, col)
                if all(all(revealed_row) for revealed_row in revealed):
                    print('Вы выиграли!')
                    game_over = True
        else:
            print('Клетка уже открыта. Выберите другую клетку.')

    print_board(board, revealed)

# Запуск игры
print('Игра Сапер')

difficulty = int(input("Выберите уровень сложности (1 - Легкий, 2 - Средний, 3 - Тяжелый): "))
if difficulty == 1:
    rows = 5
    cols = 5
    mines = 5
elif difficulty == 2:
    rows = 8
    cols = 8
    mines = 10
else:
    rows = 10
    cols = 10
    mines = 15

play_game(rows, cols, mines)
