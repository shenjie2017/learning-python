class Dog(object):
    def __init__(self, name, age, sex="male"):
        self.name = name
        self.age = age
        self.sex = sex

    def sit(self):
        print("I am a dog," + self.name + " is sit")

    def hello(self):
        print("I am a dog,my name is " + self.name + ".how are you?")

    def get_type(self):
        return self.name + " dog"
