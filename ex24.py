print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intution
and requires an explanation
\n\t\twhere there is more.
"""
print("---------*---------")
print(poem)
print("---------*---------")

five = 10 - 3 + 5 - 7
print(f"This should be five: {five}\n")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates # to call the variable, out of the function.

start_points = 10000
beans, jars, crates = secret_formula(start_points)

# remember that this is another way to format a string
print("with a starting point of: {}".format(start_points))

# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_points = start_points / 10

print("We can also do that this way: ")
formula = secret_formula(start_points) # secreat..... means "27"
#this is an easy way to apply a list  to a format string 
print("we'd have {} beans, {} jars, and {} crates.".format(*formula)) # * all included 