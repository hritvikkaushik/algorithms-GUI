import heapq
from collections import defaultdict


def encode(frequency):
    heap = [[weight, [symbol, '']] for symbol, weight in frequency.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        for pair in left[1:]:
            pair[1] = '0' + pair[1]
        for pair in right[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [left[0] + right[0]] + left[1:] + right[1:])
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))


data = "" 
frequency = defaultdict(int)
huff = 0
encodedString =""

def getEncoding():
    global frequency
    frequency = defaultdict(int)
    global data
    global huff
    global encodedString
    encodedString = ""
    huff = 0
    for symbol in data:
        frequency[symbol] += 1
    huff = encode(frequency)

    for symbol in data:
        for p in huff:
            if (p[0] == symbol):
                encodedString += str(p[1])