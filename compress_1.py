# Algoritmo de compressão RLE otimizado com armazenamento binário
# Lógica: letra (1 byte) + quantidade (2 bytes binários)

import struct

input_file = 'arquivo1.txt'
output_file = 'arquivo1_compress.txt'

with open(input_file, 'r') as f:
    data = f.read()

with open(output_file, 'wb') as f:
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i - 1] and count < 65535:
            count += 1
        else:
            f.write(data[i - 1].encode('utf-8'))  # 1 byte
            f.write(struct.pack('>H', count))    # 2 bytes (unsigned short big endian)
            count = 1
    # Escreve o último grupo
    f.write(data[-1].encode('utf-8'))
    f.write(struct.pack('>H', count))

print(f"Arquivo compactado como {output_file}")
