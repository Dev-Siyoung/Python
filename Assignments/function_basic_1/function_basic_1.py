#1 Prediction: 5 (correct)
#2 Prediction: 10 (correct)
#3 Prediction: 5 (correct)
#4 Prediction: 5 (correct)
#5 Prediction: 5 (half-correct: it will print out 5 and none - Assigning result of a function call, where the function has no return)
#6 Prediction: 8 (wrong: print out 3,5  TypeError: unsupported operand type for+: 'NoneType' and 'NonType')
#7 Prediction: 25 (correct)
#8 Prediction: 100,10 (correct)
#9 Prediction: 7,14,21 (correct)
#10 Prediction: 8 (correct)
#11 Prediction: 500,500,300,500 (correct)
#12 Prediction: 500,500,300,500 (correct)
#13 Prediction: 500,500,300,300 (correct)
#14 Prediction: 1,3,2 (correct)
#15 Prediction: 1,3,5,10 (correct)

def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)
