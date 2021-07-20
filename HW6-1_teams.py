import sys
sys.setrecursionlimit(400000) 

class Teams:
    def teams(self, idols, teetee):
        self.num_idols = idols
        self.idols_graph = []
        self.marked = []
        self.color = []
        for i in range(self.num_idols):
            self.marked.append(False)
            self.color.append(None)
            self.idols_graph.append([])
        ### make adjancy list
        self.relation(teetee)
        ### conduct dfs
        for init in range(len(self.idols_graph)):
            if self.dfs(self.idols_graph , init) == False:
                return False
        return True

    def relation(self , tee):
        for i in range(len(tee)):
            self.idols_graph[tee[i][0]].append(tee[i][1])
            self.idols_graph[tee[i][1]].append(tee[i][0])

    def dfs(self , graph , init):
        if self.marked[init] == False:
            if self.color[init] == None:
                self.color[init] = "white"

            self.marked[init] = True

            for i in range(len(graph[init])):
                if self.marked[graph[init][i]] == False:
                    ### assign color
                    if self.color[init] == "white":
                        self.color[graph[init][i]] = "red"
                    else:
                        self.color[graph[init][i]] = "white"

                    if self.dfs(graph ,graph[init][i]) == False:
                        return False 
                else:
                    if self.color[graph[init][i]] == self.color[init]:
                        return False
            return True
        else:
            return True

if __name__ == "__main__":
    # example 1: True
    print(Teams().teams(4, [[0,1],[0,3],[2,1],[3,2]]))
    # example 1: False
    print(Teams().teams(4, [[0,1],[0,3],[0,2],[2,1],[3,2]]))


    # print(Teams().teams(8, [[0,1],[1,2],[2,7],[4,7]]))

    # print(Teams().teams(8, [[0,1],[0,3],[2,1],[3,2],[4,5],[4,7],[7,6],[6,5],[3,6]]))
    