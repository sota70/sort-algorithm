def sort(array: list[int]):
    for i in range(1, len(array)):
        chosen = array[i]
        empty_idx = i
        while empty_idx > 0 and chosen < array[empty_idx - 1]:
            array[empty_idx] = array[empty_idx - 1]
            empty_idx = empty_idx - 1
        array[empty_idx] = chosen

array = [ 10, 9, 3, 1, 2, 44 ]
print(array)
sort(array)
print(array)