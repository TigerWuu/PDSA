from operator import attrgetter


class Mountains:
    def mountains(self, mountains_height):
        self.mountains_height = mountains_height
        self.distance = []
        self.viewed = []
        self.disto = []
        N = len(self.mountains_height)
        M = len(self.mountains_height[0])
        for i in range(N):
            self.distance.append([])
            for j in range(M):
                self.distance[i].append(None)
        ## initialize
        self.distance[0][0] = 0
        i = 0
        j = 0 
        while len(self.viewed) < N*M:
            self.viewed.append([i,j])

            self.relax_mod_j(i , j , i , j+1 , M)
            self.relax_mod_j(i , j , i , j-1 , M)
            self.relax_mod_i(i , j , i+1 , j , N)
            self.relax_mod_i(i , j , i-1 , j , N)

            self.disto.sort(key = attrgetter("energy_lost"))
            
            i = self.disto[0].w[0]
            j = self.disto[0].w[1]

            self.disto.remove(self.disto[0])

        dis = self.distance[N-1][M-1]
        return dis

    def relax_mod_j(self, i , j , new_i , new_j , limit):
        if new_j < limit and new_j >= 0 and [new_i,new_j] not in self.viewed:
            if self.mountains_height[i][j] < self.mountains_height[new_i][new_j]:
                energy = 2*(self.mountains_height[new_i][new_j]-self.mountains_height[i][j])
            else:
                energy = self.mountains_height[i][j] - self.mountains_height[new_i][new_j]

            if self.distance[new_i][new_j] == None:
                self.distance[new_i][new_j] = self.distance[i][j] + energy
            elif self.distance[i][j] + energy < self.distance[new_i][new_j]:
                self.distance[new_i][new_j] = self.distance[i][j] + energy
            
            w_len = dis_to([new_i,new_j] ,self.distance[new_i][new_j])
            self.disto.append(w_len)

    def relax_mod_i(self, i , j , new_i , new_j , limit):
        if new_i < limit and new_i >= 0 and [new_i,new_j] not in self.viewed:
            if self.mountains_height[i][j] < self.mountains_height[new_i][new_j]:
                energy = 2*(self.mountains_height[new_i][new_j]-self.mountains_height[i][j])
            else:
                energy = self.mountains_height[i][j] - self.mountains_height[new_i][new_j]
 
            if self.distance[new_i][new_j] == None:
                self.distance[new_i][new_j] = self.distance[i][j] + energy
            elif self.distance[i][j] + energy < self.distance[new_i][new_j]:
                self.distance[new_i][new_j] = self.distance[i][j] + energy
            
            w_len = dis_to([new_i,new_j] ,self.distance[new_i][new_j])
            self.disto.append(w_len)




class dis_to:
    def __init__(self ,w , distance):
        self.w = w 
        self.energy_lost = distance

if __name__ == "__main__":
    print(Mountains().mountains(
        [[ 0, 1, 2, 3, 4], 
         [24,23,22,21, 5], 
         [12,13,14,15,16],
         [11,17,18,19,20],
         [10, 9, 8, 7, 6]]))
    # ans=42
    print(Mountains().mountains(

        [[3, 4, 5], 
         [9, 3, 5], 
         [7, 4, 3]]))
    # ans=6

    print(Mountains().mountains(

        [[3, 3 ,3], 
         [3, 3, 3], 
         [3, 3, 3]]))