class House:
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floor):
        self.numberOfFloors = int(floor)
        print(floor)


H = House()
print(H.numberOfFloors)
H.setNewNumberOfFloors(5)
