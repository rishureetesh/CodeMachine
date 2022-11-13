def bubble_sort(list_elements):
    for i in range(len(list_elements)-2, -1, -1):
        flag = True
        for j in range(0, i+1):
            if list_elements[j] > list_elements[j+1]:
                flag = False
                list_elements[j], list_elements[j+1] = list_elements[j+1],list_elements[j]
        if flag:
            break
    return list_elements

def insertion_sort(list_elements):
    if not list_elements or len(list_elements) == 1:
        return list_elements
    for i in range(2,len(list_elements)):
        min = list_elements[i]
        j = i
        while j > 0 and list_elements[j-1] > min:
            list_elements[j] = list_elements[j-1]
            j -= 1
        list_elements[j] = min
    return list_elements

def selection_sort(list_elements):
    if not list_elements or len(list_elements) == 1:
        return list_elements
    for i in range(len(list_elements)):
        min = i
        for j in range(i+1, len(list_elements)):
            if list_elements[j] < list_elements[min]:
                min = j
        list_elements[min], list_elements[i] = list_elements[i], list_elements[min]
    return list_elements

def merge_sort(list_elements):
    pass

def quick_sort(list_elements):
    pass

def heap_sort(list_elements):
    pass

