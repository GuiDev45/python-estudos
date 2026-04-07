import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import random
import string
import os

# caminho base
BASE_DIR = os.path.dirname(__file__)

# Cores
co0 = "#444466"
co1 = "#feffff"
co2 = "#6f9fbd"
co3 = "#f05a43"

fundo = co1

root = tk.Tk()
root.title("Gerenciamento de Senhas")
root.geometry("300x360")
root.configure(bg=fundo)

# Frames
frame_main = tk.Frame(root, width=300, height=110, bg=fundo)
frame_main.grid(row=0, column=0)

frame_box = tk.Frame(root, width=300, height=220, bg=fundo)
frame_box.grid(row=1, column=0)

style = ttk.Style(root)
style.theme_use("clam")

# imagem corrigida
img_path = os.path.join(BASE_DIR, "password.png")
img_0 = Image.open(img_path)
img_0 = img_0.resize((30, 30))
img_0 = ImageTk.PhotoImage(img_0)

app_imagem = tk.Label(frame_main, height=60, image=img_0,
                 compound=tk.LEFT, padx=10, relief="flat", anchor="nw",
                 font=("Ivy 16 bold"), bg=co1, fg=co3)
app_imagem.place(x=2, y=0)

app_name = tk.Label(frame_main, text="Gerador de Senhas", height=1, width=20,
                 anchor="nw", font=("Ivy 16 bold"), bg=co1, fg=co0)
app_name.place(x=35, y=2)

app_linha = tk.Label(frame_main, height=1, width=400,
                 font=("Arial 1"), bg=co3)
app_linha.place(x=0, y=35)

alfabeto_menos = string.ascii_lowercase
alfabeto_mais = string.ascii_uppercase
numeros = "123456789"
simbolos = "[]{}()*;/,_-"

var = tk.IntVar(value=8)

app_info = tk.Label(frame_main, text="Número de caracteres da senha",
                 font=("Ivy 10 bold"), bg=fundo, fg=co0)
app_info.place(x=15, y=60)

spin = tk.Spinbox(frame_main, from_=0, to=20, width=5, textvariable=var)
spin.place(x=20, y=90)

app_senha = tk.Label(frame_box, text="- - - ", width=20, height=2,
                  relief="solid", anchor="center", bg=fundo,
                  font=("Ivy 10 bold"), fg=co0)
app_senha.grid(row=0, column=0, columnspan=2, sticky=tk.NSEW, pady=10, padx=2)

# Checkboxes
estado_1 = tk.StringVar(value="off")
estado_2 = tk.StringVar(value="off")
estado_3 = tk.StringVar(value="off")
estado_4 = tk.StringVar(value="off")

tk.Checkbutton(frame_box, var=estado_1, onvalue=alfabeto_mais, offvalue="off", bg=fundo).grid(row=1, column=0)
tk.Label(frame_box, text="ABC Letras Maiúsculas", bg=co1, font=("Ivy 10 bold")).grid(row=1, column=1)

tk.Checkbutton(frame_box, var=estado_2, onvalue=alfabeto_menos, offvalue="off", bg=fundo).grid(row=2, column=0)
tk.Label(frame_box, text="abc Letras minúsculas", bg=co1, font=("Ivy 10 bold")).grid(row=2, column=1)

tk.Checkbutton(frame_box, var=estado_3, onvalue=numeros, offvalue="off", bg=fundo).grid(row=3, column=0)
tk.Label(frame_box, text="123 Números", bg=co1, font=("Ivy 10 bold")).grid(row=3, column=1)

tk.Checkbutton(frame_box, var=estado_4, onvalue=simbolos, offvalue="off", bg=fundo).grid(row=4, column=0)
tk.Label(frame_box, text="!@# Símbolos", bg=co1, font=("Ivy 10 bold")).grid(row=4, column=1)

def criar_senha():
    combinar = ""

    if estado_1.get() != "off":
        combinar += estado_1.get()
    if estado_2.get() != "off":
        combinar += estado_2.get()
    if estado_3.get() != "off":
        combinar += estado_3.get()
    if estado_4.get() != "off":
        combinar += estado_4.get()

    if not combinar:
        messagebox.showwarning("Atenção", "Selecione pelo menos uma opção!")
        return

    comprimento = int(spin.get())

    # usa choices (permite repetição)
    senha = "".join(random.choices(combinar, k=comprimento))
    app_senha["text"] = senha

    def copiar():
        root.clipboard_clear()
        root.clipboard_append(senha)
        messagebox.showinfo("Sucesso", "Senha copiada!")

    tk.Button(frame_box, text="Copiar", command=copiar,
              bg=co1, font=("Ivy 10 bold")).grid(row=0, column=2, padx=2)

tk.Button(frame_box, text="Gerar Senha",
          command=criar_senha,
          bg=co3, fg="white",
          font=("Ivy 10 bold")).grid(row=5, column=0, columnspan=5, pady=20)

root.mainloop()