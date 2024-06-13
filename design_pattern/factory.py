class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class AnimalFactory:
    @staticmethod
    def get_animal(animal_type):
        if animal_type == 'dog':
            return Dog()
        elif animal_type == 'cat':
            return Cat()
        else:
            raise ValueError("Unknown animal type")

# Usage
animal_factory = AnimalFactory()

dog = animal_factory.get_animal('dog')
print(dog.speak())  # Output: Woof!

cat = animal_factory.get_animal('cat')
print(cat.speak())  # Output: Meow!
