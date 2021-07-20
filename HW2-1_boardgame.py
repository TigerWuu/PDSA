from time import time


class BoardGame():
    def __init__(self , h ,w):
        self.height = h
        self.width = w
        self.type = {}
        self.stonetype = 0
        self.board=[]
        for i in range(h):
            self.board.append([])
            j = 0 
            while j < w:
                self.board[i].append(".")
                j += 1

    def putStone(self, x , y , stoneType):
        for i in range(len(x)):
            self.board[x[i]][y[i]] = stoneType
            

    def surrounded(self , x ,y):
        #print(self.board)
        if x == self.height-1 or x == 0 or y == self.width-1 or y == 0:
            return False
        else:
            self.type = {}
            return self.find_bound(x , y)


    def find_bound(self , x , y):
        self.stonetype = self.board[x][y]
        

        if  self.stonetype in self.type:
            self.type[self.stonetype].append([x , y])
        else:
            self.type[self.stonetype] = [[x , y]]

        # p = x+1
        # q = y
        if self.board[x+1][y] not in self.type[self.stonetype]:
            if x+1 < self.height:
                if self.board[x+1][y] == self.stonetype:
                    if self.find_bound(x+1 , y) == False:  ## false represent that the piece doesn ot be surrounded         
                        return False

                elif self.board[x+1][y] == ".":
                    return False
            else:
                return False

        # p = x-1
        # q = y
        if self.board[x-1][y] not in self.type[self.stonetype]: 
            if x-1 >=0:
                if self.board[x-1][y] == self.stonetype:
                    
                    if self.find_bound(x-1 , y) == False:  ## false represent that the piece doesn ot be surrounded
                        return False

                elif self.board[x-1][y] == ".":
                    return False
            else:
                return False

        # p = x
        # q = y+1
        if self.board[x][y+1] not in self.type[self.stonetype]: 
            if y+1 < self.width:

                if self.board[x][y+1] == self.stonetype:

                    if self.find_bound(x , y+1) == False:  ## false represent that the piece doesn ot be surrounded
                        return False

                elif self.board[x][y+1] == ".":
                    return False
            else:
                return False

        # p = x
        # q = y-1
        if self.board[x][y-1] not in self.type[self.stonetype]:
            if y-1 >=0:
                if self.board[x][y-1] == self.stonetype:

                    if self.find_bound(x ,y-1) == False:  ## false represent that the piece doesn ot be surrounded
                        return False

                elif self.board[x][y-1] == ".":
                    return False
            else:
                return False

        return True        ## true represents that the piece is surrounded

    def getStoneType(self , x , y):
        stoneType = self.board[x][y]
        return stoneType

if __name__ == "__main__":
    first_start = time()

    g = BoardGame(3, 3)
    g.putStone([1], [1], 'O')
    print(g.surrounded(1, 1))

    g.putStone([0, 1, 1], [1, 0, 2], 'X')
    print(g.surrounded(1, 1))

    g.putStone([2], [1], 'X')
    print(g.surrounded(1, 1))
    print(g.surrounded(2, 1))

    g.putStone([2], [0], 'O')
    print(g.surrounded(2, 0))

    first_finish = time()
    processing_1 = first_finish - first_start
    print("time : " , processing_1)
