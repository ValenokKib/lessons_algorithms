import heapq
from collections import Counter
from collections import namedtuple

class Node(namedtuple('Node', ['left', 'right'])):
    def walk(self, code, acc):

        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')

class Leaf(namedtuple('Leaf', ['char'])):
    def walk(self, code, acc):

        code[self.char] = acc or '0'

def huffman_encode(s):
    h = []
    for i, j in Counter(s).items():
        h.append((j, len(h), Leaf(i)))
    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:
        j_1, _count1, left = heapq.heappop(h)
        j_2, _count2, right = heapq.heappop(h)

        heapq.heappush(h, (j_1 + j_2, count, Node(left, right)))
        count += 1
    code = {}
    if h:
        [(_j, _count, root)] = h
        root.walk(code, '')
    return code

def main():
    s = input('Введи строки для кодировки: ')
    code = huffman_encode(s)
    encode = " ".join(code[i] for i in s)
    print(encode)

print(main()) #привет, это кодировка  алгоритмом хаффманама
#00000 1010 1011 11011 00001 1100 00010 010 00011 1100 011 010 11110 011 00100 1011 1010 011 11011 11110 100 010 010 100 00101 00110 011 1010 1011 1100 1110 011 1110 010 00111 100 11111 11111 1110 100 11010 100 1110 100
print(main()) #этот алгоритм реализован
#11110 010 011 010 1011 100 1100 11111 011 1101 1110 010 0000 1011 1101 0001 100 1100 1110 0010 011 0011 100 1010
print(main()) #один один ноль один ноль  ноль
#110 010 011 111 00 110 010 011 111 00 111 110 100 101 00 110 010 011 111 00 111 110 100 101 00 00 111 110 100 101