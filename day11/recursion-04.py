'''
To print your name n times on screen using recursion
'''


def print_name(name, times):
    if times == 1:
        print(name)
        return
    else:
        print(name)
        return print_name(name, times-1)


print_name("Ajay", 10)
