class Pet():
    def __init__(self, animal):
        self.name = animal

class Person():
    def __init__(self, name, age, height, hair_colour, favourite_colour):
        self.name = name
        self.brain = 'very very smart'
        self.age = age
        self.height = height
        self.hair_colour = hair_colour
        self.favourite_colour = favourite_colour
        self.pets = []

    def hello(self):
        return f"Hello, my name is {self.name}, how are you?"

class House():
    def __init__(self, number_of_bathrooms, number_of_bedrooms):
        self.number_of_bathrooms = number_of_bathrooms
        self.number_of_bedrooms = number_of_bedrooms
        self.color = 'yellow'
        self.year_built = 2023
        self.people = []
    
    def add_people(self, person):
        self.people.append(person)

class Street():
    def __init__(self):
        self.houses = []


person1 = Person('Donald', 42, 163, 'brown', 'blue')
person2 = Person('Hannah', 18, 155, 'blonde', 'blue')

# print(person1)
# print(person2)
# print(person1.__dict__)
# print(person2.__dict__)

house1 = House(2, 3)
# print(house1)
# print(house1.__dict__)

house1.add_people(person1.__dict__)
house1.add_people(person2.__dict__)
print(house1.people[0].hello())
print(house1.people[1].hello())

print(house1.__dict__)


# what's the diffence between a class and instance (of a class) ? answered
# can we answer what does the keyword 'Any' refer to?
# The Creator design pattern
