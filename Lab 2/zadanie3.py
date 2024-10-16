# Zadanie 3
# Uruchom testy metody z pktu 2 z różnymi rozmiarami danych wejściowych oraz różną liczbą procesów, 
# następnie przedstaw zebrane wyniki w postaci graficznej z użyciem matplotlib.

import time
import random
from multiprocessing import Pool
import matplotlib.pyplot as plt

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(data):
    if len(data) <= 1:
        return data

    middle = len(data) // 2
    left = merge_sort(data[:middle])
    right = merge_sort(data[middle:])
    
    return merge(left, right)

def parallel_sort(data, num_processes):
    chunk_size = len(data) // num_processes

    chunks = [data[i * chunk_size: (i + 1) * chunk_size] for i in range(num_processes)]
    if len(data) % num_processes:
        chunks.append(data[num_processes * chunk_size:])

    with Pool(processes=num_processes) as pool:
        sorted_chunks = pool.map(merge_sort, [chunk for chunk in chunks if chunk])

    sorted_data = sorted_chunks[0]
    for chunk in sorted_chunks[1:]:
        sorted_data = merge(sorted_data, chunk)
    
    return sorted_data

def run_tests():
    data_sizes = [10**3, 10**4, 10**5, 10**6]   # Dane wejściowe
    process_counts = [1, 2, 4, 8]
    results = {}
    
    for size in data_sizes:
        print(f"Test dla rozmiaru danych: {size}")
        data = [random.randint(0, 10000) for _ in range(size)]
        results[size] = []

        for processes in process_counts:
            start_time = time.time()
            parallel_sort(data, processes)
            end_time = time.time()
            duration = end_time - start_time
            print(f"Procesy: {processes}, czas: {duration:.4f} s")
            results[size].append((processes, duration))
    
    return results

def plot_results(results):
    plt.figure(figsize=(10, 6))
    
    for size, timings in results.items():
        processes = [x[0] for x in timings]
        times = [x[1] for x in timings]
        plt.plot(processes, times, marker='o', label=f"Rozmiar danych: {size}")
    
    plt.title("Wydajność równoległego sortowania dla różnych rozmiarów danych")
    plt.xlabel("Liczba procesów")
    plt.ylabel("Czas sortowania (sekundy)")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    results = run_tests()
    plot_results(results)
