# Compressão usando o algoritmo de Huffman
# Lógica: gera árvore de Huffman, substitui caracteres por códigos binários e salva árvore + dados compactados

import heapq
import pickle
from collections import Counter

class Node:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(freq):
    heap = [Node(char=c, freq=f) for c, f in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(freq=left.freq + right.freq, left=left, right=right)
        heapq.heappush(heap, merged)

    return heap[0]

def build_codes(node, prefix='', code_map={}):
    if node is None:
        return

    if node.char is not None:
        code_map[node.char] = prefix
    build_codes(node.left, prefix + '0', code_map)
    build_codes(node.right, prefix + '1', code_map)

    return code_map

input_file = 'arquivo2.txt'
output_file = 'arquivo2_compress.txt'

with open(input_file, 'r') as f:
    data = f.read()

# Calcula frequência de caracteres
freq = Counter(data)

# Constrói árvore e códigos
huffman_tree = build_huffman_tree(freq)
code_map = build_codes(huffman_tree)

# Codifica o texto
encoded_data = ''.join(code_map[char] for char in data)

# Preenche até múltiplo de 8 bits (com 0's no final)
extra_padding = 8 - len(encoded_data) % 8
encoded_data += '0' * extra_padding

# Armazena o padding no começo
padded_info = "{0:08b}".format(extra_padding)

encoded_data = padded_info + encoded_data

# Converte a string de bits para bytes
b = bytearray()
for i in range(0, len(encoded_data), 8):
    byte = encoded_data[i:i+8]
    b.append(int(byte, 2))

# Salva árvore + dados compactados (usando pickle para serializar a árvore)
with open(output_file, 'wb') as f:
    pickle.dump(huffman_tree, f)
    f.write(b)

print(f"Arquivo compactado como {output_file}")
