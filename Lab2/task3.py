import multiprocessing

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def parallel_merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_part = arr[:mid]
    right_part = arr[mid:]

    print("Left half sent to process 1:", left_part)
    print("Right half sent to process 2:", right_part)

    with multiprocessing.Pool(processes=2) as pool:
        results = pool.map(merge_sort, [left_part, right_part])

    print("Process 1 sorted result:", results[0])
    print("Process 2 sorted result:", results[1])

    return merge(results[0], results[1])


if __name__ == "__main__":
    numbers = input("Enter numbers to sort, separated by spaces: ")
    arr = list(map(int, numbers.split()))

    print("\nOriginal array:", arr)

    sorted_arr = parallel_merge_sort(arr)

    print("\nFinal sorted array:", sorted_arr)