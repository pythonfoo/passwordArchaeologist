import time


class Brute:
    def __init__(self):
        self.testChars = "abcdefghijklmnopqrstuvwxyz"
        self.printCount = 0
        self.pwLen = 0
        self.userPw = ''
        self.pwList = list()
        self.maxPwLen = 0

        self.start = 0
        self.stop = 0

    def setPassword(self, inputPw):
        self.userPw = inputPw
        self.pwList = list(inputPw)
        self.maxPwLen = len(self.pwList)

    def checkPwForLen(self, pwLen):
        generatedPw = [self.testChars[0]] * pwLen
        while generatedPw != [self.testChars[-1]] * pwLen:
            self.incrementPw(generatedPw)

            self.printCount += 1
            if self.printCount % 10000 == 0:
                print('TESTING:', generatedPw)

            if generatedPw == self.pwList:
                print('TESTING:', generatedPw)
                print('FOUND:', ''.join(generatedPw))
                return True
        return False

    def incrementPw(self, generatedPw):
        incr = 0
        while True:
            pos = self.testChars.find(generatedPw[incr])
            if pos == len(self.testChars)-1:
                generatedPw[incr] = self.testChars[0]
                incr += 1
                if incr > len(generatedPw)-1:
                    break
            else:
                generatedPw[incr] = self.testChars[pos + 1]
                break

    def processPassword(self):
        self.start = time.time()
        for i in range(self.maxPwLen):
            if self.checkPwForLen(i + 1):
                break
        self.stop = time.time()

    def getDuration(self):
        return self.stop - self.start


if __name__ == '__main__':
    force = Brute()
    # testChars = "0987654321"
    # testChars = "abcdefghijklmnopqrstuvwxyz0987654321"

    force.setPassword('test')
    force.processPassword()
    print('DURATION:', force.getDuration())
    print('CHECKED:', force.printCount)
