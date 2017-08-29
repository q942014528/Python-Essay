#coding=utf-8
import random,time
def QuickSort(array,first,last):

    if first<last:
        index = sorts(array,first,last)
        QuickSort(array,first,index)
        QuickSort(array,index+1,last)




def sorts(array,first,last):
    tmp = array[first]
    while first<last:
        while first<last and array[last]>=tmp:
            last-=1
        if first<last:
            array[first],array[last] = array[last],array[first]
        else:
            break
        while first<last and array[first]<tmp:
            first+=1
        if first<last:
            array[first],array[last] = array[last],array[first]
        else:
            break
    return first

            


array = []
for i in range(1000000):
    array.append(random.randint(0,100000000))

t1 = time.time()
QuickSort(array,0,len(array)-1)
t2 = time.time()
print(t2-t1)
print"-------------"
