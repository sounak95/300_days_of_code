'''
main
└── printAllPath(0,0)
    └── D
        └── printAllPath(1,0)
            ├── U (backtracking - not allowed, so no recursive call)
            ├── R (blocked, so no recursive call)
            ├── D
            │   └── printAllPath(2,0)
            │       ├── U (backtracking - not allowed, so no recursive call)
            │       ├── R (blocked, so no recursive call)
            │       ├── D
            │       │   └── printAllPath(3,0)
            │       │       ├── U (backtracking - not allowed, so no recursive call)
            │       │       ├── R
            │       │       │   └── printAllPath(3,1)  [Continues...]
            │       │       ├── D (blocked, so no recursive call)
            │       │       └── L (blocked, so no recursive call)
            │       └── L (blocked, so no recursive call)
            └── L (blocked, so no recursive call)

'''
'''
a function that will handle all the below mentioned possibilities:
posssiblity hai
-> path closed
out if bound
check is pos is already visited
'''
def isSafe(newx, newy,maze, row, col, visited):
    if (newx>=0 and newx<row) and (newy>=0 and newy<col) and maze[newx][newy]==1 and visited[newx][newy]==False:
        return True
    else:
        return  False

def printAllPath(maze, row, col, srcx, srcy, output, visited):
    # You need to implement this function.
    # base case
    # destination coordinates are [row-1], [col-1]
    if srcx == row-1 and srcy==col-1:
        print(output)
        return

    # 1 case solve karo and baakai recursion sambhal lega
    # UP
    new_x = srcx-1
    new_y = srcy

    if isSafe(new_x, new_y, maze, row, col, visited):
        # mark visited
        visited[new_x][new_y] = True
        # call recursion
        output.append("U")
        printAllPath(maze, row, col, new_x, new_y, output, visited)
        # backtracking
        output.pop()
        visited[new_x][new_y] = False

    # RIGHT
    new_x = srcx
    new_y = srcy+1

    if isSafe(new_x, new_y, maze, row, col, visited):
        # mark visited
        visited[new_x][new_y] = True
        # call recursion
        output.append("R")
        printAllPath(maze, row, col, new_x, new_y, output, visited)
        # backtracking
        output.pop()
        visited[new_x][new_y] = False



    # DOWN
    new_x = srcx +1
    new_y = srcy

    if isSafe(new_x, new_y, maze, row, col, visited):
        # mark visited
        visited[new_x][new_y] = True
        # call recursion
        output.append("D")
        printAllPath(maze, row, col, new_x, new_y, output, visited)
        # backtracking
        output.pop()
        visited[new_x][new_y] = False

    # LEFT
    new_x = srcx
    new_y = srcy-1

    if isSafe(new_x, new_y, maze, row, col, visited):
        # mark visited
        visited[new_x][new_y] = True
        # call recursion
        output.append("L")
        printAllPath(maze, row, col, new_x, new_y, output, visited)
        # backtracking
        output.pop()
        visited[new_x][new_y] = False

def main():
    maze = [
        [1, 0, 0, 0],
        [1, 1, 0, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 1]
    ]
    row = 4
    col = 4

    srcx = 0
    srcy = 0
    output = []

    # create visited 2D list
    visited = [[False for _ in range(col)] for _ in range(row)]

    if maze[0][0] == 0:
        # src position is Closed, that means RAT cannot move
        print("No Path Exists")
    else:
        visited[srcx][srcy] = True
        printAllPath(maze, row, col, srcx, srcy, output, visited)

if __name__ == "__main__":
    main()
