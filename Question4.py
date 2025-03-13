# Define the Dog class with a make_sound() method
class Dog:
    def make_sound(self):
        return "Woof!"

# Define the Cat class with a make_sound() method
class Cat:
    def make_sound(self):
        return "Meow!"

# Define the process_sound() function that expects an object with a make_sound() method
def process_sound(sound_object):
    # Check if the object has a make_sound() method
    if hasattr(sound_object, 'make_sound') and callable(sound_object.make_sound):
        # Call the make_sound() method and print the result
        print(sound_object.make_sound())
    else:
        print("Error: Object does not have a make_sound() method")

# Create Dog and Cat objects
dog = Dog()
cat = Cat()

# Pass the objects to the process_sound() function
process_sound(dog)  # Output: Woof!
process_sound(cat)  # Output: Meow!

# Attempt to pass an object without a make_sound() method
process_sound("Hello")  # Output: Error: Object does not have a make_sound() method
