from time import process_time
from matplotlib import pyplot as plt
from n import find_n
from kmp import find_kmp
from rk import find_rk


def calc_process_time(func, strings, text):
    start = process_time()
    for string in strings:
        func(string, text)
    stop = process_time()

    return (stop - start)


def calc_time(text, sp_text, sizes, funcs):
    time = {}
    for func in funcs:
        tmp = []
        for size in sizes:
            strings = sp_text[:size]
            tmp.append(calc_process_time(func,  strings, text))
        time.update({func.__name__: tmp})
    return time


def plot(sizes, time, file_name):
    plt.clf()
    for name, times in time.items():
        plt.plot(sizes, times, label=name)

    plt.yscale('linear')
    plt.xlabel('sample size')
    plt.ylabel('time [s]')
    plt.legend(loc="upper left")
    plt.grid(b=True, which='major', axis='both')

    plt.savefig(file_name)
    plt.show()


def main():
    with open('pan-tadeusz.txt', 'r', encoding='utf-8') as file_handle:
        text = file_handle.read()
    sp_text = text.split()

    sizes = [10, 20, 30, 50, 100]
    funcs = [find_kmp, find_n, find_rk]
    time = calc_time(text, sp_text, sizes, funcs)

    plot(sizes, time, 'wyszukiwanie')


if __name__ == '__main__':
    main()
