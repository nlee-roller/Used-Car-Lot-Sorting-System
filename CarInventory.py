from Car import Car
from CarInventoryNode import CarInventoryNode

class CarInventory:
    def __init__(self):
        self.root = None

    def _addCar(self, car, currentCar):
        carNode = CarInventoryNode(car)
        fixCar = Car(car.make, car.model, car.year, car.price)
        
        if carNode == currentCar:
            currentCar.cars.append(fixCar)
                
        elif carNode < currentCar:
            if currentCar.left is None:
                currentCar.left = carNode
                carNode.parent = currentCar
            else:
                self._addCar(car, currentCar.left)
                
        else:
            if currentCar.right is None:
                currentCar.right = carNode
                carNode.parent = currentCar
            else:
                self._addCar(car, currentCar.right)
                
    def addCar(self, car):
        if self.root:
            self._addCar(car, self.root)
        else:
            self.root = CarInventoryNode(car)

    def _doesCarExist(self, car, currCar):
        carNode = CarInventoryNode(car)
        if carNode == currCar:
            for item in currCar.cars:
                if car == item:
                    return True
            return False
        elif carNode < currCar:
            if currCar.getLeft():
                return self._doesCarExist(car, currCar.left)
            else:
                return False
        else:
            if currCar.getRight():
                return self._doesCarExist(car, currCar.right)
            else:
                return False

    def doesCarExist(self, car):
        if self.root:
            return self._doesCarExist(car, self.root)
        else:
            return False

    def inOrder(self):
        return self._inOrder(self.root)

    def _inOrder(self, carInventoryNode):
        returnStr = ""

        if carInventoryNode:
            returnStr += self._inOrder(carInventoryNode.getLeft())
            returnStr += str(carInventoryNode)
            returnStr += self._inOrder(carInventoryNode.getRight())

        return returnStr

    def preOrder(self):
        return self._preOrder(self.root)

    def _preOrder(self, carInventoryNode):
        returnStr = ""

        if carInventoryNode:
            returnStr += str(carInventoryNode)
            returnStr += self._preOrder(carInventoryNode.getLeft())
            returnStr += self._preOrder(carInventoryNode.getRight())

        return returnStr

    def postOrder(self):
        return self._postOrder(self.root)

    def _postOrder(self, carInventoryNode):
        returnStr = ""

        if carInventoryNode:
            returnStr += self._postOrder(carInventoryNode.getLeft())
            returnStr += self._postOrder(carInventoryNode.getRight())
            returnStr += str(carInventoryNode)

        return returnStr

    def _findCar(self, car, currentNode):
        if currentNode:
            if car == currentNode:
                return currentNode
            elif car > currentNode:
                return self._findCar(car, currentNode.right)
            else:
                return self._findCar(car, currentNode.left)
        else:
            return None
                
    def getBestCar(self, make, model):
        car = Car(make, model, None, None)
        carNode = CarInventoryNode(car)
        foundCarNode = self._findCar(carNode, self.root)
        
        #car does not exist
        if foundCarNode is None:
            return None
        #car does exist
        bestCar = foundCarNode.cars[-1]
        for vehicle in foundCarNode.cars:
            if vehicle > bestCar:
                bestCar = vehicle
        return bestCar
        

    def getWorstCar(self, make, model):
        car = Car(make, model, None, None)
        carNode = CarInventoryNode(car)
        foundCarNode = self._findCar(carNode, self.root)
        
        #car does not exist
        if foundCarNode is None:
            return None
        #car does exist
        worstCar = foundCarNode.cars[-1]
        for vehicle in foundCarNode.cars:
            if vehicle < worstCar:
                worstCar = vehicle
        return worstCar

    def _getTotalInventoryPrice(self, carNode):
        totalPrice = 0
        rightPrice = 0
        leftPrice = 0
        
        if carNode:
            for car in carNode.cars:
                totalPrice = totalPrice + car.price

            rightPrice = self._getTotalInventoryPrice(carNode.right)
            leftPrice = self._getTotalInventoryPrice(carNode.left)

        totalPrice = totalPrice + rightPrice + leftPrice
        return totalPrice

    def getTotalInventoryPrice(self):
        if self.root:
            return self._getTotalInventoryPrice(self.root)
        else:
            return 0

    def spliceOut(self, node):
        if not (node.getLeft() or node.getRight()):
            if node.getParent().getLeft() == node:
                node.parent.left = None
            else:
                node.parent.right = None
                
        elif node.getLeft() or node.getRight():
            if node.getRight():
                if node.getParent().getLeft() == node:
                    node.parent.left = node.right
                else:
                    node.parent.right = node.right
                node.right.parent = node.parent

    def remove(self, currentNode):
        # case 1: node to remove is leaf
        if not (currentNode.getLeft() or currentNode.getRight()):
            if not currentNode.parent:
                return False
            if currentNode == currentNode.getParent().getLeft():
                currentNode.parent.left = None
            else:
                currentNode.parent.right = None
                
        # case 3: node to remove has both children
        elif currentNode.getLeft() and currentNode.getRight():
            # Need to find the successor, remove successor, and replace
            # currentNode with successor's data / payload
            successor = self.getSuccessor(currentNode.make, currentNode.model)
            self.spliceOut(successor)
            currentNode.cars = successor.cars
            currentNode.model = successor.model
            currentNode.make = successor.make
                     
            
        # case 2: node to remove has one child
        else:
            # Node has leftChild
            if currentNode.getLeft():
                if currentNode.parent and currentNode.parent.left == currentNode:
                    currentNode.left.parent = currentNode.parent
                    currentNode.parent.left = currentNode.left
                elif currentNode.parent and currentNode.parent.right == currentNode:
                    currentNode.left.parent = currentNode.parent
                    currentNode.parent.right = currentNode.left
                else: # currentNode is the root
                    currentNode.replaceNodeData(currentNode.left.make,
                                                currentNode.left.model,
                                                currentNode.left.cars,
                                                currentNode.left.left,
                                                currentNode.left.right)
            # Node has rightChild
            else:
                if currentNode.parent and currentNode.parent.left == currentNode:
                    currentNode.right.parent = currentNode.parent
                    currentNode.parent.left = currentNode.right
                elif currentNode.parent and currentNode.parent.right == currentNode:
                    currentNode.right.parent = currentNode.parent
                    currentNode.parent.right = currentNode.right
                else:
                    currentNode.replaceNodeData(currentNode.right.make,
                                                currentNode.right.model,
                                                currentNode.right.cars,
                                                currentNode.right.left,
                                                currentNode.right.right)

    def removeCar(self, make, model, year, price):
        if self.root is None:
            return False
        temp_car = Car(make, model, year, price)
        tempNode = CarInventoryNode(temp_car)
        foundCar = self._findCar(tempNode, self.root)
        if foundCar:
            for idx in range(len(foundCar.cars)):
                if foundCar.cars[idx] == temp_car:
                    foundCar.cars.pop(idx)
                    break
            if len(foundCar.cars) == 0:
                if self.root:
                    if not(self.root.getLeft() or self.root.getRight()):
                        self.root = None
                        return True
                    self.remove(foundCar)
                    return True
            return True
        else:
            return False

    def getSuccessor(self, make, model):
        tempCar = Car(make, model, None, None)
        carNode = CarInventoryNode(tempCar)
        foundCar = self._findCar(carNode, self.root)
        if not foundCar:
            return None
        elif foundCar:
            if foundCar.getRight():
                foundCar = foundCar.right
                foundCar = foundCar.findMin()
                return foundCar
            if foundCar.getParent() is None:
                return None
            elif foundCar:
                while foundCar.getParent():
                    if foundCar.parent.left == foundCar:
                        return foundCar.parent
                    else:
                        foundCar = foundCar.parent
            return None
        return foundCar







    
        
