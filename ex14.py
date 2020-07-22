from sys import argv

scrpt, user_name = argv
prompt ='>>>> '

print(f"Hi {user_name}, I'm the {scrpt} scrip")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("what kind of computer do you have?")
computer = input(prompt)

print(f""" Ok 
Alright, so u said {likes} about liking me. 
You live in {lives}. Not sure  where that is .
And you have a {computer} computer. Nice . """)