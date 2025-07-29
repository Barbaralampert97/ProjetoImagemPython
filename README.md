# 🖼️ Processador de Imagem em Python

Um script simples em Python para converter imagens coloridas para tons de cinza e para o formato binarizado (preto e branco), implementando os algoritmos de conversão manualmente com a ajuda da biblioteca NumPy.

## 📖 Sobre o Projeto

Este projeto foi criado como um exercício prático para entender a manipulação de imagens a nível de pixel. Em vez de usar funções de conversão direta de bibliotecas como OpenCV (`cv2.cvtColor`) ou Pillow (`.convert()`), os algoritmos de conversão para escala de cinza (método de luminosidade) e binarização (usando um limiar) foram implementados do zero.

---

## ✨ Funcionalidades

- **Conversão para Tons de Cinza**: Transforma uma imagem RGB em uma imagem de 8 bits em escala de cinza, usando a fórmula de média ponderada para uma percepção de brilho mais precisa.
- **Binarização de Imagem**: Converte a imagem em tons de cinza para uma imagem puramente preta e branca, com base em um valor de limiar (threshold) configurável.
- **Manipulação Manual de Pixels**: Todo o processamento é feito através da manipulação de arrays NumPy, o que torna o processo transparente e educativo.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Pillow (PIL Fork)**: Para abrir, manipular e salvar os arquivos de imagem.
- **NumPy**: Para realizar os cálculos matemáticos em matrizes de pixels de forma eficiente.

---

## 🚀 Como Usar

Siga os passos abaixo para executar o projeto localmente.

### Pré-requisitos

- Python 3 instalado
- Git instalado

### Instalação e Execução

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/Barbaralampert97/ProjetoImagemPython.git](https://github.com/Barbaralampert97/ProjetoImagemPython.git)
   ```

2. **Navegue até a pasta do projeto:**
   ```bash
   cd projeto-processador-de-imagem
   ```

3. **Instale as dependências:**
   ```bash
   pip install Pillow numpy
   ```

4. **Adicione sua imagem:**
   Coloque a imagem colorida que você deseja processar na raiz da pasta e renomeie-a para `imagem_colorida.jpg`.

5. **Execute o script:**
   ```bash
   python processador_imagem.py
   ```

6. **Verifique os resultados:**
   Após a execução, duas novas imagens serão criadas na pasta:
   - `resultado_cinza.jpg`
   - `resultado_binario.jpg`

---








