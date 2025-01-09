class Animal:
    def speak(self):
        return "The animal makes a sound."

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def call_animal_sound(animal_type):
    # Create an instance of the chosen animal type
    animal_class = {
        "dog": Dog,
        "cat": Cat
    }.get(animal_type, Animal)

    # Create an instance of the selected animal
    animal_instance = animal_class()

    # Dynamically call the speak method using getattr
    sound = getattr(animal_instance, 'speak')()
    return sound

if __name__ == "__main__":
    animal_types = ["dog", "cat", "unknown"]
    
    for animal in animal_types:
        sound = call_animal_sound(animal)
        print(f"{animal.capitalize()} says: {sound}")