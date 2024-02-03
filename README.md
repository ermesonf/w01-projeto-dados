# Workshop 01 - Projeto de dados

### Instalação e Configuração

1. Clone o repositório:
```bash
git clone https://github.com/ermesonf/w01-projeto-dados.git
cd projeto_dados
```
2. Configure a versão correta do Python com `pyenv`:
```bash
pyenv install 3.11.7
pyenv local 3.11.7
```
3. Instale as dependências do projeto:
```bash
python -m venv .venv
# O padrao é utilizar .venv
source .venv/bin/activate
# Usuários Linux e mac
.venv\Scripts\Activate
# Usuários Windows
pip install -r requirements.txt  
```