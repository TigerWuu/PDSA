from functools import cmp_to_key


class Cluster:
    def cluster(self, points, cluster_num):
        weights = []
        i = 0
        while i < len(points):
            weights.append(1)
            i += 1
            
        self.num = len(points)
        while self.num > cluster_num:
            dis = None
            min_i = None
            min_j = None
            for i in range(len(points)):
                if i == len(points)-1:
                    break
                for j in range(i+1 , len(points)):
                    if dis == None:
                        dis = self.distance(points[i] , points[j])
                        min_i = i
                        min_j = j
                    elif self.distance(points[i] , points[j]) < dis:
                        dis = self.distance(points[i] , points[j])
                        min_i = i
                        min_j = j

            cen = self.centroid(points[min_i] , points[min_j] , weights[min_i] , weights[min_j])
            a = points[min_i]
            b = points[min_j]
            points.remove(a)
            points.remove(b)
            points.append(cen)

            cen_weight = weights[min_i] + weights[min_j]
            a_weight = weights[min_i]
            b_weight = weights[min_j]
            weights.remove(a_weight)
            weights.remove(b_weight)
            weights.append(cen_weight)
            self.num -= 1
        points = sorted(points , key = cmp_to_key(compare))
        return points

    def distance(self , a ,b):
        dis = ((a[0]-b[0]) ** 2 + (a[1]-b[1]) ** 2) ** 0.5
        return dis

    def centroid(self , i , j , weights_i , weights_j):
        cen_x = (i[0]*weights_i+j[0]*weights_j)/(weights_i+weights_j)
        cen_y = (i[1]*weights_i+j[1]*weights_j)/(weights_i+weights_j)
        cen = [cen_x , cen_y]
        return cen

def compare(a,b):
    if a[0] > b[0]:
        return 1
    elif a[0] < b[0]:
        return -1
    else:
        if a[1] > b[1]:
            return 1
        elif a[1] < b[1]:
            return -1
        else:
            return 0


if __name__ == "__main__":
    print(Cluster().cluster([[0,0], [1,0], [3,0], [0,1]], 2)) 
    # [[0.3333333333333333, 0.3333333333333333], [3, 0]] 
    # [0,0], [1,0], [0,1] are in same cluster
    # [3,0] are in another cluster

    print(Cluster().cluster([[0,3], [3,3], [4,7], [9,0], [9,4]], 3)) 
    # [[1.5, 3.0], [4, 7], [9.0, 2.0]]

    print(Cluster().cluster([[0,1], [0,2], [3,1], [3,2]], 2)) 
    # [[0.0, 1.5], [3.0, 1.5]]