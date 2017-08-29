#coding=utf-8

def balance(li):
    """
    取平衡点
    """
    for i in range(1,len(li)-1):
        num1 = 0
        num2 = 0
        for r in range(len(li)):
            if i==r:
                continue
            elif r<i:
                
                num1+=li[r]
            else:
                num2+=li[r]
        if num1==num2:
            return li[i],i

if __name__=="__main__":
    li = [8,9,50,10,10,10,10,10,10,20,5,12]
    print balance(li)