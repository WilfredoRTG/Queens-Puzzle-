'''
Algoritmo fuerza bruta
Tablero de 8x8, 8 reinas que no son capaces de eliminarse entre ellas
Representar Reinas con 1 y espacios blancos con 0
'''
import time
inicio = time.time()
def dispo(row, col):
    for i in range(8):  #Recorre La matriz en busca de 1
        if board[row][i] == 1 or board[i][col] == 1:
            return False
            
    if row <= col:
        colum = col - row
        fila = 0
    else:
        fila = row - col
        colum = 0
    while colum < 8 and fila < 8:
        if board[fila][colum] == 1:
            return False
        fila += 1
        colum += 1
    if row <= col:
        fila = 0
        colum = col + row
        if colum > 7:
            fila = colum - 7
            colum = 7
    else:
        colum = 7
        fila = row - (7 - col)
    while colum >= 0 and fila < 8:
        if board[fila][colum] == 1:
            return False
        fila += 1
        colum -= 1
    return True
        

def nuevaReina(n):
    if n<1:
        return True
    
    for i in range(8):
        for j in range(8):
            if dispo(i,j):      #backtraking
                board[i][j]=1
                if nuevaReina(n-1): #recursion 
                    print("Reina en: ", i+1,top[j+1])
                    return True
                else:
                    board[i][j]=0
                
    return False
    
top = [" ","a","b","c","d","e","f","g","h"]
board=[[0]*8 for i in range(8)]
nuevaReina(8)

print("\n","Tablero")

for i in range(len(top)):
    print("",top[i],end="")
print()

for i in range(len(board)):
    print((i+1),"|",end="")
    for j in range(len(board)):
        print(board[i][j],end="|")
    print("")

fin=time.time()
print("\nTiempo de ejecución:",fin-inicio)
