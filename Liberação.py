import tkinter as tk
from tkinter import messagebox
import os
import hashlib
import json
from datetime import datetime
from cryptography.fernet import Fernet
import uuid

CHAVE_SECRETA = b'zIpQK6kSuv51qmZdUt7zBzvsbsE6EkAVE_5s_oFtZsc='

def gerar_id_maquina():
    return hashlib.md5(f"{os.environ['COMPUTERNAME']}-{os.environ['USERNAME']}".encode()).hexdigest()

def gerar_codigo_desbloqueio():
    return uuid.uuid4().hex[:16]

def salvar_codigo(id_maquina, codigo):
    pasta_destino = os.path.join(os.environ['LOCALAPPDATA'], 'CNTECH') # A pasta onde o arquivo será salvo(Pode ser alterada para qualquer nome de sua preferência)
    os.makedirs(pasta_destino, exist_ok=True)
    arquivo_codigos = os.path.join(pasta_destino, 'Licence.enc') # O nome do arquivo que será salvo(Pode ser alterado para qualquer nome de sua preferência)
    
    data_geracao = datetime.now().isoformat()
    fernet = Fernet(CHAVE_SECRETA)
    
    try:
        if os.path.exists(arquivo_codigos):
            with open(arquivo_codigos, 'rb') as f:
                dados = json.loads(fernet.decrypt(f.read()).decode())
        else:
            dados = {}
        
        if id_maquina not in dados or not isinstance(dados[id_maquina], list):
            dados[id_maquina] = []
        
        dados[id_maquina].append({'codigo': codigo, 'data_geracao': data_geracao})
        dados[id_maquina] = dados[id_maquina][-3:]
        
        with open(arquivo_codigos, 'wb') as f:
            f.write(fernet.encrypt(json.dumps(dados).encode()))
        
        return True
    except Exception as e:
        print(f"Erro ao salvar o código: {e}")
        return False

def liberar():
    id_maquina = gerar_id_maquina()
    codigo = gerar_codigo_desbloqueio()
    if salvar_codigo(id_maquina, codigo):
        messagebox.showinfo("Código Gerado", f"Novo código de desbloqueio gerado e salvo com sucesso.\nO programa será fechado.")
        janela.quit()
    else:
        messagebox.showerror("Erro", "Falha ao salvar o código.")

# Interface gráfica principal
janela = tk.Tk()
janela.title("Liberação Movere")
janela.geometry("200x100")

botao_liberar = tk.Button(janela, text="Gerar Código de Liberação", command=liberar)
botao_liberar.pack(expand=True)

janela.mainloop()