#coding=utf-8
class StackError(ValueError):
    pass
"""
list形式stack
class SStack(object):
    def __init__(self):
        self._elem = []

    def is_empty():
        return self._elem == []

    def push(self,elem):
        self._elem.append(elem)
    def pop(self):
        if self._elem == []:
            raise StackError
        return self._elem.pop()

    def top(self):
        if self._elem == []:
            raise StackError
        return self._elem[-1]

st = SStack()
st.push(5)
st.push(10)
while st.is_empty:
    print(st.pop())
"""
class LNode(object):
    def __init__(self,elem,next_):
        self.elem = elem
        self.next = next_
class SStack(object):
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head is None

    def push(self,elem):
        self.head = LNode(elem,self.head)
    def pop(self):
        if self.head is None:
            raise StackError
        e = self.head.elem
        self.head = self.head.next
        return e 
    def top(self):
        if self.head is None:
            raise StackError
        return self.head.elem
st = SStack()
st.push(5)
st.push(10)
while st.is_empty:
    print(st.pop())











