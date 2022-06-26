from time import process_time
from heap import Heap

from random import randint
from matplotlib import pyplot as plt


def get_sample(size):
    res = []
    for _ in range(size):
        res.append(randint(1, size*10))
    return res


def calc_insert(sample, sizes):
    time = {}
    for i in range(2, 5):
        tmp = []
        for size in sizes:
            h = Heap(i)
            arg = sample[:size]

            start = process_time()
            h.insert(arg)
            stop = process_time()
            tmp.append(1000 * (stop - start))

        time.update({f'{i}-heap': tmp})
    return time


def calc_remove_peak(sample, sizes):
    time = {}
    for i in range(2, 5):
        tmp = []
        for size in sizes:
            h = Heap(i)
            h.insert(sample)

            start = process_time()
            for _ in range(size):
                h.remove_peak()
            stop = process_time()
            tmp.append(1000 * (stop - start))

        time.update({f'{i}-heap': tmp})
    return time


def save_plot(time, sizes, file_name):
    plt.clf()
    for name, times in time.items():
        plt.plot(sizes, times, label=name)

    plt.yscale('linear')
    plt.xlabel('sample size')
    plt.ylabel('time [ms]')
    plt.legend(loc="upper left")
    plt.grid(b=True, which='major', axis='both')
    plt.title(file_name)
    plt.savefig(f'{file_name}.png')


def main():
    sample = get_sample(100000)
    sizes = list(range(10**3, 10**4 + 1, 10**3))
    time_insert = calc_insert(sample, sizes)
    save_plot(time_insert, sizes, 'insertion')

    time_remove_peak = calc_remove_peak(sample, sizes)
    save_plot(time_remove_peak, sizes, 'remove_peak')


if __name__ == '__main__':
    main()
