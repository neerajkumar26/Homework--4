
# Name: - Neeraj Kumar
# ID: - 2047559
def selection_sort_descend_trace(val):
    for i in range(len(val)):
        max = i
        for j in range(i + 1, len(val)):
            if val[j] > val[max]:
                max = j
        val[i], val[max] = val[max], val[i]
        if len(val) - 1>i:
            for item in val:
                print(f"{item} ", end="")
            print()
    return val


if __name__ == '__main__':
    _input = map(int, input().split(" "))
    _input = list(_input)
    selection_sort_descend_trace(_input)
