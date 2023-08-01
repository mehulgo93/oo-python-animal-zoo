from typing import Any
from lib.animal import Animal

class Zoo:

    all = []

    def __init__(self, name, location):
        self._name = name
        self._location = location
        self._animals = []
        Zoo.all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @property
    def location(self):
        return self._location
    
    def animals(self):
        return self._animals
    
    def add_animals(self, animal):
        return self._animals.append(animal)
    
    def animal_species(self):
        species_set = set()
        for animal in self._animals:
            species_set.add(animal)
        return list(species_set)
    
    def get_species(self, species):
        return [animal for animal in self._animals if animal.species == species]
    

    def get_location(cls, location):
        return [zoo for zoo in cls.all if zoo.location == location]

    

# Creating zoo instances
zoo1 = Zoo("Zoo A", "Location A")
zoo2 = Zoo("Zoo B", "Location B")

# Creating animals and adding them to zoos
animal1 = Animal("Dog", "Buddy")
animal2 = Animal("Cat", "Whiskers")
animal3 = Animal("Dog", "Max")
animal4 = Animal("Elephant")

zoo1.add_animal(animal1)
zoo1.add_animal(animal2)
zoo2.add_animal(animal3)
zoo2.add_animal(animal4)

# Accessing the attributes and methods
print("Zoo 1 Name:", zoo1.get_name())
print("Zoo 1 Location:", zoo1.get_location())
print("Zoo 1 Animals:", [animal.species for animal in zoo1.animals()])
print("Zoo 1 Animal Species:", zoo1.animal_species())
print("Zoo 1 Animals with species 'Dog':", [animal.species for animal in zoo1.find_by_species("Dog")])
print("Zoo 1 Animal Nicknames:", zoo1.animal_nicknames())

print("Zoo 2 Name:", zoo2.get_name())
print("Zoo 2 Location:", zoo2.get_location())
print("Zoo 2 Animals:", [animal.species for animal in zoo2.animals()])
print("Zoo 2 Animal Species:", zoo2.animal_species())
print("Zoo 2 Animals with species 'Dog':", [animal.species for animal in zoo2.find_by_species("Dog")])
print("Zoo 2 Animal Nicknames:", zoo2.animal_nicknames())

# Using the class method to find zoos by location
zoos_in_location_b = Zoo.find_by_location("Location B")
for zoo in zoos_in_location_b:
    print("Zoo Name:", zoo.get_name(), "| Zoo Location:", zoo.get_location())
