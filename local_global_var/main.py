message = 'Hello, World!'

def greet(name):
    message = 'Hello, {name}!'

    def include_name():
        nonlocal message
        message = message.format(name=name)

    include_name()
    return message

def main():
    global message

    message = message.format(name='Farhan')
    print(message)
    print(greet('Farhan'))



if __name__ == '__main__':
    main()

# NameError: name 'msg' is not defined