def factorial(number):
    answer = 1
    for x in range(1,number+1):
        answer = x * answer
    return answer

def fizzbuzz(seriesMax):
    for x in range(1,seriesMax):
        if x%3 == 0:
            divisibleby3 = True
        else:
            divisibleby3 = False
        if x%5 == 0:
            divisibleby5 = True
        else:
            divisibleby5 = False
        if divisibleby3 and divisibleby5:
            print("fizzbuzz")
        elif divisibleby3:
            print("fizz")
        elif divisibleby5:
            print("buzz")
        else:
            print(x)

def fibbonacci(seriesMax):
    a = 0
    b = 1
    print(a)
    print(b)
    for x in range(2,seriesMax):
        c = b
        b = b + a
        a = c
        print(b)
#         print("X:{0} B:{1}".format(x,b))

def sparkle(jia,seriesmax):
    for x in range(1,seriesmax):
        if x%jia == 0 or findx(jia,x):
            print("sparkle")
        else:
            print(x)

def findx(findWhat,findIn):
    strFindIn = str(findIn)
    lengthOfStrFindIn = len(strFindIn)
#     print(strFindIn)
    for i in range(0,lengthOfStrFindIn):
#       print("Position{0}:{1}".format(i,strFindIn[i])) 
    if strFindIn[i] == str(findWhat):
#       print("From the if loop...")
    return True
#       print("I got here...")
    return False
   #    if you get here, that means, the entire for loop executed, and you did not find a match