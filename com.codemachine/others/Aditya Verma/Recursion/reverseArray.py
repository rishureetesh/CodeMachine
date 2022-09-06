#Reverse Array and check if string is palindromic

def reverseArray(array, index, length):
    if index > length:
        return
    array[index], array[length] = array[length], array[index]
    reverseArray(array, index+1, length-1)
    return array

def checkPalindromicString(string, index, length):
    if index > length:
        return True
    if string[index] != string[length]:
        return False
    return checkPalindromicString(string, index+1, length-1)

array = [1,2,3,4,5,6]
string = "madam"
print(reverseArray(array, 0, len(array)-1))
print(checkPalindromicString(string, 0, len(string)-1))