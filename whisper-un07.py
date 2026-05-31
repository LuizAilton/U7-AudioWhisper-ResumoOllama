# Pipeline de Transcrição e Resumo de Áudio com Whisper e Ollama

# Exibe o caminho do interpretador Python que está sendo usado
# Útil para verificar se o notebook está utilizando o ambiente virtual correto
import sys
print(sys.executable)

# Biblioteca de transcrição Whisper da OpenAI
#!pip install -U openai-whisper
import whisper

# Carrega o modelo Whisper
# Modelos possíveis: tiny, base, small, medium, large
model = whisper.load_model("large")

# Biblioteca para manipulação de arquivos
import os
mp3_path = 'ia-completa.mp3'

if not os.path.exists(mp3_path):
    print("Arquivo não encontrado!")
else:
    # Transcreve o áudio utilizando Whisper
    result = model.transcribe(mp3_path)

    # Obtém apenas o texto transcrito
    texto = result['text']

    # Exibe a transcrição completa
    print("Transcrição:")
    print(texto)

# Biblioteca para comunicação com o Ollama
#!pip install ollama
import ollama

# Prompt enviado ao modelo LLM
# O modelo receberá a transcrição e produzirá um resumo
prompt = f"""
Você é um assistente especializado em resumir textos.

Leia a transcrição abaixo e gere:
- Um resumo curto

Transcrição:
{texto}
"""

# Envia o prompt ao modelo executado pelo Ollama
response = ollama.chat(
    model='llama3.2:3b',
    messages=[
        {
            'role': 'user',
            'content': prompt
        }
    ]
)

# Extrai a resposta do modelo
resumo = response['message']['content']

# Exibe o resumo final
print(resumo)
