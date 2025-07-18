import tkinter as tk
from tkinter import messagebox
import pyautogui
import time
import threading
import keyboard

def enviar_mensagens():
    try:
        mensagem = entrada_mensagem.get()
        quantidade = int(entrada_quantidade.get())

        if not mensagem.strip():
            messagebox.showerror("Erro", "Digite uma mensagem válida.")
            return

        messagebox.showinfo("Atenção", "Você terá 5 segundos para clicar na caixa de texto do Discord.\nPressione ESC a qualquer momento para parar.")
        time.sleep(5)

        for i in range(quantidade):
            if keyboard.is_pressed("esc"):
                messagebox.showinfo("Parado", "Envio de mensagens interrompido pela tecla ESC.")
                break
            pyautogui.typewrite(mensagem)
            pyautogui.press("enter")
            time.sleep(1)

    except ValueError:
        messagebox.showerror("Erro", "Quantidade deve ser um número inteiro.")

def iniciar_envio():
    thread = threading.Thread(target=enviar_mensagens)
    thread.start()

# Criação da janela
janela = tk.Tk()
janela.title("Bot de Mensagems")
janela.geometry("400x250")
janela.resizable(False, False)

# Label e campo para mensagem
tk.Label(janela, text="Mensagem:").pack(pady=5)
entrada_mensagem = tk.Entry(janela, width=50)
entrada_mensagem.pack(pady=5)

# Label e campo para quantidade
tk.Label(janela, text="Quantidade de vezes:").pack(pady=5)
entrada_quantidade = tk.Entry(janela, width=10)
entrada_quantidade.pack(pady=5)

# Botão para iniciar
btn_iniciar = tk.Button(janela, text="Enviar", command=iniciar_envio, bg="green", fg="white", width=20)
btn_iniciar.pack(pady=20)

# Informação extra
tk.Label(janela, text="Pressione ESC para parar o envio a qualquer momento.", fg="gray").pack(pady=5)

# Rodar janela
janela.mainloop()
