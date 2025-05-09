# Contador de Dedos com MediaPipe e OpenCV

Este projeto usa a biblioteca MediaPipe junto com OpenCV para detectar mãos pela webcam e contar quantos dedos estão levantados.

## Pré-requisitos

- Python 3.8+
- pip

## Instalação

1. Clone o repositório:
   ```
   git clone https://github.com/seu-usuario/meu_projeto_maos.git
   cd meu_projeto_maos
   ```

2. Crie e ative um ambiente virtual:
   ```
   python -m venv venv
   venv\Scripts\activate  # ou source venv/bin/activate
   ```

3. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

## Execução

```bash
python main.py
```

## Estrutura do Projeto

- `main.py`: script principal de execução.
- `utils/hand_utils.py`: funções auxiliares como contagem de dedos.
- `requirements.txt`: dependências do projeto.
