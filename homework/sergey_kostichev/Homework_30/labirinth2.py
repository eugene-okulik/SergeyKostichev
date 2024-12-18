import csv
import sys

DIRECTIONS = [(-1, 0, '^'), (0, 1, '>'), (1, 0, 'v'), (0, -1, '<')]  # up, right, down, left
MY_PATH = '.'
START_POINT = 'o'
EXIT_POINT = 'X'


def walk(row: int, col: int) -> bool:  
    f"""
    Эта функция начинает выполнение с указанных параметров row и col и 
    продолжает выполнение до тех пор, пока не найдет последний элемент, обозначенный символом {EXIT_POINT}. 
    Вокруг текущего элемента матрицы проверяются ячейки, чтобы определить, свободна ли ячейка сверху, справа, 
    снизу или слева. Эти возможные пути добавляются в список paths, и следующая ячейка(ячейки) проверяются рекурсивно. 
    Если существует несколько направлений, то все возможные варианты также добавляются в этот список.
    Если на каком-то вызове функции список paths оказывается пустым, значит, на этом направлении тупик. Тогда
    функция начинает возвращаться к предыдущим элементам списка paths, откуда были другие возможные пути (перекрестки).
    Функция помечает каждую новую ячейку при вызове функции символом {START_POINT}, чтобы отслеживать выбранный путь
    и избежать петляния по уже пройденным элементам матрицы. 
    Когда найдена конечная точка, рекурсивная функция завершается и каждая ячейка вдоль правильного пути 
    заменяет временный символ {START_POINT} символом {MY_PATH}.

    Параметры:
        row (int): Начальный индекс строки.
        col (int): Начальный индекс столбца.
    
    Возвращает:
        bool: True, если достигнута конечная точка {EXIT_POINT}, в противном случае - False.
    """
    paths = []
    # если мы достигли выхода, или в проходе уже есть наши следы, значит, мы возвращаемся из функции.
    # иначе оставляем след, на текущем элементе матрицы.
    for dir in DIRECTIONS:
        if matrix[row + dir[0]][col + dir[1]] == EXIT_POINT or matrix[row + dir[0]][col + dir[1]] == MY_PATH:
            return True
        else:
            matrix[row][col] = START_POINT
        # Проверяем, какой путь сейчас свободен. Каждый свободный проход из текущего элемента будет в добавлен в список.
        if matrix[row + dir[0]][col + dir[1]] == ' ':
            # dir[2] - это просто <<красивость>> в виде символа текущего направления наверх ^, вниз v, вправо >, влево <
            # при проходе по лабиринту.
            # Можно заменить dir[2] на MY_PATH, чтобы оставить лишь дефолтные точки.
            # direction = MY_PATH
            direction = dir[2]
            paths.append((row + dir[0], col + dir[1], direction))
    # Если в списке есть проходы, то для каждого запускается рекурсивная функция с координатами этого прохода.
    if len(paths) > 0:
        for i in range(len(paths)):
            if walk(paths[i][0], paths[i][1]):
                matrix[paths[i][0]][paths[i][1]] = paths[i][2]
                return True
            else:
                # Убери эту строку, если нужно увидеть,
                # какие тупики попали в обход лабиринта.
                matrix[paths[i][0]][paths[i][1]] = ' '


if __name__ == '__main__':
    # Есть два сгенерированных лабиринта.
    maze = input("Enter 1 for a small labyrinth or 2 for a big one\n")
    if maze == '1':
        maze = 'maze-1.csv'
    elif maze == '2':
        maze = 'maze.csv'
    else:
        print("There is no such labyrinth, and we will select a small one for you")
    # Перевод csv файла в матрицу.
    try:
        with open(maze, 'r') as file:
            reader = csv.reader(file, delimiter=';')
            matrix = []
            for row in reader:
                matrix.append(row)
    except Exception:
        print('csv.file was not read')
    else:
        # Очистка лабиринта от нулей, чтобы лучше отображались проходы.
        matrix = [[' ' if element == '0' else element for element in row] for row in matrix]
        # По условию, искомая цель всегда находится в предпоследнем ряду в предпоследнем столбце матрицы.
        end = (len(matrix) - 2, len(matrix) - 2)
        matrix[end[0]][end[1]] = EXIT_POINT
        # Запуск рекурсивной функции, по условию начало всегда в ячейке матрицы (1, 1).
        walk(1, 1)
        # Вывод найденного пути.
        for row in matrix:
            print(' '.join(row))
