def sort_stack(array):
    if not array:
        return
    temp = array.pop()
    sort_stack(array)
    sort(array, temp)
    return array

def sort(array, temp):
    if not array or array[len(array)-1] <= temp:
        array.append(temp)
        return
    val = array.pop()
    sort(array, temp)
    array.append(val)


lst = [9,8,7,6,5,4,3,2,1]
new_array = sort_stack(lst)
print(new_array)