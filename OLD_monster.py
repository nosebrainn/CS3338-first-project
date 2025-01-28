##Monster Class
class Monster:
    def __init__(self, monName, monSize):   #initialize an attribute name
        self.name = monName
        self.size = monSize

    def attack(self, location):             #Attack Method
        return(self.name + " attacks " + str(location))

    def __str__(self):                      #Monster Description
        return ("Monster is " + self.name + " with size of " + str(self.size))

    def __eq__(self, other):                       #Equal in size and name
        return ((self.name == other.name) & (self.size == other.size))

    def __add__(self, other):               #Name is the names of the two
        return (self.name + other.name)

#Creating instances Dougie and Pluto
Godzilla = Monster("Godzilla", 20)
GodzillaEQ = Monster("Godzilla", 20)
Kong = Monster("Kong", 15)


#Accessing fields of an instance
print(Godzilla)                     #str test
print(Godzilla.attack("Tokyo\n"))   #attack() test
print(Kong)                         #other monster
print(Kong==Godzilla)               #Equal test
print(str(GodzillaEQ==Godzilla))    #Equal test 2
print("\n")
print(Godzilla+Kong)                #add test



