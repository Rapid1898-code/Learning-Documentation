import random
import time

def merge (list, l, m, r):
    divider =  m+1
    l_cache = l
    out_list = []
    for i in range(r-l+1):
        if l > m:
            out_list.append(list[divider])
            divider += 1
        elif  divider > r:
            out_list.append(list[l])
            l += 1
        elif list[l] < list[divider]:
            out_list.append(list[l])
            l = l+1
        elif list[l] >= list[divider]:
            out_list.append(list[divider])
            divider = divider + 1
    for i in range(len(out_list)):
        list[i+l_cache] = out_list[i]

def merge_sort(unsorted_list, l=0, r=None):
    if r is  None:
        r =  len(unsorted_list) - 1

    if l < r:
        m = (l+r-1) // 2
        merge_sort(unsorted_list, l, m)
        merge_sort(unsorted_list, m+1, r)
        merge(unsorted_list, l, m, r)

if __name__ == "__main__":
    l = []
    for i in range(9999):
        l.append(random.randint(0,999))
    start = time.time()
    merge_sort(l)
    print(l)
    end = time.time()
    for i in  range(len(l)-1):
        assert l[i] <= l[i+1]
    print(end-start)
