import random
def insertion_sort(unsorted_list):
    sorted_list = []
    while (len(unsorted_list)>0):
        smallest = unsorted_list[0]
        smallest_index = 0
        for index, element in enumerate (unsorted_list):
            if element < smallest:
                smallest = element
                smallest_index = index
        unsorted_list.pop(smallest_index)
        sorted_list.append(smallest)
    return sorted_list

if __name__ == "__main__":
    l = []
    for i in range(9999):
        l.append(random.randint(0,999))
    print(insertion_sort(l))
