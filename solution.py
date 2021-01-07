def solution(floor):
    """
    >>> floor1 = [ [0, 1], [0, 0] ]
    >>> solution(floor1)
    3
    >>> floor2 = [ [0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0] ]
    >>> solution(floor2)
    7
    >>> floor3 = [
    ... [0, 1, 1, 0],
    ... [0, 0, 0, 0],
    ... [1, 0, 1, 0],
    ... [1, 1, 1, 0] ]
    >>> solution(floor3)
    7
    >>> floor4 = [
    ... [0, 0, 0, 0],
    ... [0, 0, 1, 1],
    ... [1, 0, 1, 0],
    ... [1, 0, 0, 0] ]
    >>> solution(floor4)
    7
    """
    height = len(floor)
    width = len(floor[height - 1])

    maze_num_path = []  # build a new matrix with all 0 entries
    for h in range(height):
        maze_num_path.append([])
        for w in range(width):
            maze_num_path[-1].append(0)
    maze_num_path[0][0] = 1     # set start point as one, matrix will be filled with number of steps for each path

    step = 0    # below will fill matrix with with steps to each accessible point from start to end
    while maze_num_path[-1][-1] == 0: # checks to make sure end point is zero ie have not reached end yet
        step += 1
        for i in range(len(maze_num_path)):  # i == height
            for j in range(len(maze_num_path[i])):  # j == width
                if maze_num_path[i][j] == step:
                    if i > 0 and maze_num_path[i-1][j] == 0 and floor[i-1][j] == 0:     # step up
                        maze_num_path[i-1][j] = step + 1
                    if j > 0 and maze_num_path[i][j-1] == 0 and floor[i][j-1] == 0:     # step left
                        maze_num_path[i][j-1] = step + 1
                    if i < len(maze_num_path)-1 and maze_num_path[i+1][j] == 0 and floor[i+1][j] == 0:  # step down
                        maze_num_path[i+1][j] = step + 1
                    if j < len(maze_num_path[i])-1 and maze_num_path[i][j+1] == 0 and floor[i][j+1] == 0:   # step right
                        maze_num_path[i][j+1] = step + 1

    # find shortest path working backwards
    step = maze_num_path[-1][-1]
    the_path = [(i, j)]  # list of indexes on the path
    while step > 1:
        if i > 0 and maze_num_path[i - 1][j] == step - 1:   # step up
            i, j = i - 1, j
            the_path.append((i, j))
            step -= 1
        elif j > 0 and maze_num_path[i][j - 1] == step - 1:     # step left
            i, j = i, j-1
            the_path.append((i, j))
            step -= 1
        elif i < len(maze_num_path) - 1 and maze_num_path[i + 1][j] == step - 1:    # step down
            i, j = i+1, j
            the_path.append((i, j))
            step -= 1
        elif j < len(maze_num_path[i]) - 1 and maze_num_path[i][j + 1] == step - 1:     # step right
            i, j = i, j+1
            the_path.append((i, j))
            step -= 1
    return len(the_path)


    # #  Attempt 1
    # j = 0   # width
    # i = 0   # height
    # count = 1
    #
    # while (i < len(floor)) and (j < len(floor[i])):  # height and width
    #     if (i + 1 < len(floor)) and floor[i + 1][j] == 0:
    #         i += 1
    #         count += 1
    #     elif (j + 1 < len(floor[i])) and floor[i][j + 1] == 0:
    #         j += 1
    #         count += 1
    #     elif (i + 1 == len(floor)) and (j + 1 == len(floor[i])):
    #         break
    #     elif (i - 1 >= 0) and floor[i-1][j] == 0:
    #         i -= 1
    #         count += 1
    #     elif (j - 1 >= 0) and floor[i][j - 1] == 0:
    #         j -= 1
    #         count += 1
    # return count

    # repeat below until at bottom right most corner
        # is the spot to the right a wall or floor
        # is the spot to the bottom a wall or floor
        # is the spot to the left a wall or floor
        # is the spot to the top a wall or floor
        # physically move and increment count once i know it is a floor


if __name__ == '__main__':
    import doctest
    doctest.testmod()
