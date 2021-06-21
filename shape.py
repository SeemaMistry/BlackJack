class Shape:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def getLength(self):
        return self.length

    def getWidth(self):
        return self.width

    def setLength(self, length):
        self.length = length

    def setWidth(self, width):
        self.width = width

    def printArea(self):
        print(self.length*self.width)

    def print(self):
        print("bye")

class Cube(Shape):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def printVolume(self):



