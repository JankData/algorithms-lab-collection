def minHeapify(a, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and a[left] < a[smallest]:
        smallest = left
    if right < n and a[right] < a[smallest]:
        smallest = right

    if smallest != i:
        a[i], a[smallest] = a[smallest], a[i]
        minHeapify(a, n, smallest)


def buildMinHeap(a):
    n = len(a)
    for i in range(n // 2 - 1, -1, -1):
        minHeapify(a, n, i)

def multi_merge(a):
    heap = [x[:] for x in a if len(x) > 0]

    buildMinHeap(heap)

    b = []

    while len(heap)>0:
        smallest_list = heap[0]

        b.append(smallest_list.pop(0))

        if len(smallest_list) == 0:
            heap[0] = heap[-1]
            heap.pop()
        if len(heap)>0:
            minHeapify(heap, len(heap), 0)

    return b

from random import randint

for i in range(1, 5):
    a = []
    for _ in range(randint(3, 10)):
        x = [randint(0, 99) for _ in range(randint(1, 5))]
        x.sort()
        a.append(x)
    print('In ' + str(i) + ':', a)
    b = multi_merge(a)
    print('Out ' + str(i) + ':', b)
    print()

a = []
for k in [1, 1, 2, 2, 3]:
    x = [randint(0, 10) for _ in range(k)]
    x.sort()
    a.append(x)