#power sets .py
# # power set,binary masking and a subset selector
# 
input("a set wiuth n elements has 2^n subsets. press enter")
print(" 3 eleemtns 2^3 =", 2**3,"subsets")
print("     mask 5 = binary", bin(5)[2:], "select positions 0 and 2")

n = int(input("en ter a numnber of elemeents, try 4 or 5:"))
guess = input("how many subsets does a set of " + str(n)  +  " elements have?")
input("each eleement is in or out -  2 choices per element. press enter")
print(" ", n,"elements subsets:",  2**n, " ur guess:", guess)