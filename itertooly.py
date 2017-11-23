from itertools import combinations_with_replacement
from string import ascii_lowercase
import time

userPw = input("Enter Password: ")
maxPwLen = len(userPw)
printCount = 0

start = time.time()
for max_len in range(1, maxPwLen + 1):
    for pw in combinations_with_replacement(ascii_lowercase, max_len):
        if printCount % 10000 == 0:
            print("".join(pw))
        printCount += 1
        if "".join(pw) == userPw:
            break
stop = time.time()

print('DURATION:', stop - start)
print('CHECKED:', printCount)
