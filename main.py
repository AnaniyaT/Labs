import enum
#Question number one (Class array)
class array:
    def __init__(self,dt,l,initval=[]):
        self.dtype = dt
        self.size = l
        self.arr = [None]*l
        assert len(initval)<=l, "Too many initial values"
        for l,k in enumerate (initval):
            self.arr[l] = k
    def __shift(self,n):
        for i in range (n,self.size-1):
            self.arr[i] = self.arr[i+1]
        self.arr[-1] = None
    def __shiftr(self,n):
        for i in range (self.size-1,n,-1):
            self.arr[i] = self.arr[i-1]
        self.arr[n] = None
    def setval (self, val, i):
        assert isinstance (val, self.dtype), f"Wrong datatype"
        self.arr[i] = val
    def insert (self, val, i):
        assert isinstance (val, self.dtype), f"Wrong datatype"
        if self.arr[i] != None:
            self.__shiftr(i)
        self.arr[i] = val
    def remove(self, val):
        n=0
        for i,j in enumerate(self.arr):
            if j==val:
                self.arr[i] = None
                n = i
                self.__shift(n)
                break
    def iremove(self,i):
        self.arr[i] = None
        self.__shift(i)
    def showarray(self):
        return self.arr

# Question number two (array of five integers)
class intarray5(array):
    def __init__(self, initval):
        super().__init__(int, 5, initval)
    def printarr(self):
        print (self.arr)
    def get(self,i):
        return self.arr[i]
myarray = array (int, 6)
myarray.insert(6,0)
print (myarray.showarray())
myarray.insert(7,5)
print (myarray.showarray())
myarray.insert(9,3)
print (myarray.showarray())
myarray.insert(8,0)
print (myarray.showarray())
myarray.insert(1,0)
print (myarray.showarray())
myarray.insert(7,0)
print (myarray.showarray())
myarray.insert(3,0)
print (myarray.showarray())

