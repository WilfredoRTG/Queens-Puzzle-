import time
inicio = time.time()
def dispo(board,fila):
    for i in range(fila):
        if(board[i] == board[fila]) or (abs(fila-i) == abs(board[fila]-board[i])):
            return False
    return True

def nuevaReina(board,fila,n,top):
    if (fila>=n):
        return False
    ok = False
    while (True):
        if (board[fila]<n):
            board[fila] = board[fila] + 1
        if (dispo(board,fila)):
            if (fila != n-1):
                ok = nuevaReina(board,fila+1,n,top)
                if (ok==False):
                    board[fila+1]=0
            else:
                ok=True
        if(board[fila]==n or ok==True):
            break
    return ok

def tablero(board,top):
    for i in range(len(board)):
        for j in range(len(board)):
            if (board[i]==j+1):
                print("Reina en: ", i+1,top[j+1])
    
    print("\n","Tablero")
    for i in range(len(top)):
        print("",top[i],end="")
    print("")
    
    for i in range(len(board)):
        print((i+1),"|",end="")
        for j in range(len(board)):
            if (board[i]==j+1):
                print(1,end="|")
            else:
                print(0,end="|")
        print("")
            
            
top = [" ","a","b","c","d","e","f","g","h"]
board=[0]*8
nuevaReina(board,0,8,top)
tablero(board,top)


fin=time.time()
print("\nTiempo de ejecución:",fin-inicio)
