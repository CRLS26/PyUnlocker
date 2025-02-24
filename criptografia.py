from cryptography.fernet import Fernet
import hashlib
import json
import os
from datetime import datetime

# Chave secreta compartilhada entre os programas
CHAVE_SECRETA = b'zIpQK6kSuv51qmZdUt7zBzvsbsE6EkAVE_5s_oFtZsc='

def gerar_id_maquina():
    return hashlib.md5(f"{os.environ['COMPUTERNAME']}-{os.environ['USERNAME']}".encode()).hexdigest()

def verificar_codigo():
    id_maquina = gerar_id_maquina()
    pasta_destino = os.path.join(os.environ['LOCALAPPDATA'], 'CNTECH')
    arquivo_codigos = os.path.join(pasta_destino, 'Licence.enc')
    
    if not os.path.exists(arquivo_codigos):
        return False
    
    fernet = Fernet(CHAVE_SECRETA)
    
    try:
        with open(arquivo_codigos, 'rb') as f:
            dados_criptografados = f.read()
        
        dados_decriptografados = json.loads(fernet.decrypt(dados_criptografados).decode())
        
        if id_maquina not in dados_decriptografados:
            return False
        
        codigos_maquina = dados_decriptografados[id_maquina]
        data_atual = datetime.now()
        
        for codigo_info in codigos_maquina:
            data_geracao = datetime.fromisoformat(codigo_info['data_geracao'])
            if (data_atual - data_geracao).days <= 180:
                return True
        
        return False
    except:
        return False
