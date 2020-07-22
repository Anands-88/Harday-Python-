# first def function. one parameter two arguments.
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2 : {arg2}")

#second def function. 2 parameters 2 arguments.
def print_two_again(arg1, arg2):
    print(f"arg1 : {arg1}, arg2: {arg2}")

# third def function. 1 parameter and 1 argument.
def print_one(arg1):
    print(f"arg1: {arg1}")

# fourth def function. No arguments.
def print_none():
    print("I got nothing")

print_two("one","Two")
print_two_again("one","two")
print_one("first")
print_none()