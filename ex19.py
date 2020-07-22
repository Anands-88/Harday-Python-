def Chocolates_and_Gifts(number_of_chocolates,number_of_gifts):
    print(f"You have {number_of_chocolates} chocolates")
    print(f"You have {number_of_gifts} gifts")
    print("That's enough for a party!")
    print("Let's Party.\n")

print("We can just give the function numbers directly:")
Chocolates_and_Gifts(5,20)

print("Or we can use variables from our script :")
amount_of_chocolates = 10
amount_of_gifts = 30

Chocolates_and_Gifts (amount_of_chocolates, amount_of_gifts)

print("We can even do math inside too:")
Chocolates_and_Gifts (12 + 18, 33 + 44) 

print("And we can combine the two, variables and math:")
Chocolates_and_Gifts (amount_of_chocolates+ 74, amount_of_gifts * 5)

def party(*items):
    chocolates, gifts,cakes = items
    print(f"There are {cakes} cakes, {chocolates} chocolates and {gifts} gifts ")

party(10,30,2)