from com.blue.python.syntax.dog import Dog


class Golden(Dog):
    def __init__(self, name, age, sex="male"):
        Dog.__init__(self, name, age, sex)

    def sit(self):
        print("I am a golden dog, " + self.name + " is sit")

    def hello(self):
        print("I am a golden dog,my name is " + self.name + ".how are you?")

    def get_type(self):
        return self.name+" golden"
