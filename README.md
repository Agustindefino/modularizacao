# 📇 Agenda Telefônica Modularizada

Este projeto foi desenvolvido como parte do curso no **UniSENAI**, focado na prática de **Modularização e Funções** em Python. O objetivo principal foi transformar um código linear em uma estrutura organizada, reutilizável e de fácil manutenção.

## 🚀 Tecnologias Utilizadas
* **Linguagem:** Python 3.x
* **Conceitos:** Funções (`def`), Parâmetros, Dicionários e Estruturas de Repetição.

## 🧠 Conceitos Aplicados (Baseado no Material Didático)
Seguindo as boas práticas de programação, o código foi dividido em módulos com responsabilidades únicas:

* **Divisão de Responsabilidades:** Cada função resolve um problema específico (Cadastrar, Listar, Exibir Menu).
* **Uso de Parâmetros:** A lista `agenda` é passada como referência para as funções, garantindo a integridade dos dados.
* **Abstração:** O loop principal do aplicativo apenas chama as funções, tornando a leitura do código muito mais clara.

## 🛠️ Funcionalidades
1.  **Cadastrar Contato:** Recebe nome e telefone e armazena em um dicionário dentro da lista.
2.  **Listar Contatos:** Percorre a agenda e exibe todos os contatos salvos.
3.  **Sistema de Menu:** Interface via terminal para navegação do usuário.

## 📋 Como Executar
1. Certifique-se de ter o Python instalado.
2. Clone este repositório.
3. No terminal, execute o comando:
   ```bash
   python main.py