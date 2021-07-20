import sys
from operator import attrgetter
sys.setrecursionlimit(1000001)


class Railway():

    def railway(self, landmarks, distance):
        edge = []
        MST = []
        uf = unionfind(landmarks)

        for verge in distance:
            brink = weightededge(verge[0] ,verge[1] ,verge[2])
            edge.append(brink)

        edge.sort(key = attrgetter("length"))

        for side in edge:
            if uf.is_union(side.v , side.w) == False:
                MST.append(side)
                uf.union(side.v , side.w)

                if side.v == side.w:
                    continue
                if len(MST) == landmarks - 1:
                    break

        railway_length = self.total_length(MST)
        return railway_length

    def total_length(self, mst):
        total = 0
        for i in mst:
            total += i.length
        return total


class weightededge():
    def __init__ (self , v , w , length):
        self.v = v
        self.w = w
        self.length = length

class unionfind():
    def __init__(self , landmarks):
        self.site_root = []
        for i in range(landmarks):
            self.site_root.append(i)

    def root(self , v):
        parents = []
        while self.site_root[v] != v:
            parents.append(v)
            v = self.site_root[v]
        for i in parents:
            self.site_root[i] = v
        return v

    def union(self , v ,w):
        self.site_root[self.root(v)] = self.root(w)

    def is_union(self , v ,w):
        if self.root(v) == self.root(w):
            return True
        else:
            return False



if __name__ == "__main__":
    print(
    Railway().railway(4,[[0,1,2],
                         [0,2,4], 
                         [1,3,5], 
                         [2,1,1]])
    )
    # Answer: 8 (2 + 5 + 1)

    print(
    Railway().railway(4,[[0,1,0],
                         [0,2,4], 
                         [0,3,4], 
                         [1,2,1], 
                         [1,3,4], 
                         [2,3,2]])
    )
    # Answer: 3(0 + 1 + 2)