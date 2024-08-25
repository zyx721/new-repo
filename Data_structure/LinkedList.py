class Node:
    def __init__(self, data=None, nxt=None):
        self.data = data
        self.nxt = nxt
class Linkedlist:
    def __init__(self):
        self.head = None
    def insert_at_begining(self,d):
        newnode = Node(d, self.head)
        self.head = newnode
    def print(self):
        if self.head == None:
            print("it's empty")
            return
        curtun = self.head
        list_ = ''
        while curtun:
            list_ += str(curtun.data) + '-->'
            curtun = curtun.nxt
        print(list_)
    def insert_at_end(self,d):
        if self.head == None:
            self.head = Node(d,None)
            return
        newnode = Node(d,None)
        curtun = self.head
        while curtun.nxt:
            curtun = curtun.nxt
        curtun.nxt = newnode

    def insert_value(self,data_values):
        self.head = None
        for sata in data_values:
            self.insert_at_end(sata)
    def length(self):
        n = 0
        curtun = self.head
        while curtun:
            n+=1
            curtun = curtun.nxt
        return n
    def remove(self,index):
        if index<0 or index> self.length():
            print('its out of the length')
            return
        if index == 0:
            self.head = self.head.nxt
            return
        else:
            curtun = self.head
            x=0
            while curtun :
                x+=1
                curtun = curtun.nxt
                if x+1 == index:
                    curtun.nxt =curtun.nxt.nxt
                    break
    def insert_at(self,index,n):
        if index<0 or index> self.length():
            print('its out of the length')
            return
        if index == 0:
            self.insert_at_begining(n)
        elif index == self.length():
            self.insert_at_end(n)
        else:
            curtun =self.head
            l=0
            while curtun :
                if l+1 == index:
                    newnode = Node(n,curtun.nxt)
                    curtun.nxt = newnode
                    break
                curtun = curtun.nxt
                l += 1
    def insert_after_value(self,data_after,data_to_inset):
        curtun = self.head
        while curtun :
            if curtun.data == data_after:
                curtun.nxt=Node(data_to_inset,curtun.nxt)
                return
            curtun=curtun.nxt
        print("ur value dosen't exist")
    def remove_by_value(self,data):
        if self.head.data == data:
            self.head=self.head.nxt
            return
        curtun = self.head
        while curtun.nxt:
            if curtun.nxt.data == data:
                curtun.nxt = curtun.nxt.nxt
                return
            curtun = curtun.nxt

        print("ur value dosen't exist")




li = Linkedlist()
li.insert_at_end(10)
li.insert_value(['ziad','moh','fares'])
li.print()
print(li.length())
li.remove(0)
li.insert_at(1,'it_sme')
li.insert_at(0,'hello')
li.insert_at(4,'nope')
li.print()
li.insert_after_value('hello','mhe2')
li.remove_by_value('hello')
li.print()