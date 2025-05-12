# Descompressão usando o algoritmo de Huffman
# Lógica: carrega árvore de Huffman, decodifica bits de volta para caracteres

import pickle

input_file = 'arquivo2_compress.txt'
output_file = 'arquivo2_uncompressed.txt'

class Node:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

with open(input_file, 'rb') as f:
    huffman_tree = pickle.load(f)  # Recupera a árvore
    compressed_data = f.read()

# Converte bytes para string de bits
bit_string = ''
for byte in compressed_data:
    bits = bin(byte)[2:].rjust(8, '0')
    bit_string += bits

# Recupera padding
padding = int(bit_string[:8], 2)
bit_string = bit_string[8:]  # remove padding info
bit_string = bit_string[:-padding]  # remove padding extra

# Decodifica usando a árvore
decompressed = ''
node = huffman_tree
for bit in bit_string:
    if bit == '0':
        node = node.left
    else:
        node = node.right

    if node.char is not None:
        decompressed += node.char
        node = huffman_tree

with open(output_file, 'w') as f:
    f.write(decompressed)

print(f"Arquivo descompactado como {output_file}")
