import sys
import argparse
from time import process_time

from merge_sort import merge_sort_recursive, merge_sort_iterative
from selective_sort import selective_sort
from bubble_sort import bubble_sort
from quick_sort import quick_sort, quick_sort_mem_save

from matplotlib import pyplot as plt
sys.setrecursionlimit(5000)

# SIZES = [5000, 10000, 20000, 30000, 40000, 50000]
SIZES = [1000, 2000, 3000, 5000, 10000]
FUNCS = [quick_sort, quick_sort_mem_save, selective_sort, bubble_sort,
         merge_sort_recursive, merge_sort_iterative]


def get_samples(sizes, text):
    res = []
    for n in sizes:
        res.append(text[:n])
    return res


def calc_process_time(func, arr):
    arr = arr.copy()

    start = process_time()
    func(arr)
    stop = process_time()

    time = stop - start
    return time * 1000


def calc_time(samples, funcs):
    time = {}
    for func in funcs:
        tmp = []
        for arr in samples:
            tmp.append(calc_process_time(func, arr))
        time.update({func.__name__: tmp})
    return time


def plot(sizes, time):
    for name, times in time.items():
        plt.plot(sizes, times, label=name)

    plt.yscale('linear')
    plt.xlabel('sample size')
    plt.ylabel('time [ms]')
    plt.legend(loc="upper left")
    plt.grid(b=True, which='major', axis='both')

    plt.savefig('graph.png')
    plt.show()


def main(arguments):
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name', nargs='?', default='pan-tadeusz.txt', type=str)
    args = parser.parse_args(arguments[1:])
    with open(args.file_name, 'r', encoding='utf-8') as file_handle:
        text = file_handle.read()
    text = text.split(' ')

    samples = get_samples(SIZES, text)
    time = calc_time(samples, FUNCS)

    plot(SIZES, time)


if __name__ == '__main__':
    main(sys.argv)
