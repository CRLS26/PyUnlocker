# PyUnlocker

O PyUnlocker é um conjunto de scripts Python que permite a geração de códigos de desbloqueio para acesso a um programa protegido. O projeto é dividido em três scripts principais:

## Scripts

### 1. Liberação.py

O script `Liberação.py` é responsável por gerar um código de desbloqueio utilizando uma chave secreta. Ele realiza as seguintes funções:

- Gera um ID único para a máquina, combinando o nome do computador e o nome do usuário.
- Gera um código de desbloqueio aleatório.
- Salva o código gerado em um arquivo criptografado (`Licence.enc`) dentro de uma pasta chamada `CNTECH` no diretório local do usuário.

### 2. Criptografia.py

O script `Criptografia.py` complementa outros programas que necessitam de proteção. Ele utiliza o arquivo `Licence.enc` gerado pelo `Liberação.py` para verificar se o acesso ao programa deve ser concedido. O acesso é permitido apenas após a liberação bem-sucedida através do `Liberação.py`.

### 3. Gerador de Chave.py

O script `Gerador de Chave.py` é utilizado para gerar uma nova chave secreta. Essa chave pode ser utilizada para alterar a chave existente no `Liberação.py`. O script é simples e automatiza o processo de geração de chaves, facilitando a manutenção da segurança do sistema.

## Como Usar

1. Execute o `Gerador de Chave.py` para criar uma nova chave secreta, se necessário.
2. Execute o `Liberação.py` para gerar um código de desbloqueio e salvá-lo no arquivo `Licence.enc`.
3. Utilize o `Criptografia.py` em seu programa para verificar o acesso com base no código gerado.

## Requisitos

- Python 3.x
- Bibliotecas: `tkinter`, `hashlib`, `json`, `datetime`, `cryptography`

💙 **Agradecimentos**  
💻 **Contribuidores do projeto**  
🛠 **Usuários que reportam bugs e sugerem melhorias**  

## 📩 Contato

Se tiver dúvidas ou quiser saber mais sobre o projeto, entre em contato:  
👤 **Carlos Teixeira**  
📧 **Email:** carlosteixeiraneto26@gmail.com  
💼 **LinkedIn:** [Carlos Neto](https://www.linkedin.com/in/carlos-neto-861541252/)
