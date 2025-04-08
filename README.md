# Automação de Cadastro de Produtos

Este projeto utiliza a biblioteca `pyautogui` para automatizar o cadastro de produtos em um sistema web. Ele também usa a biblioteca `pandas` para importar os dados de uma planilha CSV contendo informações sobre os produtos.

## Funcionalidade

O script realiza os seguintes passos:

1. **Abertura do Navegador e Acesso ao Sistema:** 
   - O script abre o navegador Chrome e acessa o URL de login do sistema da empresa.
   
2. **Login no Sistema:** 
   - O login é feito utilizando um nome de usuário e senha configurados diretamente no código.
   
3. **Importação de Dados:**
   - O script importa os dados de uma planilha CSV (`produtos.csv`) que contém as informações dos produtos a serem cadastrados.
   
4. **Cadastro de Produtos:**
   - O script preenche automaticamente os campos do formulário de cadastro de produto no sistema com os dados da planilha. Ele preenche informações como código, marca, tipo, categoria, preço unitário, custo e observações.

5. **Interrupção de Automação:**
   - A automação pode ser interrompida pressionando a tecla "ESC".

## Pré-requisitos

Antes de executar o script, você precisará instalar as dependências. Use o seguinte comando para instalá-las:

```bash
pip install pandas pyautogui keyboard
