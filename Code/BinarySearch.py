def binary_search(sorted_list, item):
    first = 0

    last = len (sorted_list) - 1
    found = False
    i = -1
    while (found != True and first <= last):
        mid = (first + last) // 2
        if sorted_list[mid] == item:
            found = True
            return mid
        else:
            if item > sorted_list[mid]:
                first = mid + 1
            else:
                last = mid - 1
    return found

if __name__ == "__main__":
    l = [1, 2, 4, 8, 9, 42, 1337, 1338, 5600, 13370]
    print (binary_search (l, 42))
