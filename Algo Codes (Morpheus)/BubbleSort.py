import random
import time

def bubble_sort(unsortedd_list):
    for i in range(len(unsortedd_list)):
        for j in range(0,len(unsortedd_list)-1-i):
            if unsortedd_list[j] > unsortedd_list [j+1]:
                # vertauschen von 2 Werten - ohne cache zu benutzen zu müssen
                unsortedd_list[j], unsortedd_list[j+1] = unsortedd_list[j+1], unsortedd_list[j]
    return unsortedd_list

if __name__ == "__main__":
    l = []
    for i in range(9999):
        l.append(random.randint(0,999))
    start = time.time()
    l = bubble_sort(l)
    print(l)
    end = time.time()
    for i in range(len(l)-1):
        assert l[i] <= l[i+1]
    print(end-start)
