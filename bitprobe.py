#bitprobing

input("bit probe : (n >> j)   & 1 checks if bit J is on. press enter")
print(" 12 is binary = ", bin(12)[2:] ,"   bit 2:", (12 >> 2) & 1, "   bit 1:", (12 >> 1) & 1)
print("7's binary =", bin(7)[2:], " bit 2:", (7 >> 2) & 1, " bit 1:", (7 >> 1) & 1)

n = int(input("enter a number, try 6 or 5  :"))
print(" binary:",bin(n)[2:])

guess = input("guess what is bit 2 of" + str(n) + "? 0 or 1???")
input("BIT PROBE: n >> 2 & 1 gives the value of the bit. press enter.")
print(n,"bit 2=", (n >> 2) & 1," ur guess :", guess)
