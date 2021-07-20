from time import time

class BoardGame():
    def __init__(self , h ,w):
        self.height = h
        self.width = w
        self.type = {}
        self.edges = 4

        # for i in range(h):
        #     self.board.append([])
        #     self.counter.append([])
        #     self.grids.append([])
        #     self.type[(x,y)] = [[x,y] , stoneType ,0]
        #     j = 0 
        #     while j < w:
        #         self.board[i].append(".")
        #         self.counter[i].append(0)
        #         self.grids[i].append([])
        #         j += 1

    def putStone(self, x , y , stoneType):
        for i in range(len(x)):
            #print([x[i],y[i]])
            self.type[(x[i],y[i])] = [[x[i],y[i]] , stoneType , 0]
            #print(self.type)

            if x[i] == self.height-1 or x[i] == 0 or y[i] == self.width-1 or y[i] == 0:
                self.type[(x[i],y[i])][2] = 1000
            else : 
                self.type[(x[i],y[i])][2] = self.edges


            p = x[i]+1
            q = y[i]
            if p < self.height and (p,q) in self.type:
                if self.type[(p,q)][1] == stoneType:
                    self.union([p,q] , [x[i],y[i]])

                else:
                    roo = self.root([x[i],y[i]])
                    roo_d = self.root([p,q])
                    self.type[(roo[0],roo[1])][2] -= 1
                    self.type[(roo_d[0],roo_d[1])][2] -= 1

            p = x[i]-1
            q = y[i]
            if p >=0 and (p,q) in self.type:
                if self.type[(p,q)][1] == stoneType:
                    self.union([p,q] , [x[i],y[i]])

                else:
                    roo = self.root([x[i],y[i]])
                    roo_d = self.root([p,q])
                    self.type[(roo[0],roo[1])][2] -= 1
                    self.type[(roo_d[0],roo_d[1])][2] -= 1


            p = x[i]
            q = y[i]+1
            if q < self.width and (p,q) in self.type:
                if self.type[(p,q)][1] == stoneType:
                    self.union([p,q] , [x[i],y[i]])

                else:
                    roo = self.root([x[i],y[i]])
                    roo_d = self.root([p,q])
                    self.type[(roo[0],roo[1])][2] -= 1
                    self.type[(roo_d[0],roo_d[1])][2] -= 1


            p = x[i]
            q = y[i]-1
            if q >=0 and (p,q) in self.type:
                if self.type[(p,q)][1] == stoneType:
                    self.union([p,q] , [x[i],y[i]])

                else:
                    roo = self.root([x[i],y[i]])
                    roo_d = self.root([p,q])
                    self.type[(roo[0],roo[1])][2] -= 1
                    self.type[(roo_d[0],roo_d[1])][2] -= 1

    
    def union(self, p , q):
        root_p = self.root(p)
        root_q = self.root(q)

        if root_p[0] > root_q[0]:
            self.type[(root_p[0],root_p[1])] = root_q
            self.type[(root_q[0],root_q[1])][2] = self.type[(root_p[0],root_p[1])][2] +self.type[(root_q[0],root_q[1])][2] - 2
        else:
            self.type[(root_q[0],root_q[1])] = root_p
            self.type[(root_p[0],root_p[1])][2] = self.type[(root_p[0],root_p[1])][2] +self.type[(root_q[0],root_q[1])][2] - 2

    def root(self , p):
        parents = []
        while p != self.type[(p[0],p[1])][0]:
            parents.append(self.type[(p[0],p[1])][0]) 
            p = self.type[(p[0],p[1])][0]
        
        for i in parents:    #update root
            self.type[(i[0],i[1])][0] = p
        return p

    def surrounded(self , x ,y):
        if x == self.height-1 or x == 0 or y == self.width-1 or y == 0:
            return False

        roo = self.root([x,y])       
        if self.type[(roo[0],roo[1])][2] == 0:
            return True
        else:
            return False

    def getStoneType(self , x , y):
        stoneType = self.type[(x,y)][1]
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

    print(g.type)
    
    first_finish = time()
    processing_1 = first_finish - first_start
    print("time : " , processing_1)