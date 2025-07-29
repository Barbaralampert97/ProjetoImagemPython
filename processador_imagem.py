# processador_imagem.py

# Importa as bibliotecas necessárias
# Pillow (PIL) para manipulação de arquivos de imagem

from PIL import Image
import numpy as np

def transformar_imagem(caminho_imagem_entrada: str, caminho_saida_cinza: str, caminho_saida_binaria: str, limiar: int = 128):
    """
    Converte uma imagem colorida para níveis de cinza e para binarizado.

    Parâmetros:
        caminho_imagem_entrada (str): O caminho para a imagem a ser processada.
        caminho_saida_cinza (str): O caminho para salvar a imagem em tons de cinza.
        caminho_saida_binaria (str): O caminho para salvar a imagem binarizada.
        limiar (int, optional): O limiar para a binarização. O padrão é 128.
    """
    try:
        # --- Passo 1: Abrir a imagem e converter para um array NumPy ---
        print(f"Abrindo a imagem: {caminho_imagem_entrada}")
        imagem_colorida = Image.open(caminho_imagem_entrada)
        
        # Converte a imagem para um array NumPy para facilitar os cálculos.
        imagem_np = np.array(imagem_colorida)
        
        # --- Passo 2: Conversão para Níveis de Cinza ---
        print("Convertendo para níveis de cinza...")
        
        # Pega os canais R, G e B. 
        r = imagem_np[:, :, 0].astype(np.float64)
        g = imagem_np[:, :, 1].astype(np.float64)
        b = imagem_np[:, :, 2].astype(np.float64)
        
        # Aplica a fórmula de luminosidade (média ponderada)
        
        imagem_em_cinza_np = 0.299 * r + 0.587 * g + 0.114 * b
        
        # Converte o resultado de volta para o tipo de dados de imagem 
        imagem_em_cinza_np = imagem_em_cinza_np.astype(np.uint8)

        # Cria uma nova imagem PIL a partir do array NumPy
        imagem_cinza_pil = Image.fromarray(imagem_em_cinza_np)
        
        # Salva a imagem em tons de cinza
        imagem_cinza_pil.save(caminho_saida_cinza)
        print(f"Imagem em níveis de cinza salva em: {caminho_saida_cinza}")

        # --- Passo 3: Conversão para Binarizado (Preto e Branco) ---
        print(f"Binarizando a imagem com limiar = {limiar}...")
        
        # Usa a imagem em cinza já calculada como base.
        imagem_binarizada_np = np.where(imagem_em_cinza_np >= limiar, 255, 0)

        # Converte o resultado para o tipo de dados de imagem
        imagem_binarizada_np = imagem_binarizada_np.astype(np.uint8)

        # Cria uma nova imagem PIL a partir do array binarizado
        imagem_binaria_pil = Image.fromarray(imagem_binarizada_np)

        # Salva a imagem binarizada
        imagem_binaria_pil.save(caminho_saida_binaria)
        print(f"Imagem binarizada salva em: {caminho_saida_binaria}")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_imagem_entrada}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# --- Ponto de Entrada do Script ---
if __name__ == "__main__":
    # Nomes do arquivo de entrada
    ARQUIVO_ENTRADA = "imagem_colorida.jpg"  

    # Nomes dos arquivos de saída
    ARQUIVO_SAIDA_CINZA = "resultado_cinza.jpg"
    ARQUIVO_SAIDA_BINARIA = "resultado_binario.jpg"

    # Chama a função principal para executar a transformação
    transformar_imagem(ARQUIVO_ENTRADA, ARQUIVO_SAIDA_CINZA, ARQUIVO_SAIDA_BINARIA)