from random import randint
import time

def make_random_list():
    arr = []
    for i in range(100):
        arr.append(randint(1, 100))
    return arr

def selection_sort():
    arr = make_random_list()

    print('-------- SELECTION SORT --------')
    print(f'Before : {arr}')

    start_time = time.time()
    for i in range(len(arr)):
        saver = i
        for j in range(i, len(arr)):
            if arr[saver] > arr[j]:
                saver = j
        arr[i], arr[saver] = arr[saver], arr[i]
    end_time = time.time()

    print(f'After : {arr}')
    print(f'time : {end_time - start_time}')
    print('--------------------------------')

def insertion_sort():
    arr = make_random_list()

    print('-------- INSERTION SORT --------')
    print(f'Before : {arr}')

    start_time = time.time()
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    end_time = time.time()

    print(f'After : {arr}')
    print(f'time : {end_time - start_time}')
    print('--------------------------------')

def bubble_sort():
    arr = make_random_list()

    print('-------- BUBBLE SORT --------')
    print(f'Before : {arr}')

    start_time = time.time()
    for i in range(len(arr) - 1):
        for j in range(1, len(arr)):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    end_time = time.time()

    print(f'After : {arr}')
    print(f'time : {end_time - start_time}')
    print('--------------------------------')

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = -1
    left_side, right_side = [], []

    for i in range(len(arr) - 1):
        if arr[i] <= arr[pivot]:
            left_side.append(arr[i])
        else:
            right_side.append(arr[i])

    return quick_sort(left_side) + [arr[pivot]] + quick_sort(right_side)

def count_sort(arr):
    counter = [0 for _ in range(max(arr) + 1)]
    for value in arr:
        counter[value] += 1

    for k in range(len(counter)):
        if counter[k] != 0:
            for j in range(counter[k]):
                print(k, end = ', ')