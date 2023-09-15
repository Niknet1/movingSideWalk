import math

with open('moving_sidewalk.dat') as f:
    lines = f.readlines()
    print(lines)
    maze = []
    mazeL = 0
    mazeW = 0
    for x in lines:
        strX = str(x)
        print(strX.find("/"))
        if strX.find("/") >= 0:
            maze = []
            mazeL = int(x[:x.index('/')])
            mazeW = int(x[x.index('/')+1:])

        else:
            xAsList=[]
            for m in x:
                xAsList.append(m)
            xAsList.remove('\n')

            maze.append(xAsList)
        print(maze)
        print(len(maze))


        if len(maze)==mazeL:
            startcoord = []
            endCoord = []
            pointercoord = startcoord
            moveCnt = 0
            lessmoveCnt = 9999999999999
            for row in range(mazeW):
                for col in range(mazeL):
                    if maze[row][col] == 'S':
                        startcoord.append(row)
                        startcoord.append(col)
                    elif maze[row][col] == 'D':
                        endCoord.append(row)
                        endCoord.append(col)
            for x in range(math.exp(6)):
                if maze[pointercoord[0]][pointercoord[1]+1] =='>':
                    if maze[pointercoord[0]][pointercoord[1]+2] == '>':




