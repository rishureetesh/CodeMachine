def OnceAppearingElement(lst):
    low = 0
    high = len(lst)-1
    while low <= high:
        mid = low+(high-low)//2
        previousElement = (mid+len(lst)-1) % len(lst)
        NextElement = (mid+1) % len(lst)
        if lst[mid] != lst[previousElement] and lst[mid] != lst[NextElement]:
            return lst[mid]
        elif (mid % 2 == 0 and lst[mid] == lst[NextElement]) or (mid % 2 != 0 and lst[mid] == lst[previousElement]):
            low = NextElement
        else:
            high = previousElement
    return -1

lst = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8]
data = OnceAppearingElement(lst)
if data == -1:
    print("Array contains Twice appearing elements")
else:
    print(f"Once appearing element is : {data}")