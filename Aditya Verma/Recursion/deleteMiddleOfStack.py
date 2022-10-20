def delete_middle_of_stack(array, mid):
    if len(array) == mid:
        array.pop()
        return
    temp = array.pop()
    delete_middle_of_stack(array, mid)
    array.append(temp)
    return array


lst = [1,2,3,4,5,6,7,8,9]
mid = (len(lst)//2)+1
new_array = delete_middle_of_stack(lst, mid)
print(new_array)