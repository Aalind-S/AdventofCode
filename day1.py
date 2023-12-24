
with open('day1input.txt', 'r') as file:
    list2 = file.read().splitlines()

currSum = 0
totalSum = 0

for inp1 in list2:
    l = 0
    r = len(inp1) - 1
    leftval = rightval = ""
    leftFlag = rightFlag = True
    while l < r:
        if inp1[l].isdigit() and leftFlag:
            #print("l")
            leftFlag = False
            leftval = inp1[l]
            #print(inp1[l])
        if inp1[r].isdigit() and rightFlag:
            #print("r")
            rightFlag = False
            rightval = inp1[r]
            #print(inp1[r])
        l += 1 
        r -= 1
    if leftval and rightval:
        currSum = int(leftval+rightval)
    else:
        currSum = 0
    totalSum += currSum

print(totalSum)