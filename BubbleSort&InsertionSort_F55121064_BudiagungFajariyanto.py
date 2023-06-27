import time

def bubble_sort(arr):
    n = len(arr)
    start_time = time.time()

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if i < 5 or i >= n - 6:
            print(f"Iterasi {i + 1}: {arr}")

    end_time = time.time()
    execution_time = end_time - start_time

    return arr, execution_time

def insertion_sort(arr):
    n = len(arr)
    start_time = time.time()

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

        if i < 6 or i >= n - 5:
            print(f"Iterasi {i}: {arr}")

    end_time = time.time()
    execution_time = end_time - start_time

    return arr, execution_time


def main():
    arr = [12, 99, 62, 15, 20, 95, 39, 48, 3, 24, 8, 43, 74, 19, 97, 33, 49, 68, 55, 33, 90, 90, 7, 26, 85, 46, 39, 40, 9,
           36, 60, 64, 89, 31, 25, 71, 21, 23, 63, 84, 32, 5, 3, 44, 21, 10, 21, 17, 50, 2, 36, 53, 79, 54, 19, 88, 1, 32,
           31, 15, 6, 3, 1, 40, 22, 43, 18, 1, 77, 9, 59, 40, 7, 41, 81]

    print("Sebelum pengurutan:")
    print(arr)

    while True:
        print("Pilihan Algoritma:")
        print("1. Bubble Sort")
        print("2. Insertion Sort")
        choice = input("\nPilih jenis pengurutan (1/2): ")
        if choice.lower() == "1":
            sorted_arr, execution_time = bubble_sort(arr.copy())
            break
        elif choice.lower() == "2":
            sorted_arr, execution_time = insertion_sort(arr.copy())
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

    print("\nSetelah pengurutan:")
    print(sorted_arr)

    print("\nWaktu komputasi pengurutan:", execution_time, "detik")


if __name__ == '__main__':
    main()