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

    




    #  Attempt 1
    j = 0
    i = 0
    count = 1

    while (i < len(floor)) and (j < len(floor[i])):  # height and width
        if (i + 1 < len(floor)) and floor[i + 1][j] == 0:
            i += 1
            count += 1
        elif (j + 1 < len(floor[i])) and floor[i][j + 1] == 0:
            j += 1
            count += 1
        elif (i + 1 == len(floor)) and (j + 1 == len(floor[i])):
            break
        elif (i - 1 >= 0) and floor[i-1][j]:
            i -= 1
            count += 1
        elif (j - 1 >= 0) and floor[i][j - 1]:
            j -= 1
            count += 1

    return count

    # repeat below until at bottom right most corner
        # is the spot to the right a wall or floor
        # is the spot to the bottom a wall or floor
        # is the spot to the left a wall or floor
        # is the spot to the top a wall or floor
        # physically move and increment count once i know it is a floor


if __name__ == '__main__':
    import doctest
    doctest.testmod()
