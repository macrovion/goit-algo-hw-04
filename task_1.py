import random
import timeit
import sys

# збільшєння ліміту рекурсії для Merge Sort на великих масивах
sys.setrecursionlimit(20000)

# 1. реалізація сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# 2. реалізація сортування злиттям
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    sorted_arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr

# 3. проводимо обгортку для Timsort
def timsort_wrapper(arr):
    return sorted(arr)

# запуску тесту
def run_benchmark(algorithm, data, iterations=1):
  
    t = timeit.timeit(lambda: algorithm(data.copy()), number=iterations)
    return t / iterations

# тест
list_size = 2000  # ромір списку
iterations = 10   # кількість прогонів

# генерація даних
data_random = [random.randint(0, 10000) for _ in range(list_size)]
data_sorted = sorted(data_random)
data_reverse = sorted(data_random, reverse=True)

print(f"--- Порівняння на {list_size} елементах (середнє за {iterations} ітерацій) ---\n")

scenarios = {
    "Випадковий": data_random,
    "Відсортований": data_sorted,
    "Зворотний": data_reverse
}

for scenario_name, data in scenarios.items():
    print(f"[{scenario_name} набір даних]")
    
    t_insert = run_benchmark(insertion_sort, data, iterations)
    print(f"Insertion Sort: {t_insert:.6f} сек")
    
    t_merge = run_benchmark(merge_sort, data, iterations)
    print(f"Merge Sort:     {t_merge:.6f} сек")
    
    t_timsort = run_benchmark(timsort_wrapper, data, iterations)
    print(f"Timsort:        {t_timsort:.6f} сек")
    
    print("-" * 30)


    """
        
    Аналіз результатів

Insertion Sort
Випадкові дані: Можна сказати, що дуже повільно. Імовірно буде його непридатним для великих масивів.
Відсортовані дані: Миттєво. Це "найкращий випадок", алгоритм просто проходить по списку один раз.

Merge Sort
Всі сценарії: Показує стабільний час.

Timsort
Випадкові дані: Швидше за Merge Sort.
Відсортовані дані: Дуже швидко.
     
    """
