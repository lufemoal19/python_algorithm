"""

"""

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    left = [item for item in array[1:] if item < pivot]
    right = [item for item in array[1:] if item >= pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

def main():
    unsorted_list = [9, 10, 54, 31, 0, 23, -5, -4, -10, 14, 2, 7, 90, 0, 2, 6, 67, 9]
    print(f'Sorted list: {quick_sort(unsorted_list)}')

if __name__ == '__main__':
    main()