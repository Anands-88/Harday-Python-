formatter = "{} {} {} {}"

print(formatter.format(1,2,3,4))
print(formatter.format('one','two','three','four'))
print(formatter.format(True,False,True,False))
print(formatter.format(formatter,formatter,formatter,formatter))
print(formatter.format(
    'Return a formated version of S', 
    'using substitutions from',
     'args and kwargs',
    'The substitutions are identified by braces'
))

print('{}'.format('thank You'))