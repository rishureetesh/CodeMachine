#Balanced Parenthesis:
def balancedParenthesis(open, close, output):
    if open == 0 and close == 0:
        print(output)
        return
    
    if open:
        outputOne = output + "("
        balancedParenthesis(open-1, close, outputOne)
    if close > open:
        outputOne = output + ")"
        balancedParenthesis(open, close-1, outputOne)
    return


#Binary 1&0
def binaryOnesZero(one, zero, num, output):
    if num == 0:
        print(output)
        return
    
    outputOne = output + "1"
    binaryOnesZero(one + 1, zero, num -1, outputOne)
    
    if one > zero:
        outputOne = output + "0"
        binaryOnesZero(one, zero+1, num-1, outputOne)
    return


#Joshephus problem
def joshephusProblem(numList, killing, index):
    if len(numList) == 1:
        print(numList)
        return
    
    index = (index + killing) % len(numList)
    del numList[index]
    
    joshephusProblem(numList, killing, index)

sum = [index for index in range(1,41)]
joshephusProblem(sum, 6, 0)