#coding=utf-8
#质数

def zhishu(num):
    nums = 0
    if num%2==0:

        li = range(2,num,2)
    else:
   _     li = range(3,num,2)
    for i in li:
        nums+=1
        if num%i==0:
            print nums
            print 'i:%d'%i
            return False
    print nums
    return True

num = input("请输入:")
shu = zhishu(num)
print shu