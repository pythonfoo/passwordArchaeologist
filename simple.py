import time

testChars = "abcdefghijklmnopqrstuvwxyz"
#testChars = "0987654321"
#testChars = "abcdefghijklmnopqrstuvwxyz0987654321"

def checkPwForLen(pwLen):
    global printCount

    generatedPw = [testChars[0]] * pwLen
    while generatedPw != [testChars[-1]] * pwLen:
        incrementPw(generatedPw)

        printCount += 1
        if printCount % 10000 == 0:
            print('TESTING:', generatedPw)

        if generatedPw == pwList:
            print('TESTING:', generatedPw)
            print('FOUND:', ''.join(generatedPw))
            return True
    return False


def incrementPw(generatedPw):
    incr = 0
    while True:
        pos = testChars.find(generatedPw[incr])
        if pos == len(testChars)-1:
            generatedPw[incr] = testChars[0]
            incr += 1
            if incr > len(generatedPw)-1:
                break
        else:
            generatedPw[incr] = testChars[pos + 1]
            break

userPw = input("Enter Password: ")
pwList = list(userPw)
maxPwLen = len(pwList)
printCount = 0

start = time.time()
for i in range(maxPwLen):
    if checkPwForLen(i + 1):
        break
stop = time.time()

print('DURATION:', stop - start)
print('CHECKED:', printCount)
