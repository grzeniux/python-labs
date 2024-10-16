import multiprocessing
from multiprocessing import Pool

def merge(left, right):
    """
    Funkcja łącząca dwie posortowane listy w jedną posortowaną listę.
    """
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
    
    print(f"Merging: {left} and {right} -> {result}")
    return result

def merge_sort(data):
    """
    Standardowy algorytm Merge Sort, który będzie używany przez poszczególne procesy.
    """
    if len(data) <= 1:
        return data

    middle = len(data) // 2
    left = merge_sort(data[:middle])
    right = merge_sort(data[middle:])
    
    return merge(left, right)

def parallel_sort(data):
    """
    Funkcja inicjująca równoległe sortowanie dla danych wejściowych.
    """
    num_processes = min(multiprocessing.cpu_count(), len(data))  # Ustalenie liczby procesów, ale nie więcej niż liczba elementów
    chunk_size = len(data) // num_processes

    # Podzielenie danych na części dla poszczególnych procesów
    chunks = [data[i * chunk_size: (i + 1) * chunk_size] for i in range(num_processes)]
    if len(data) % num_processes:
        chunks.append(data[num_processes * chunk_size:])

    print(f"Chunks przed sortowaniem: {chunks[:2]}")

    # Tworzenie puli procesów i sortowanie poszczególnych części równolegle
    with Pool(processes=num_processes) as pool:
        sorted_chunks = pool.map(merge_sort, [chunk for chunk in chunks if chunk])

    print(f"Posortowane fragmenty: {sorted_chunks[:2]}") 

    # Scalenie posortowanych fragmentów
    sorted_data = sorted_chunks[0]
    for chunk in sorted_chunks[1:]:
        sorted_data = merge(sorted_data, chunk)
    
    return sorted_data

if __name__ == '__main__':
    import random

    data = [random.randint(0, 100) for _ in range(10)]
    print(f"Losowe dane: {data[:10]}")  
    
    sorted_data = parallel_sort(data)
    print(f"Posortowane dane: {sorted_data[:10]}")
