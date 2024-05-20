import re
from typing import List
from numpy import argmax


class NumberNotFound(Exception):
    pass


# task 1
def special_number(raw_line: str) -> str:
    number_match = re.search(r"[0-9]{2,4}\\[0-9]{2,5}", raw_line)
    if number_match is None:
        raise NumberNotFound()
    numbers = number_match.group(0).split('\\')
    numbers[0] = '0' * (4 - len(numbers[0])) + numbers[0]
    numbers[1] = '0' * (5 - len(numbers[1])) + numbers[1]
    return "\\".join(numbers)


# task 2
def distance_reducer(n: int, k: int, distances: List, mmd):
    for d in range(k):
        mdi = argmax(distances)
        reduced = distances[mdi]
        d = 2
        while reduced > mmd:
            reduced = distances[mdi] // d
            d += 1
        distances = distances[:mdi] + [reduced] * (d - 1) + distances[mdi + 1:]
    return distances


def is_possible(D, arr, n, k):
    used = 0
    for i in range(n):
        used += int(arr[i] / D)
    return used <= k


def min_max_dist(stations, n, k):
    low = 0
    high = max(stations)
    while high - low > 1e-6:
        mid = (low + high) / 2.0
        if is_possible(mid, stations, n, k):
            high = mid
        else:
            low = mid
    return round(low, 2)


# task 3
def largest_number(numbers: List[str]) -> str:
    sortedd = sorted(numbers, key=lambda x: len(x), reverse=True)
    max_len = len(sortedd[0])
    numbers.sort(key=lambda x: int(x + '0' * (max_len - len(x))), reverse=True)
    largest = ''

    numbers.sort(key=lambda x: x[0], reverse=True)
    for i in range(0, len(numbers) - 1):
        try:
            if numbers[i][0] == numbers[i + 1][0] and numbers[i][1] < numbers[i + 1][0]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
        except IndexError:
            pass
    largest = ''.join(numbers)

    return largest


if __name__ == "__main__":
    # task 1
    print(special_number(r'Адрес 5467\456. Номер '))

    # task 2
    mmds = min_max_dist([100, 180, 50, 45, 150], 5, 4)
    print(distance_reducer(5, 4, [100, 180, 50, 45, 150], mmds))

    # task 3
    print(largest_number(['11', '234', '005', '87', '8']))
    arr = [100, 180, 50, 45, 150]
    k = 4
    n = len(arr)

