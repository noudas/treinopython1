def printMat(Matriz):
   for i in range(len(Matriz)):
      for j in range(len(Matriz[0])):
         print("%2s"%Matriz[i][j], " ", end="")
      print()
