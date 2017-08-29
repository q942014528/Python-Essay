#coding=utf-8
#求最小差
import random


def Mininum(ar1,ar2):
    """
    局部最优解
    """
    if len(ar1) != len(ar2):
        return
    
    num1 = reduce(lambda x,y:x+y,ar1)
    num2 = reduce(lambda x,y:x+y,ar2)
    length = len(ar1)
    if num1<num2:
        ar1,ar2 = ar2,ar1
    print"---------------------"
    print ar1,ar2
    temp = True
    while temp:
        temp = False
        for i in range(length):
            for r in range(length):
                numindex = ar1[i]-ar2[r] 
                numsmall = sum(ar1) - sum(ar2)

                if (numindex<numsmall) and (numindex>0):
                    temp=True
                    ar1[i],ar2[r] = ar2[r],ar1[i]
    return ar1,ar2




        












array1 = []
array2 = []
for i in xrange(10):
    array1.append(random.randint(1,100))
    array2.append(random.randint(1,100))
print(array1,array2)
print sum(array1),sum(array2)
array1,array2 = Mininum(array1,array2)
print(array1,array2)
print sum(array1),sum(array2)