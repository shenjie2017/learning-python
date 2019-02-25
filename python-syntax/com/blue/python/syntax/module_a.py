def sayHello(name):
    print('Hello ', name)


def sayBye(name):
    print('Bye ', name)


def sayGood(name):
    print('Good', name)


print('in module_a:', __name__)

if __name__ == "__main__":
    print("module run python")
    sayHello('Bob')
