def sort(array: list[int]):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] < array[j + 1]: continue
            array[j], array[j + 1] = array[j + 1], array[j]

array = [ 10, 9, 3, 1, 2, 44 ]
print(array)
sort(array)
print(array)