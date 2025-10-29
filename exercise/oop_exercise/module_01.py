class helloName:
    def __init__(self, n):
        self.name = n
    def getName(self):
        self.name = input("nhap ten cua ban: ")
    def printName(self):
        print(" --> Xin Chao : ", self.name.upper())

str = ''
someOne = helloName(str)    #tao. 1 object someOne tu` class 

someOne.getName()

someOne.printName()