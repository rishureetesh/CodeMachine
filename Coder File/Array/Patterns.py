NUM = 5
def pattern_one(num):
    for i in range(1, num+1):
        for j in range(1, num+1):
            print("*", end=" ")
        print("")

def pattern_two(num):
    for i in range(1, num+1):
        for j in range(1, i+1):
            print("*", end=" ")
        print("")

def pattern_three(num):
    for i in range(1, num+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print("")

def pattern_four(num):
    for i in range(1, num+1):
        for j in range(1, i+1):
            print(i, end=" ")
        print("")

def pattern_five(num):
    for i in range(num, 0, -1):
        for j in range(1,i+1):
            print("*", end=" ")
        print("")

def pattern_six(num):
    for i in range(num, 0, -1):
        for j in range(1,i+1):
            print(j, end=" ")
        print("")

def pattern_seven(num):
    for i in range(1, num+1):
        result = " " * (num - i) if (num - i) else ""
        for j in range(1, i+1):
            result += "*"
        for j in  range(j-1, 0, -1):
            result += "*"
        print(result)

def pattern_eight(num):
    for i in range(num, 0, -1):
        result = " " * (num - i) if (num - i) else ""
        for j in range(1, i+1):
            result += "*"
        for j in  range(j-1, 0, -1):
            result += "*"
        print(result)

def pattern_nine(num):
    for i in range(1, num+1):
        result = " " * (num - i) if (num - i) else ""
        for j in range(1, i+1):
            result += "*"
        for j in  range(j-1, 0, -1):
            result += "*"
        print(result)
    for i in range(num, 0, -1):
        result = " " * (num - i) if (num - i) else ""
        for j in range(1, i+1):
            result += "*"
        for j in  range(j-1, 0, -1):
            result += "*"
        print(result)

def pattern_ten(num):
    for i in range(1, num+1):
        result = ""
        for j in range(1, i+1):
            result += "*"
        print(result)
    for i in range(num-1, 0, -1):
        result = ""
        for j in range(1, i+1):
            result += "*"
        print(result)

pattern_ten(NUM)