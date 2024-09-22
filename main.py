class Dog:
    def sound(self):
        return 'woo!!'
    
class Cat:
    def sound(self):
        return 'meew..'

def sound(animal):
    return(animal.sound())

dog = Dog()
cat = Cat()

print(sound(dog))