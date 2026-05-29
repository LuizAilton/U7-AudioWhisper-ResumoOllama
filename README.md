# Pipeline de Transcrição e Resumo de Áudio com Whisper e Ollama

## Descrição do Projeto

Este projeto implementa um pipeline de Inteligência Artificial capaz de:

1. Receber um arquivo de áudio (`.mp3` ou `.wav`)
2. Realizar a transcrição automática utilizando o modelo Whisper
3. Enviar o texto transcrito para o Ollama
4. Gerar um resumo do conteúdo

O objetivo é demonstrar a integração entre modelos de reconhecimento de fala e modelos de linguagem executados localmente.

---

## Tecnologias Utilizadas

* Python 3
* Whisper
* Ollama
* Modelo LLM `llama3.2:3b`

---

## Instalação do Ambiente

### 1. Clonar o repositório

```bash
git clone https://github.com/LuizAilton/U7-AudioWhisper-ResumoOllama.git
cd U7-AudioWhisper-ResumoOllama
```

---

### 2. Criar ambiente virtual

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Instalar dependências Python

```bash
pip install openai-whisper
pip install ollama
```

---

## Instalação do Ollama

Baixe e instale o Ollama:

https://ollama.com

Após a instalação, execute o download do modelo utilizado:

```bash
ollama pull llama3.2:3b
```

Verifique se o Ollama está funcionando:

```bash
ollama list
```

---

## Execução do Projeto

1. Coloque o arquivo de áudio (`.mp3` ou `.wav`) na pasta do projeto.

2. Atualize o nome do arquivo no código:

```python
mp3_path = 'ia-completa.mp3'
```

3. Execute o notebook ou script Python.

---

## Exemplo de Uso

### Entrada

Arquivo de áudio contendo uma aula, reunião ou palestra.

### Saída Esperada

#### Transcrição

```text
A inteligência artificial está transformando diversas áreas...
```

#### Resumo Gerado

```text
Resumo:
O áudio aborda conceitos de inteligência artificial e suas aplicações.
```

---

## Código Principal

```python
import whisper
import ollama
import os

model = whisper.load_model("base")

mp3_path = 'ia-completa.mp3'

if not os.path.exists(mp3_path):
    print("Arquivo não encontrado!")

else:
    result = model.transcribe(mp3_path)

    texto = result['text']

    prompt = f"""
    Resuma o texto abaixo e extraia os principais pontos-chave.

    Texto:
    {texto}
    """

    response = ollama.chat(
        model='llama3.2:3b',
        messages=[
            {
                'role': 'user',
                'content': prompt
            }
        ]
    )

    print(response['message']['content'])
```

---

## Modelos Recomendados para CPU

Para execução em notebooks e computadores sem GPU dedicada:

| Modelo      | Desempenho     |
| ----------- | -------------- |
| llama3.2:3b | Bom equilíbrio |
| phi3:mini   | Muito leve     |
| gemma2:2b   | Leve e rápido  |

---

## Observações

* O modelo `large` do Whisper pode ser muito pesado para CPU.
* Recomenda-se utilizar:

  * `base`
  * `small`

Exemplo:

```python
model = whisper.load_model("base")
```

---

## Autor

Projeto desenvolvido para fins acadêmicos e experimentação com IA local utilizando Whisper e Ollama.
