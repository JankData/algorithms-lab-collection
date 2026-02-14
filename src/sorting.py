# heapsort
def maxHeapify(a, n, i):
    comparisons = 0

    left = 2 * i + 1
    right = 2 * i + 2
    largest = i

    if left < n:
        comparisons += 1
        if a[left] > a[largest]:
            largest = left

    if right < n:
        comparisons += 1
        if a[right] > a[largest]:
            largest = right

    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        c = maxHeapify(a, n, largest)
        comparisons += c

    return comparisons

def buildMaxHeap(a):
    comparisons = 0
    n = len(a)

    for i in range(n // 2 - 1, -1, -1):
        comparisons += maxHeapify(a, n, i)

    return comparisons

def heapsort(a):
    comparisons = 0

    comparisons += buildMaxHeap(a)

    for n in range(len(a), 1, -1):
        a[0], a[n - 1] = a[n - 1], a[0]
        comparisons += maxHeapify(a, n - 1, 0)

    return comparisons

# insertionsort
def insertion_sort(a):
    comparisons = 0

    for i in range(1, len(a)):
        k = a[i]
        j = i - 1

        while j >= 0:
            comparisons += 1
            if a[j] > k:
                a[j + 1] = a[j]
                j -= 1
            else:
                break

        a[j + 1] = k

    return comparisons

# quicksort
def quicksort(list):
    comparisons = 0

    if len(list) <= 1:
        return comparisons

    pivot = list[-1]
    point = -1

    for i, element in enumerate(list[:-1]):
        comparisons += 1
        if element <= pivot:
            point += 1
            list[point], list[i] = list[i], list[point]

    list[point + 1], list[-1] = list[-1], list[point + 1]

    comparisons += quicksort(list[:point + 1])
    comparisons += quicksort(list[point + 2:])

    return comparisons

# bubblesort
def bubblesort(list):
    comparisons = 0
    for i in range(0, len(list) - 1):
        changes = False
        for j in range(0, len(list) - 1 - i):
            comparisons += 1
            if list[j] > list[j + 1]:
                changes = True
                list[j], list[j + 1] = list[j + 1], list[j]
        if not changes:
            return comparisons

    return comparisons