from math import log


class Heap:
    def __init__(self, k=2):
        self._k = k
        self._n = 0
        self._arr = []

    def insert(self, item):
        if isinstance(item, list):
            for i in item:
                self.insert(i)
        else:
            self._arr.append(item)
            self._n += 1
            self.heapify_up()

    def heapify_up(self):
        currentItem = len(self._arr) - 1
        while currentItem > 0:
            parent = (currentItem - 1) // self._k
            if self._arr[parent] > self._arr[currentItem]:
                self.swap(currentItem, parent)
                currentItem = parent
                continue
            break

    def remove_peak(self):
        self.swap(0, len(self._arr) - 1)
        self._arr.remove(self._arr[-1])
        self._n -= 1

        self.heapify_down()

    def heapify_down(self):
        currentItem = 0
        while 1:
            child = self._k * currentItem + 1
            if child > self._n - 1:
                break
            if self._arr[currentItem] > self._arr[child]:
                self.swap(currentItem, child)
                currentItem = child
                continue
            child += 1
            if child > self._n - 1:
                break
            if self._arr[currentItem] > self._arr[child]:
                self.swap(currentItem, child)
                currentItem = child
                continue
            break

    def swap(self, i1, i2):
        self._arr[i1], self._arr[i2] = self._arr[i2], self._arr[i1]

    def print(self):
        h = int(log(self._n, self._k) + 1)
        last_row_items_number = self._k ** (h-1)
        row_width = last_row_items_number * 8 + self._k ** (h-2)
        printed_elem = 0
        for i in range(h):
            tmp = self._k ** i + printed_elem
            line = ''

            for j, item in enumerate(self._arr[printed_elem:tmp]):
                width = row_width // self._k ** i
                if j % self._k == 0 and j != 0:
                    line += '|'
                line += f'{item:^{width}}'

            printed_elem = tmp
            print(f"{line}\n")
