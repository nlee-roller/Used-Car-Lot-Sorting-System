from Car import Car

class CarInventoryNode:
    def __init__(self, car):
        self.cars = [car]
        self.make = car.make.upper()
        self.model = car.model.upper()
        self.parent = None
        self.left = None
        self.right = None

    def getMake(self):
        return self.make

    def getModel(self):
        return self.model

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent

    def getLeft(self):
        return self.left

    def setLeft(self, left):
        self.left = left

    def getRight(self):
        return self.right

    def setRight(self, right):
        self.right = right

    def __str__(self):
        returnStr = ""
        for car in self.cars:
            returnStr = returnStr + str(car) + "\n"
        return returnStr

    def __gt__(self, rhs):
        if self.make > rhs.make:
            return True
        elif self.make == rhs.make and self.model > rhs.model:
            return True
        else:
            return False

    def __lt__(self, rhs):
        if self.make < rhs.make:
            return True
        elif self.make == rhs.make and self.model < rhs.model:
            return True
        else:
            return False

    def __eq__(self, rhs):
        if rhs == None:
            return False
        elif self.make == rhs.make and self.model == rhs.model:
            return True
        else:
            return False

    def findMin(self):
        current = self
        while current.left:
            current = current.left
        return current

    def replaceNodeData(self, make, model, cars, lc, rc):
        if self.getRight():
            self.right.parent = self
        if self.getLeft():
            self.left.parent = self

        self.make = make.upper()
        self.model = model.upper()
        self.cars = cars
        self.left = lc
        self.right = rc
        





        
