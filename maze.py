'''
->First funtion to create maze board size (n*n)
->Top left corner i.e Start and Bottom right corner i.e End represented by "S" and "E" with green color.
UNIQUE CODE:
for Walls :Full block(U+2593) (Red)
for Open space :Dotted circle(U+25CC)(Blue)
for Path : Circle With Vertical Fill(U+25CD)(Green)
'''
from colorama import Fore
import random
from collections import deque
def mazeCreate(n):
    maze = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == 0 and j == 0:
                row.append(Fore.GREEN + "S" + Fore.RESET)   #Start point (S) 
            elif i == n - 1 and j == n- 1:
                row.append(Fore.GREEN + "E" + Fore.RESET)   #End point (E)
            else:
                row.append(Fore.BLUE + u"\u25cc" + Fore.RESET)
        maze.append(row)
    
        

    #The number of random walls should be restricted to be less than or equal to 25% of the total cells.
    total_cells=n*n
    number_of_cells=total_cells//4

    wall_pairs=[]
    while(len(wall_pairs) < number_of_cells):
        temp_i=random.randint(0,n-1)
        temp_j=random.randint(0,n-1)
        if([temp_i,temp_j] not in wall_pairs):
            wall_pairs.append([temp_i,temp_j])

    #printing random walls on the box
    
    for i in range(n):
        for j in range(n):
            if([i,j] in wall_pairs and [i,j]!=[0,0] and [i,j]!=[n-1,n-1]):
                maze[i][j]=Fore.RED+u"\u2593"+Fore.RESET

    return maze
def printMaze(box, size):
    hrow = Fore.RED + '+' + '---+' * size + Fore.RESET
    for i in range(size):
        print(hrow)
        print("| ", end="")
        for j in range(size):
            print(box[i][j], end=" | ")
        print()

    print(hrow)


#Finding a path from the start to the end using BFS algorithm 
def path_finding(maze,size):
    start=(0,0)
    end=(size-1,size-1)

    paths = []
    visited = set()
    rows = len(maze)
    cols = len(maze[0])

    def algo_BFS(start,end):
        queue=deque()
        visited.add(start)
        queue.append((start,[start]))

        while queue:
            curr,path=queue.popleft()
            visited.add(curr)

            if curr==end:
                paths.append(path)
            
            else:
                i, j = curr[0], curr[1]

                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for dx, dy in directions:
                    new_i, new_j = i + dx, j + dy

                    if new_i in range(rows) and new_j in range(cols) and (new_i, new_j) not in visited and maze[new_i][new_j] != Fore.RED + u"\u2593" + Fore.RESET:
                        queue.append(((new_i, new_j), path + [(new_i, new_j)]))
                        visited.add((new_i, new_j))
    algo_BFS(start,end)
    min_path=0

    for i in range(len(paths)):
        if len(paths[i])<len(paths[min_path]):
            min_path=i
    
    path_found=1
    
    if(len(paths)):
        for i in paths[min_path]:   
            if((i[0]==1 and i[1]==1) or (i[0]==size and i[1]==size)):
                continue
            else:
                maze[i[0]][i[1]] =Fore.GREEN + u'\u25cd' + Fore.RESET
    else:
        path_found=0

    if(path_found):
        print('Generated Maze:')
        printMaze(maze,size)
    else:
        print("No Path exists for the above maze..!")

size=int(input("Enter the Size of the maze (n*n):"))
maze=mazeCreate(size)
path_finding(maze,size)

