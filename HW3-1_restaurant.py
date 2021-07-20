from functools import cmp_to_key
from time import time


class Restaurant(object):
    def __init__(self, id , rate , price , distance ):
        self.id = id
        self.rate = rate 
        self.price = price
        self.distance = distance

    def getID(self):
        return self.id

    def __lt__(self, b):
        my_cp = self.distance * self.price / self.rate
        b_cp = b.distance * b.price / b.rate
        if my_cp < b_cp:
            return True
        elif my_cp > b_cp:
            return False

    @staticmethod
    def comparator1( a, b):
        if compare_rate(a,b) == 0:
            if compare_distance(a,b) == 0:
                if compare_id(a,b) == 0:
                    return 0
                else:
                    return compare_id(a,b)
            else:
                return compare_distance(a,b)
        else:
            return compare_rate(a,b)

    @staticmethod
    def comparator2(a, b):
        if compare_distance(a,b) == 0:
            if compare_id(a,b) == 0:
                return 0
            else:
                return compare_id(a,b)
        else:
            return compare_distance(a,b)
 

def compare_rate(a,b):
    if a.rate < b.rate:
        return -1
    elif a.rate > b.rate:
        return 1
    else:
        return 0

def compare_rate_inverse(a,b):
    if a.rate < b.rate:
        return 1
    elif a.rate > b.rate:
        return -1
    else:
        return 0
    

def compare_distance(a,b):
    if a.distance < b.distance:
        return -1
    elif a.distance > b.distance:
        return 1
    else:
        return 0


def compare_id(a,b):
    if a.id < b.id:
        return 1
    elif a.id > b.id:
        return -1
    else:
        return 0


class Restaurants(object):
    def __init__(self, restaurants):
        self.restaurants = sorted(restaurants , key=cmp_to_key(Restaurant.comparator2))
        self.answer = {}
        for thres in range(1,6):
            self.answer[thres] = []
            for i in self.restaurants:
                if i.rate >= thres:
                    self.answer[thres].append(i)

        # self.restaurants = sorted(restaurants , key=cmp_to_key(compare_rate_inverse))
        # self.answer = {}
        # for thres in range(1,6):
        #     self.answer[thres] = []
        #     for i in self.restaurants:
        #         if i.rate < thres:
        #             break
        #         else:
        #             self.answer[thres].append(i)
                
        #     self.answer[thres] = sorted(self.answer[thres] , key=cmp_to_key(Restaurant.comparator2))
            
    def filter(self, min_price, max_price, min_rate):
        ans = []
        for i in self.answer[min_rate]:
            if i.price >= min_price and i.price <=max_price:
                ans.append(i.id)

        return ans
        # answer = []
        # for i in self.restaurants:
        #     if i.price >= min_price and i.price <= max_price and i.rate >= min_rate:
        #         answer.append(i.id)
         
        # return answer

if __name__ == "__main__":
    first_start = time()

    rests = [
        # id, rate, price, distance
        Restaurant(20, 1, 20, 12),
        Restaurant(15, 3, 19, 11),
        Restaurant(19, 4, 19, 12),
        Restaurant(18, 5, 20, 11),
    ]
    r = Restaurants(rests)
    print(r.filter(0, 25, 3)) 
    print(r.filter(0, 25, 4)) 
    print(r.filter(0, 20, 1)) 
    print(r.filter(0, 10, 1))
    print(r.filter(0, 19, 1))
    print(r.filter(19, 19, 3))

    # # case6
    rests = [
        # id, rate, price, distance
        Restaurant(3, 2, 3, 8),
        Restaurant(0, 2, 4, 6),
        Restaurant(2, 4, 5, 12),
        Restaurant(1, 5, 6, 11),
    ]
    print([i.getID() for i in sorted(rests)])
    print([i.getID() for i in sorted(rests, key=cmp_to_key(Restaurant.comparator1))])

    first_finish = time()
    processing_1 = first_finish - first_start
    print("time : " , processing_1)
