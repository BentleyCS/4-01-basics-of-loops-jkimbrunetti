#All questions must use a loop for full points.
import random

def oddNumbers(n:int) ->str:
    odd = ""
    for i in range(1, n + 1, 1):
        if i < n:
            if i % 2 != 0:
                odd += str(i)
            elif i % 2 == 0:
                odd += " "
        if i == n and i % 2 == 1:
            odd += str(i)
    print(odd)
    return odd

def backwards(n)-> int:
    bw = ""
    for i in range(n, 0, -1):
        if i > 1:
            bw += str(i) + " "
        elif i == 1:
            bw += "1"
    print(bw)
    return bw

def randomRepeating():
    newNum = random.randint(1,10)
    tries = 0
    while newNum in range(1,9):
        tries +=1
        newNum = random.randint(1,10)
    return f"it took {tries} tries to get a 10"

def randomRange(n):
    list = []
    for i in range(0, n, 1):
        newNum = random.randint(1, 100)
        n+=1
        list.append(newNum)
    print(list)
    list.sort()
    low = list[0]
    high = list[len(list) - 1]
    print(f"Low = {low}, High = {high}")
    return low, high

def reverse(word:str)->str:
    reverseWord = ""
    for i in range(len(word) - 1, -1, -1):
        reverseWord += word[i]
    return reverseWord

def fizzBuzzContinuous(n):
    ans = ""
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            ans += "fizzbuzz"
        elif i % 3 == 0:
            ans += "fizz"
        elif i % 5 == 0:
            ans += "buzz"
        else:
            ans += str(i)
        if i != n:
            ans += " "
    return ans

def collatz(n):
    ans = ""
    while n != 1:
        ans += str(n) + " "
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
    ans += "1"
    print(ans)
    return ans


def fibonacci(n):
    if n <= 0:
        return ""
    elif n == 1:
        return "0"
    a = 0
    b = 1
    ans = "0 1"
    for i in range(2, n):
        c = a + b
        ans += " " + str(c)
        a = b
        b = c
    return ans

print(fibonacci(300))