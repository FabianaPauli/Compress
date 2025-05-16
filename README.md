# 🔐 Compactação de Arquivos com Algoritmos Customizados e Huffman

Este projeto demonstra a criação de dois algoritmos de **compressão e descompressão de arquivos de texto**, aplicando estratégias personalizadas e o algoritmo clássico de **Huffman**, com validação de integridade usando **hash MD5**.

---

## 📁 Arquivos

- `arquivo1.txt` → Contém letras repetidas (ex: `aaaaaabbbbbbcccccc`)
- `arquivo2.txt` → Contém letras sortidas (ex: `jhdfweukfnvlxzq...`)

---

## 🧠 Lógica dos Algoritmos

### ✅ Para `arquivo1.txt` (com dados repetidos):
Utilizamos um **algoritmo de compressão por dicionário (substituição de padrões)** criado do zero, com base na repetição de blocos.

#### Compressão (`compress_1.py`)
- Analisa o texto e substitui blocos repetidos por "tokens" curtos.
- Exemplo: `"aaaaaa"` → `"@A"` (onde `@A` é um token do dicionário).
- Salva o dicionário + texto compactado.

#### Descompressão (`uncompress_1.py`)
- Lê o dicionário e reconstrói o texto original substituindo os tokens.

---

### ✅ Para `arquivo2.txt` (com dados sortidos):
Foi aplicado o **algoritmo de Huffman**, que cria uma árvore binária baseada na **frequência dos caracteres**.

#### Compressão (`compress_2.py`)
- Conta a frequência de cada caractere.
- Cria uma **árvore de Huffman** (caracteres mais frequentes ganham códigos binários menores).
- Codifica o texto em uma sequência compactada de bits.
- Serializa e salva a árvore + dados compactados.

#### Descompressão (`uncompress_2.py`)
- Lê a árvore Huffman salva no arquivo.
- Percorre os bits para reconstruir os caracteres.
- Recupera o texto original com precisão bit a bit.

---

## 🧪 Validação com MD5

O script `validate_md5.py` compara os arquivos originais com os descompactados para garantir que o processo de compressão/descompressão foi **sem perdas**.

### Exemplo de uso:
```bash
python validate_md5.py
