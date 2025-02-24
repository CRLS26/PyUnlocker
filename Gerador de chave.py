import tkinter as tk
from tkinter import messagebox, Toplevel
from tkinter import ttk
from cryptography.fernet import Fernet

def gerar_nova_chave_secreta():
    return Fernet.generate_key()

def mostrar_nova_chave():
    nova_chave = gerar_nova_chave_secreta().decode()
    janela_chave = Toplevel(root)
    janela_chave.title("Nova Chave Secreta")
    ttk.Label(janela_chave, text=f"A nova chave secreta gerada é:\n{nova_chave}", font=("Helvetica", 12)).pack(pady=10)
    ttk.Button(janela_chave, text="Copiar Chave", command=lambda: copiar_chave(nova_chave)).pack(pady=10)

def copiar_chave(chave_str):
    root.clipboard_clear()
    root.clipboard_append(chave_str)
    root.update()
    messagebox.showinfo("Copiar Chave", "A chave foi copiada para a área de transferência!")
    root.quit()

root = tk.Tk()
root.title("Gerador de Chave Secreta")
root.geometry("220x150")
root.resizable(False, False)
ttk.Button(root, text="Gerar Nova Chave Secreta", command=mostrar_nova_chave).pack(pady=60)
root.mainloop()