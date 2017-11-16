import sys
import time

testChars = "abcdefghijklmnopqrstuvwxyz"
#testChars = "0987654321"
#testChars = "abcdefghijklmnopqrstuvwxyz0987654321"

def checkPwForLen(pwLen):
    global printCount

    finalPw = [testChars[0]] * pwLen
    while finalPw != [testChars[-1]] * pwLen:
        incrementPw(finalPw)

        printCount += 1
        if printCount % 10000 == 0:
            #pass
            print('TESTING:', finalPw)

        if finalPw == pwList:
            print('TESTING:', finalPw)
            print('FOUND:', ''.join(finalPw))
            return True

    return False
def incrementPw(pw=[]):
    incr = 0
    while True:
        pos = testChars.find(pw[incr])
        if pos == len(testChars)-1:
            pw[incr] = testChars[0]
            incr += 1
            if incr > len(pw)-1:
                break
        else:
            pw[incr] = testChars[pos + 1]
            break

pw = input("Enter Password: ")
pwList = list(pw)
maxPwLen = len(pwList)
printCount = 0

start = time.time()
for i in range(maxPwLen):
   if checkPwForLen(i + 1):
       break

stop = time.time()

print('DURATION:', stop - start)
print('CHECKED:', printCount)
