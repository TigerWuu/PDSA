import math

class Airport:
    def airport(self, houses):
        p = self.find_p(houses)
        polar = self.polar_order(houses , p)
        convex = self.convex_point(polar)
        distance = self.avg_distance(convex , polar)
        return distance

    def find_p(self,house):
        p = house[0]
        for i in house:
            if i[1] < p[1]:
                p = i 
        # print("p : ",p)
        return p

    def polar_order(self , house , p):
        polar = []
        for i in house:
            dy = i[1]-p[1]
            dx = i[0]-p[0]
            rad = math.atan2(dy,dx)
            polar.append([i,rad])

        polar = sorted(polar , key = lambda k : k[1])
        # print("polar" , polar)
        return polar

    def convex_point(self , polar):
        corner = [polar[0][0]]
        for i in range(len(polar)):
            if i < 2:
                continue 
            else:
                ccw = self.is_ccw(corner[len(corner)-1], polar[i-1][0] , polar[i][0])
                if ccw > 0:
                    corner.append(polar[i-1][0])

                elif ccw < 0:
                    ccw = self.is_ccw(corner[len(corner)-2] , corner[len(corner)-1] , polar[i][0])
                    while ccw < 0:
                        corner.remove(corner[len(corner)-1])
                        ccw = self.is_ccw(corner[len(corner)-2] , corner[len(corner)-1] , polar[i][0])
                
            if i == len(polar)-1:
                corner.append(polar[i][0])

        # print("corner :" ,corner)
        return corner

    def is_ccw(self , p1 , p2 , p3):
        dx1 = p2[0] - p1[0]
        dy1 = p2[1] - p1[1]
        dx2 = p3[0] - p1[0]
        dy2 = p3[1] - p1[1]
        return (dx1*dy2-dx2*dy1)

    def avg_distance(self , convex , polar):
        min_avg_dis = 0
        if len(convex) < 3:
            return 0
        x_avg = 0
        y_avg = 0
        length = len(polar)
        for house in polar:
            x_avg += house[0][0]/length
            y_avg += house[0][1]/length
        avg_coord = [x_avg ,y_avg]

        for i in range(len(convex)):
            avg_dis = 0
            if i == len(convex)-1:
                road_len = ((convex[0][0]-convex[i][0]) ** 2+(convex[0][1]-convex[i][1]) ** 2) ** 0.5
                avg_dis = self.is_ccw(convex[i] , convex[0] , avg_coord)/road_len
            else:
                road_len = ((convex[i+1][0]-convex[i][0]) ** 2+(convex[i+1][1]-convex[i][1]) ** 2) ** 0.5
                avg_dis = self.is_ccw(convex[i] , convex[i+1] , avg_coord)/road_len
            
            # print("road : ", road_len)
            # print("avg : " ,avg_dis)
            if min_avg_dis == 0:
                min_avg_dis = avg_dis
            elif avg_dis < min_avg_dis:
                min_avg_dis = avg_dis

        return min_avg_dis

if __name__ == "__main__":
    print(Airport().airport([[0,0],[1,0]]))
    """
    0.0
    """
    print(Airport().airport([[0,0],[1,0],[0,1]]))
    """
    *.
    **
    # Convex: [[0, 0], [1, 0], [0, 1]]
    0.2357022603955159
    """
    print(Airport().airport([[0,0],[2,0],[0,2],[1,1],[2,2]]))
    """
    *.*
    .*.   
    *.*
    # Convex: [[0, 0], [2, 0], [2, 2], [0, 2]]
    1.0
    """
    print(Airport().airport([[1,1],[2,2],[0,2],[2,0],[2,4],[3,3],[4,2],[4,1],[4,0]]))
    """
    ..*..
    ...*.
    *.*.*
    .*..*
    ..*.*
    # Convex: [[0, 2], [2, 0], [4, 0], [4, 2], [2, 4]]
    1.3356461422412562
    """    





