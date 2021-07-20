import sys
sys.setrecursionlimit(1000001)


class Calendar:
    def __init__(self):
        self.calendar = calendar()   

    def book(self, start, end):
        if self.calendar.intersect(start , end):
            return False
        else:
            self.calendar.add(start , end)
            return True

class calendar:
    def __init__(self ,interval=None , max = None ,left=None , right=None):
        self.interval = interval
        self.left = left
        self.right = right
        self.max = max

    def intersect(self , lo , hi):
        if self.interval == None:
            return False
        elif (lo >= self.interval[0] and lo < self.interval[1]) or (hi > self.interval[0] and hi <= self.interval[1]) or (lo <= self.interval[0] and hi >= self.interval[1]):
            return True
        elif self.left == None:
            if self.right == None:
                return False
            else:
                #print("right")
                return self.right.intersect(lo , hi)
        elif self.left.max <= lo:
            if self.right == None:
                #print("-----------------stop_inter")
                return False
            else:
                #print("right")
                return self.right.intersect(lo , hi)
        else:
            #print("left")
            return self.left.intersect(lo , hi)

    def add(self , lo ,hi):
        if self.interval != None:
            self.max = max(self.max , hi)              ### update the maximum value
            if lo > self.interval[0]:
                if self.right == None:
                    #print("-----------------add")
                    self.right = calendar([lo , hi] , hi)
                else:
                    #print("right")
                    self.right.add(lo,hi)

            elif lo < self.interval[0]:
                if self.left == None:
                    #print("-----------------add_left")
                    self.left = calendar([lo , hi] , hi)
                else:
                    self.left.add(lo,hi)
        else:
            self.interval = [lo ,hi]
            self.max = hi
    

if __name__ == "__main__":
    a = Calendar()
    print(a.book(1, 2))
    print(a.book(2, 3))
    print(a.book(3,3))
    print(a.book(3, 4))
    print(a.book(4, 5))
    print(a.book(6, 7))
    print(a.book(10, 20))
    print(a.book(22, 30))
    print(a.book(22, 32))
    print(a.book(23, 33))
    print(a.book(23, 30))
    # a = Calendar()
    # print(a.book(10, 20))
    # a.book(20, 25)
    # a.book(25, 30)
    # a.book(30,35)
    # a.book(35, 40)
    # print(a.calendar.interval)
    # a.book(6, 8)
    # a.book(8, 10)
    # a.book(4, 6)
    # a.book(2, 4)
    # print(a.calendar.interval)
    # print(a.book(3, 5))
    # print(a.book(12,34))
    # print(a.book(30,34))
    # print(a.book(32,34))
    # print(a.book(11,25))
    # print(a.book(8,9))
    # print(a.book(33,45))
    # print(a.book(0,40))


    

    
    

    # """ 
    # True
    # False  #[15, 20) is unavailable
    # True
    # False  #[17, 21] is unavailable
    # True
    # False  #[2, 3) is unavailable
    # True
    # """ 
    # print("------")

    # a = Calendar()
    # print(a.book(5, 15))
    # print(a.book(0, 18))
    # print(a.book(24, 29))
    # print(a.book(13, 25))
    # print(a.book(18, 22))
    # print(a.book(15, 18))
    # """ 
    # True
    # False  #[5, 15) is unavailable
    # True
    # False  #[24, 25] is unavailable
    # True
    # True
    # """