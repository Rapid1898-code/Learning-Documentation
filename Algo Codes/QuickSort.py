import random
import time

def part(list, low, high):
    pivot = list[high]      # ganz rechte Element
    low_cache = low
    high_cache = high

    while low < high:
        while high > low_cache and list[high] >= pivot:
            high -= 1
        while low < high_cache and list[low] < pivot:
            low += 1
        if low < high:
            list[low], list[high] = list[high], list[low]   # Tausch von 2 Werten
        else:
            break

    if list[low] > pivot:
        list[high_cache], list[low] = list[low], list[high_cache]   # Tausch der beiden Elemente
    return low

def quick_sort(unsorted_list, low=0, high=None):
    if high is None:
        high = len(unsorted_list)-1

    if low < high:
        pivot = part(unsorted_list, low, high)
        quick_sort(unsorted_list, low, pivot-1)     # Sortierung der linken Seite
        quick_sort(unsorted_list, pivot+1, high)    # Sortierung der rechten Seite

if __name__ == "__main__":
    l = []
    for i in range(9999):
        l.append(random.randint(0,999))
    start = time.time()
    quick_sort(l)
    print(l)
    end = time.time()
    for i in range(len(l)-1):
        assert l[i] <= l[i+1]
    print(end-start)


