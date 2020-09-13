# Daniel Lu
# 9/13/20

# This function starts a counter from 0 to 50.  All values divisible by 10 are added to a list and printed.

tens = []
counter = 0

while counter < 51:
    if counter % 10 == 0:
        tens.append(counter)
    counter +=1
    print(counter)
    
print(tens)