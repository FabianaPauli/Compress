# Algoritmo de descompressão RLE otimizado (binário)
# Lógica: lemos letra (1 byte) + quantidade (2 bytes)

import struct

input_file = 'arquivo1_compress.txt'
output_file = 'arquivo1_uncompress.txt'

with open(input_file, 'rb') as f:
    compressed = f.read()

decompressed = ""
i = 0
while i < len(compressed):
    char = compressed[i:i+1].decode('utf-8')
    count = struct.unpack('>H', compressed[i+1:i+3])[0]
    decompressed += char * count
    i += 3

with open(output_file, 'w') as f:
    f.write(decompressed)

print(f"Arquivo descompactado como {output_file}")
