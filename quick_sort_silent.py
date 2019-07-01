import random
from itertools import chain

def quick_sort(dl):

    if len(dl) == 1: # One Number
        return dl

    all_same = True # All same numbers
    for i in range(len(dl)):
        if dl[0] != dl[i]:
            all_same = False
            break
    if all_same == True:
        return dl

    else:
        head_index_number = 0
        tail_index_number = len(dl)-1
        check_number = dl[0]
        temporary_number = 0
        change = False

        while head_index_number < tail_index_number:

            while head_index_number < tail_index_number:
                if dl[head_index_number] >= check_number:
                    temporary_number = dl[head_index_number]
                    break
                else:
                    head_index_number += 1

            while head_index_number < tail_index_number:
                if dl[tail_index_number] < check_number:
                    dl[head_index_number] = dl[tail_index_number]
                    dl[tail_index_number] = temporary_number
                    change = True
                    break
                else:
                    tail_index_number -= 1

        c = 0
        if change == False:
            c = 1
        dl1 = dl[:head_index_number+c]
        dl2 = dl[head_index_number+c:]
        result = [quick_sort(dl1),quick_sort(dl2)]

        return flatten_by_extend(result)

# https://www.lifewithpython.com/2014/01/python-flatten-nested-lists.html
def flatten_by_extend(nested_list):
    flat_list = []
    for e in nested_list:
        flat_list.extend(e)
    return flat_list


if __name__ == "__main__":
    random_list = [0]*10000
    i = 0
    while i < len(random_list):
        random_list[i] = random.randint(0,10000)
        i += 1

    print(random_list)
    print("Sorting...")
    print(quick_sort(random_list))