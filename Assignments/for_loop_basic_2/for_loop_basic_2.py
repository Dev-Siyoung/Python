#1. Biggie Size

def biggieSize(list):
    for x in range(0,len(list),1):
        if list[x] > 0:
            list[x] = "big"
    return list

print(biggieSize([-1,3,5,-5]))

#2. Count Positives

def countPositives(list):
    counter = 0
    for x in range(0,len(list),1):
        if list[x] > 0:
            counter += 1
    list[len(list)-1] = counter
    return list
    
print(countPositives([-1,1,1,1]))
print(countPositives([1,6,-4,-2,-7,-2]))

#3. Sum Total

def sumTotal(list):
    sum = 0
    for x in range(0,len(list),1):
        sum += list[x]
    return sum

print(sumTotal([1,2,3,4]))
print(sumTotal([6,3,-2]))

#4. Average

def average(list):
    sum = 0
    for x in range(0,len(list),1):
        sum += list[x]
    avg = sum / len(list)
    return avg

print(average([1,2,3,4]))

#5. Length

def length(list):
    counter = 0
    for x in range(0,len(list),1):
        counter = x + 1
    return counter

print(length([37,2,1,-9]))
print(length([]))

#6. Minimum

def minimum(list):
    if len(list) == 0:
        return False
    min = list[0]
    for x in range(0,len(list),1):
        if list[x] < min:
            min = list[x]
    return min

print(minimum([37,2,1,-9]))
print(minimum([]))

#7. Maximum

def maximum(list):
    if len(list) == 0:
        return False
    max = list[0]
    for x in range(0,len(list),1):
       if list[x] > max:
            max = list[x]
    return max

print(maximum([37,2,1,-9]))
print(maximum([]))

#8. Ultimate Analysis

def ultAnalysis(list):
    
    sum = 0
    avg = 0
    min = list[0]
    max = list[0]
    length = 0
    for x in range(0,len(list),1):
        sum += list[x]
        avg = sum / len(list)
        length += 1
        if list[x] <= min:
            min = list[x]
        if list[x] > max:
            max = list[x]
    ultDictionary = {"sumTotal": sum , "average": avg, "minimum": min, "maximum": max, "length": length}
    return ultDictionary

print(ultAnalysis([37,2,1,-9]))

#9. Reverse List

def reverseList(list):
    for x in range(0, int(len(list)/2), 1):
        temp = list[x]
        list[x] = list[len(list)-1 -x]
        list[len(list)-1-x] = temp
    return list    

        
print(reverseList([37,2,1,-9]))
