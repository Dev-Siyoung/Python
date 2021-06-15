#1. Countdown

def countDown(num):
    countDownList = []
    for x in range(num,-1,-1):
        countDownList.append(x)
    return countDownList

print(countDown(5))    

#2. Print and Return

def printAndReturn(num1,num2):
    num = [num1,num2]
    print(num[0])
    return num[1]

print(printAndReturn(1,2))

#3. First Plus Length

def firstPlusLength(list):
    return list[0] + len(list)

print(firstPlusLength([1,2,3,4,5]))

#4. Values Greater than Second

def valueGreaterThanSecond(list):
    newList = []
    for x in range(0,len(list),2):
        if len(list) < 2:
            return False
        elif list[x] > list[x+1]:
            newList.append(list[x])
        elif list[x] < list[x+1]:
            newList.append(list[x+1])    
    return newList
print(valueGreaterThanSecond([5,2,3,2,1,4]))
print(valueGreaterThanSecond([3]))

#5. This Length, That Value

def thisLenThatvalue(num1,num2):
    newList = []
    count = 0
    while count < num1:
        newList.append(num2)
        count +=1
    return newList

print(thisLenThatvalue(4,7))
print(thisLenThatvalue(6,2))    
        