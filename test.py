# import heapq


# # for i in range( 4 , 5):
# #     print(i)

# # yyy = {3:[] , 4 : [[4,7] , [4,5]]}
# # yyy[3].append([1,2])

# # print(yyy[3])
# import math

# if "x" != 5:
#     print("ttt")

# x=["c","c"]
# if x[0] == 0:
#     print("fff")
# else : print("ddd")

# for i in []:
#     print("nmm")

# type = {}
# type[(1,2)] = [[2,3] , "x" , 0]
# print(type)

# a=5
# b=6
# c=a/b
# print(c)

# print(list(range(1,6)))

# print(math.atan2(1,-1))

# print(0>0)


# x = [[0,0], [1,0], [3,0], [0,1],[4,7],[1,2]]
# print(x)
# heapq.heapify(x)
# print(x)

# y = [3,4,5,2,7,986,2]
# print(y)
# heapq.heapify(y)
# print(y)

# for i in range(1,4):
#     print(i)

import sys


class test:
    def __init__(self, a , b):
        self.a = a
        self.b = b



if __name__ == "__main__":
    te = test(1 ,2)
    print(te.a)
    print(te)
    print("-----")
    x = test(2 , 3)
    print(x)
    x.a = te.a
    x.b = te.b
    print(x.a)
    print(x)
    print("-----")
    x.a = 3
    print(x.a)
    print(te.a)

    #print(None > None)

def ttt():
    return True


print(ttt())

print(None == "ddd")

als = []
for i in range (len(als)):
    print("dddd")

print(range(2))

def aaa(a):
    if a==0:
        return False

print(aaa(1))
if aaa(1) == False:
    print("fff")

print(None == False)

def ddd():
    return False

def aaa():
    ddd()
    if ddd() == False:
        return True

sys.setrecursionlimit(1500) 
def function(tee):
    if tee >= 0:
        tee -= 1 
        function(tee)

function(999)
