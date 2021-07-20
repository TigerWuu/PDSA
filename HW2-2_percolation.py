from time import time


class Percolation():
    def __init__(self , N):
        self.num = N
        self.grids = []
        self.full = []
        self.virtual_node = "x"
        for i in range(N):
            self.grids.append([])
            self.full.append([])
            j = 0
            while j < N:
                self.grids[i].append("x")
                self.full[i].append("x")
                j += 1

    def root(self , p):
        #### function iteration
        # if p == self.grids[p[0]][p[1]]:
        #     return p
        # else:
        #     self.parents.append(self.grids[p[0]][p[1]])
        #     return self.root(self.grids[p[0]][p[1]]) 
        # for i in self.parents:    #update
        #     self.grids[i[0]][i[1]] = p
        # return p

        ####   while loop

        parents = []
        while p != self.grids[p[0]][p[1]]:
            parents.append(self.grids[p[0]][p[1]])
            # self.grids[p[0]][p[1]] = self.grids[self.grids[p[0]][p[1]][0]][self.grids[p[0]][p[1]][1]]
            p = self.grids[p[0]][p[1]]
            # p = self.grids[self.grids[p[0]][p[1]][0]][self.grids[p[0]][p[1]][1]]

        for i in parents:    #update root
            # if i[0] == self.num-1 and self.virtual_node[0] > p[0]:
            #     self.virtual_node = p
            self.grids[i[0]][i[1]] = p
        return p

    def root_full(self , p):

        parents = []
        while p != self.full[p[0]][p[1]]:
            parents.append(self.full[p[0]][p[1]])
            p = self.full[p[0]][p[1]]

        for i in parents:    #update root
            self.full[i[0]][i[1]] = p
        return p  

    def union(self, p , q):
        root_p = self.root(p)
        root_q = self.root(q)

        root_p_full = self.root_full(p)
        root_q_full = self.root_full(q)

        if root_p[0] > root_q[0]:
            self.grids[root_p[0]][root_p[1]] = root_q
        else:
            self.grids[root_q[0]][root_q[1]] = root_p

        if root_p_full[0] > root_q_full[0]:
            self.full[root_p_full[0]][root_p_full[1]] = root_q_full
        else:
            self.full[root_q_full[0]][root_q_full[1]] = root_p_full


    def union_virtual(self, p , q):
        root_p = self.root(p)
        root_q = self.root(q)

        if root_p[0] > root_q[0]:
            self.grids[root_p[0]][root_p[1]] = root_q
        else:
            self.grids[root_q[0]][root_q[1]] = root_p

    def open(self , i , j):
        
        self.full[i][j] = [i,j]
        self.grids[i][j] = [i,j]
        p = [i,j]
        if i+1 < self.num: 
            q = [i+1,j]
            if self.isOpen(q[0],q[1]):
                self.union(p,q)

        if i-1 >= 0:    
            q = [i-1,j]
            if self.isOpen(q[0],q[1]):
                self.union(p,q)

        if j+1 < self.num:
            q = [i,j+1]
            if self.isOpen(q[0],q[1]):
                self.union(p,q)

        if j-1 >= 0: 
            q = [i,j-1]
            if self.isOpen(q[0],q[1]):
                self.union(p,q)
        ### for virtual node

        if i == self.num-1:
            if self.virtual_node == "x":
                self.virtual_node = self.root(p)
            else:
                q = [self.virtual_node[0] , self.virtual_node[1]]
                self.union_virtual(p, q)

    def isOpen(self , i , j):
        if self.grids[i][j] != "x":
            return True
        else:
            return False

    def isFull(self , i , j):
        p = [i,j]
        if self.root_full(p)[0] == 0:
            return True
        else:
            return False 
        
    def percolates(self): 
        if self.virtual_node != "x":
            if self.root(self.virtual_node)[0] == 0:
                return True 

        # for i in range(self.num):
        #     if self.isOpen(self.num-1 , i):
        #         if self.isFull(self.num-1 , i):
        #             return True
        
        return False

if __name__ == "__main__":
    first_start = time()

    s = Percolation(3)
    s.open(1,1)
    print(s.isFull(1, 1)) 
    print(s.percolates())
    s.open(0,1)
    s.open(2,0)
    print(s.isFull(1, 1)) 
    print(s.isFull(0, 1)) 
    print(s.isFull(2, 0))
    print(s.percolates())
    s.open(2,1)
    print(s.isFull(1, 1)) 
    print(s.isFull(0, 1))
    print(s.isFull(2, 0)) 
    print(s.isFull(2, 1)) 
    print(s.percolates())

    first_finish = time()
    processing_1 = first_finish - first_start
    print("time : " , processing_1)
