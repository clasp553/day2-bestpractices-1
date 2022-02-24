class Fish:
    def __init__(self):
        self.members = ["Salmon", "Cod", "Nassel"]
        
    def printMembers(self):
        print("Printing dangeroush members of the Fish class")
        for member in self.members:
            print("\t%s " % member)