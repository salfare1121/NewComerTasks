# Quick sort 100 random numbers between 0 and 100
# Print all steps

import random

def bubble_sort(dl):
    change = True
    index_counter = 0
    temp_number = 0
    while change == True:
        change = False
        index_counter = 0
        while index_counter+1 < len(dl):
            if dl[index_counter] < dl[index_counter+1]:
                temp_number = dl[index_counter]
                dl[index_counter] = dl[index_counter+1]
                dl[index_counter+1] = temp_number
                change = True
            index_counter += 1
            print(dl)

    print('Sorted')
    print(dl)
    return dl

if __name__ == "__main__":
    random_list = [0]*100
    i = 0
    while i < len(random_list):
        random_list[i] = random.randint(0,100)
        i += 1
    print(random_list)
    bubble_sort(random_list)