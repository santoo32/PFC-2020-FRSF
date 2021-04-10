class ImageDetected:
    def __init__(self, image, classDetected, calculatedSma):
        self.image = image
        self.classDetected = classDetected
        self.calculatedSma = calculatedSma

    def myfunc(self):
        print("Hello my name is " + self.classDetected)

# p1 = Person("John", 36)
# p1.myfunc()