def reverse_stack(array):
    if not array:
        return
    temp = array.pop()
    reverse_stack(array)
    reverse(array, temp)
    return array

def reverse(new_lst, val):
    if not new_lst:
        print(val)
        new_lst.append(val)
        return
    temp_val = new_lst.pop()
    reverse(new_lst, val)
    new_lst.append(temp_val)


lst = [1,2,3,4,5,6,7,8]
new_array = reverse_stack(lst)
print(new_array)