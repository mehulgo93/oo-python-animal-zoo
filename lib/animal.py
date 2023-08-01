class Animal:
    all_animals = []  # Class variable to store all animal instances

    def __init__(self, species, nickname, weight, zoo):
        self.species = species
        self._nickname = nickname
        self._weight = weight
        self.zoo = zoo
        Animal.all_animals.append(self)  # Add the current instance to the list of all animals

    @property
    def nickname(self):
        return self._nickname

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, new_weight):
        self._weight = new_weight

    def get_species(self):
        return self.species

    def get_zoo(self):
        return self.zoo

    @classmethod
    def all(cls):
        return cls.all_animals

    @classmethod
    def find_by_species(cls, species):
        return [animal for animal in cls.all_animals if animal.species == species]
