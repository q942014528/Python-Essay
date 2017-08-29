#coding=utf-8


def search(array,key):
    '''可以查找首次出现的值的下标'''
    mins = len(array)-1  
    maxs = 0
    sss = 0
    if array[0]>=key:
        return '下标为:0'
    elif array[-1]<key:
        return '下标为:%d'%len(array)-1  
    while maxs < mins:
        
        mid = (maxs+mins)//2
        # print array[cen]
        if array[mid]>key:
            if array[mid-1]<key:
                return mid
                
            mins = mid-1
            
        elif array[mid]<key:
          
            if array[mid+1]>key:
                return mid+1
                
            maxs = mid+1
            

        else:
            for i in range(mid-1,0,-1):
                if array[i]<key:
                    return '下标为:%d'%(i+1)
                    
            
            
        


if __name__  ==  '__main__':
    num = [1,4,7,9,10,15,25,44,55,77,77,77,90,150,156,178,250,450,555,555,555,555,555,555,555,555,900,1000,1001]
    key = 555
    index = search(num,key)
    print index