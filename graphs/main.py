import sys
import argparse
from dijkstra import dijkstra


def main(arguments):
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name')
    args = parser.parse_args(arguments[1:])
    with open(args.file_name, 'r', encoding='utf-8') as file_handle:
        text = file_handle.read()
    text = text.split('\n')
    graph = []
    startEnd = []
    for i, line in enumerate(text):
        tmp = []
        for j, letter in enumerate(line):
            letter = int(letter)
            if letter == 0:
                startEnd.append((i, j))
            tmp.append(letter)
        graph.append(tmp)
    path = dijkstra(graph, startEnd[0], startEnd[1])

    for i, x in enumerate(graph):
        line = ''
        for j, y in enumerate(x):
            if (i, j) not in path:
                line += ' '
            else:
                line += f'{y}'
        print(line)


if __name__ == '__main__':
    main(sys.argv)
