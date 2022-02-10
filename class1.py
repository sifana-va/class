from operator import itemgetter
from traceback import print_exception


class store:
    count=0
    def __init__ (self,item,price,expry):
        self.item=item
        self.price=price
        self.expry=expry
        store.count=store.count+1
    def myfunc(self):
        print(self.item,self.price,self.expry)
    def itemcount(self):
        print("total no of items=%d"%(store.count))
item1=store("brush",15,2022)
item1.myfunc()
item2=store("paste",45,2024)
item2.myfunc()
item2.itemcount()