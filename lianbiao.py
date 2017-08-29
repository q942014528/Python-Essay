#coding=utf-8
class LINKERROR(ValueError):
    pass
class lNode:
    def __init__(self,elem,next_=None):
        self.elem = elem
        self.next = next_
class LList(object):
    def __init__(self):
        self.head = None
        self.last = None
    def is_empty(self):
        return self.head is None
    def prepend(self,elem):
        self.head = lNode(elem,self.head)
        if self.last is None:
            self.last = self.head
    def pop_first(self):
        if self.head is None:
            raise LINKERROR("in pop")
        self.head = self.head.next
        if self.head is None:
            self.last = None
    def append(self,elem):
        
        if self.head.next is None:

            self.head.next = lNode(elem)
            self.last = self.head.next
            
            return 
        if self.last is not None:

            self.last.next = lNode(elem=elem)
            self.last = self.last.next

            print self.last.elem
    def pop_last(self):
        if self.head is None:
            raise LINKERROR("in pop")
        p = self.head
        if p.next is None:
            e = p.elem

            self.head = None
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        self.last = p
        p.next = None
        return e
    def filter(self,pred):
        p = self.head

        while p is not None:

            if pred==p.elem:
                yield p.elem
            p = p.next
        
    def print_all(self):
        p = self.head
        while p is not None:
            yield p.elem
            p = p.next
            


if __name__ == "__main__":
    lb = LList()

    for i in range(10):
        lb.prepend(i)
    for i in xrange(1000,1010):
        lb.append(i)
    
    # for i in lb.print_all():
    #     print i
    print"--------------" 
    
    
 

