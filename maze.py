'''
->First funtion to create maze board size (n*n)
->Top left corner i.e Start and Bottom right corner i.e End represented by "S" and "E" with green color.
UNIQUE CODE:
for Walls :Full block(U+2588) (Red)
for Open space :Dotted circle(U+25CC)(Blue)
for Path : Circle With Vertical Fill(U+25CD)(Green)
'''
from colorama import Fore
import random
def mazeCreate(n):
    box = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == 0 and j == 0:
                row.append(Fore.GREEN + "S" + Fore.RESET)   #Start point (S) 
            elif i == n - 1 and j == n- 1:
                row.append(Fore.GREEN + "E" + Fore.RESET)   #End point (E)
            else:
                row.append(Fore.BLUE + u"\u25cc" + Fore.RESET)
        box.append(row)
    
        

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
                box[i][j]=Fore.RED+u"\u2593"+Fore.RESET

    return box
def printMaze(box, size):
    hrow = Fore.RED + '+' + '---+' * size + Fore.RESET
    for i in range(size):
        print(hrow)
        print("| ", end="")
        for j in range(size):
            print(box[i][j], end=" | ")
        print()

    print(hrow)
size=int(input("Enter Maze Size :"))
maze = mazeCreate(size)
printMaze(maze, size)
