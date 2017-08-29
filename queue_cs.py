#coding=utf-8
class QueueError(ValueError):
    pass
'''
链表实现队列


class LQueue(object):
    def __init__(self,elem,next_=None):
        self.elem = elem
        self.next = next_
class Queue(object):
    def __init__(self):
        self.head = None
        self.last = None
    def is_empty(self):
        return self.head is None

    def enqueue(self,elem):
        if self.head is None:
            self.head = LQueue(elem,self.head)
            self.last = self.head
            return
      
        if self.last is not None:
            self.last.next = LQueue(elem)
            self.last = self.last.next

    def dequeue(self):
        if self.head is None:
            raise QueueError
        
        e = self.head.elem
        self.head = self.head.next
        return e
    

    def peek(self):
        if self.head is None:
            raise QueueError
        return self.head.elem
q = Queue()
q.enqueue(10)
q.enqueue(5)
q.enqueue(9)
print q.dequeue()

print q.peek()
'''

'''列表实现队列'''
class Queue(object):
    def __init__(self,len_list=8):
        self.elems = [0]*len_list
        self.len_ = len_list
        self.num = 0
        self.head = 0
    def is_empty(self):
        return self.num == 0

    def peek(self):
        if self.num == 0:
            raise QueueError
        return self.elems[self.head]
    def dequeue(self):
        if self.num == 0:
            raise QueueError
        e = self.elems[self.head]
        self.head = (self.head+1)%self.len_
        self.num-=1
        return e

    def enqueue(self,elem):
        if self.num == self.len_:
            self._entend()
        self.elems[(self.head+self.num)%self.len_] = elem
        self.num +=1
    def _entend(self):
        old_len = self.len_
        self.len_ *= 2
        new_elem = [0]*self.len_
        for i in range(old_len):
            new_elem[i] = self.elems[self.head+i%old_len]
            
        self.elems,self.head = new_elem,0



    

q = Queue()
q.enqueue(10)
q.enqueue(5)
q.enqueue(9)
print q.dequeue()
print q.peek()
