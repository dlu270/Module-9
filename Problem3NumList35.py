# Daniel Lu
# 9/13/20

# This function continues prompting the user for a number until the sum of their numbers is greater than 100.

L = []

while sum(L) < 101:
    x = int(input("Please enter a number: "))
    L.append(x)
    print(L, sum(L))
print("The sum of your numbers has exceeded 100.")