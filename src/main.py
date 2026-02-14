from random import random
import csv
import pandas as pd
import matplotlib.pyplot as plt

from sorting import (
    quicksort,
    heapsort,
    insertion_sort,
    bubblesort
)

wyniki = []
lengths = [10 * i for i in range(1, 101)]

for n in lengths:
    x = [random() for _ in range(n)]

    lpq = quicksort(x.copy())
    lph = heapsort(x.copy())
    lpi = insertion_sort(x.copy())
    lpb = bubblesort(x.copy())

    wyniki.append([n, lpq, lph, lpi, lpb])

csv_file = "porownania.csv"

with open(csv_file, "w", newline="") as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerow(["Length", "Quick", "Heap", "Insertion", "Bubble"])
    writer.writerows(wyniki)

df = pd.read_csv(csv_file, delimiter=";")

plt.figure()
plt.plot(df["Length"], df["Bubble"], label="Bubble")
plt.plot(df["Length"], df["Insertion"], label="Insertion")
plt.xlabel("Długość listy")
plt.ylabel("Liczba porównań")
plt.title("Bubble-Sort vs Insertion-Sort")
plt.legend()
plt.tight_layout()
plt.savefig("bubble_vs_insertion.png")
plt.close()

plt.figure()
plt.plot(df["Length"], df["Insertion"], label="Insertion")
plt.plot(df["Length"], df["Heap"], label="Heap")
plt.xlabel("Długość listy")
plt.ylabel("Liczba porównań")
plt.title("Insertion-Sort vs Heap-Sort")
plt.legend()
plt.tight_layout()
plt.savefig("insertion_vs_heap.png")
plt.close()

plt.figure()
plt.plot(df["Length"], df["Heap"], label="Heap")
plt.plot(df["Length"], df["Quick"], label="Quick")
plt.xlabel("Długość listy")
plt.ylabel("Liczba porównań")
plt.title("Heap-Sort vs Quick-Sort")
plt.legend()
plt.tight_layout()
plt.savefig("heap_vs_quick.png")
plt.close()

plt.figure()
plt.plot(df["Length"], df["Quick"], label="Quick")
plt.plot(df["Length"], df["Heap"], label="Heap")
plt.plot(df["Length"], df["Insertion"], label="Insertion")
plt.plot(df["Length"], df["Bubble"], label="Bubble")
plt.xlabel("Długość listy")
plt.ylabel("Liczba porównań")
plt.title("Porównanie wszystkich algorytmów")
plt.legend()
plt.tight_layout()
plt.savefig("all_algorithms.png")
plt.close()