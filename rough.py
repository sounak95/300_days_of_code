def is_safe(srcx, srcy, newx, newy, maze, row, col, visited):
    # Possibilities:
    # -> path closed
    # -> out of bound
    # -> check if pos is already visited
    if (0 <= newx < row) and (0 <= newy < col) and maze[newx][newy] == 1 and not visited[newx][newy]:
        return True
    else:
        return False


def print_all_path(maze, row, col, srcx, srcy, output, visited):
    # base case
    # destination coordinates are [row-1], [col-1]
    if srcx == row - 1 and srcy == col - 1:
        # reached destination
        print(output)
        return

    # 1 case solve karo and baakai recursion sambhal lega

    # UP
    newx, newy = srcx - 1, srcy
    if is_safe(srcx, srcy, newx, newy, maze, row, col, visited):
        visited[newx][newy] = True
        output += 'U'
        print_all_path(maze, row, col, newx, newy, output, visited)
        output = output[:-1]
        visited[newx][newy] = False

    # RIGHT
    newx, newy = srcx, srcy + 1
    if is_safe(srcx, srcy, newx, newy, maze, row, col, visited):
        visited[newx][newy] = True
        output += 'R'
        print_all_path(maze, row, col, newx, newy, output, visited)
        output = output[:-1]
        visited[newx][newy] = False

    # DOWN
    newx, newy = srcx + 1, srcy
    if is_safe(srcx, srcy, newx, newy, maze, row, col, visited):
        visited[newx][newy] = True
        output += 'D'
        print_all_path(maze, row, col, newx, newy, output, visited)
        output = output[:-1]
        visited[newx][newy] = False

    # LEFT
    newx, newy = srcx, srcy - 1
    if is_safe(srcx, srcy, newx, newy, maze, row, col, visited):
        visited[newx][newy] = True
        output += 'L'
        print_all_path(maze, row, col, newx, newy, output, visited)
        output = output[:-1]
        visited[newx][newy] = False


if __name__ == "__main__":
    maze = [
        [1, 0, 0, 0],
        [1, 1, 0, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 1]
    ]
    row, col = 4, 4
    srcx, srcy = 0, 0
    output = ""

    # create visited 2D ARRAY
    visited = [[False for _ in range(col)] for _ in range(row)]

    if maze[0][0] == 0:
        # src position is Closed, that means RAT cannot move
        print("No Path Exists")
    else:
        visited[srcx][srcy] = True
        print_all_path(maze, row, col, srcx, srcy, output, visited)
