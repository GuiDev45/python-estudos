import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

# caminho base (resolve imagem)
BASE_DIR = os.path.dirname(__file__)

# Cores
co0 = "#2e2d2b"
co1 = "#feffff"
co2 = "#4fa882"
co3 = "#38576b"
co4 = "#403d3d"
co5 = "#e06636"
co6 = "#038cfc"
co7 = "#3fbfb9"
co8 = "#263238"
co9 = "#e9edf5"
co10 = "#6e8faf"
co11 = "#f2f4f2"

# Janela
janela = tk.Tk()
janela.title("Orçamento")
janela.geometry("250x400")
janela.configure(background=co1)
janela.resizable(width=False, height=False)

style = ttk.Style(janela)
style.theme_use("clam")

# Frames
frameCima = tk.Frame(janela, width=300, height=50, bg=co1, relief="flat")
frameCima.grid(row=0, column=0)

frameMeio = tk.Frame(janela, width=300, height=90, bg=co1, relief="solid")
frameMeio.grid(row=1, column=0)

frameBaixo = tk.Frame(janela, width=300, height=290, bg=co9, relief="raised")
frameBaixo.grid(row=2, column=0)

# Logo (mantido igual)
app_ = tk.Label(frameCima, text="Budget", compound=tk.LEFT, padx=5,
                relief=tk.FLAT, anchor=tk.NW, font=("Verdana 20"),
                bg=co1, fg=co4)
app_.place(x=0, y=0)

# imagem corrigida (sem mudar estilo)
img_path = os.path.join(BASE_DIR, "log.png")
app_img = Image.open(img_path)
app_img = app_img.resize((40, 40))
app_img = ImageTk.PhotoImage(app_img)

app_logo = tk.Label(frameCima, image=app_img, width=900, compound=tk.LEFT,
                    padx=5, relief=tk.FLAT, anchor=tk.NW, bg=co1, fg=co4)
app_logo.place(x=150, y=0)

l_linha = tk.Label(frameCima, width=295, height=1, anchor=tk.NW,
                font=("Verdana 1"), bg=co3, fg=co1)
l_linha.place(x=0, y=47)

# Frame Meio 
l_valor_quantia = tk.Label(frameMeio, text="Renda Mensal?", height=1, anchor=tk.NW,
                        font=("Ivy 10"), bg=co1, fg=co4)
l_valor_quantia.place(x=7, y=15)

e_valor_quantia = tk.Entry(frameMeio, width=10, font=("Ivy 14"), justify="center", relief="solid")
e_valor_quantia.place(x=10, y=40)

def calcular():
    try:
        renda_mensal = float(e_valor_quantia.get())

        vlr_50 = (50/100) * renda_mensal
        vlr_30 = (30/100) * renda_mensal
        vlr_20 = (20/100) * renda_mensal
        
        l_necessidades["text"] = "R${:,.2f}".format(vlr_50)
        l_desejos["text"] = "R${:,.2f}".format(vlr_30)
        l_poupanca["text"] = "R${:,.2f}".format(vlr_20)

    except ValueError:
        # mantém estilo simples (sem popup)
        l_necessidades["text"] = "Valor inválido"
        l_desejos["text"] = ""
        l_poupanca["text"] = ""

botao_calcular = tk.Button(frameMeio, anchor=tk.NW, text="CALCULAR", overrelief=tk.RIDGE,
                        font=("ivy 9"), bg=co1, fg=co0, command=calcular)
botao_calcular.place(x=150, y=40)

# Frame Baixo (mantido igual)
l_nome = tk.Label(frameBaixo, text="Números de 50/30/20 %:", padx=10, width=35,
               height=1, anchor=tk.NW, font=("Verdana 11"), bg=co3, fg=co1)
l_nome.place(x=0, y=0)

l_total_necessidades = tk.Label(frameBaixo, text="Necessidades", height=1, anchor=tk.E,
                             font=("Verdana 10"), bg=co9, fg=co0)
l_total_necessidades.place(x=10, y=40)

l_necessidades = tk.Label(frameBaixo, width=22, height=1, anchor=tk.NW,
                             font=("Verdana 10"), bg=co1, fg=co4)
l_necessidades.place(x=10, y=75)

l_total_desejos = tk.Label(frameBaixo, text="Desejos", height=1, anchor=tk.E, 
                        font=("Verdana 10"), bg=co9, fg=co0)
l_total_desejos.place(x=10, y=115 )

l_desejos = tk.Label(frameBaixo, width=22, height=1, anchor=tk.NW, 
                        font=("Verdana 12"), bg=co1, fg=co4)
l_desejos.place(x=10, y=145 )

l_total_poupanca = tk.Label(frameBaixo, text="Poupança", height=1, anchor=tk.E, 
                        font=("Verdana 10"), bg=co9, fg=co0)
l_total_poupanca.place(x=10, y=185 )

l_poupanca = tk.Label(frameBaixo, width=22, height=1, anchor=tk.NW, 
                        font=("Verdana 12"), bg=co1, fg=co4)
l_poupanca.place(x=10, y=215 )

janela.mainloop()