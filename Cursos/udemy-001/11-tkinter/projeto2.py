import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk
from paises import dados_pais

# Cores
co0 = "#444466"
co1 = "#feffff"
co2 = "#6f9fbd"
co3 = "#38576b"
co4 = "#403d3d"
fundo_cima = "#2aa6a8"

fundo = co1

janela = tk.Tk()
janela.title("Qual país")
janela.geometry("350x310")
janela.configure(bg=co1)

# Frames
ttk.Separator(janela, orient=tk.HORIZONTAL).grid(row=0, columnspan=1, ipadx=172)

frame_cima = tk.Frame(janela, width=350, height=60, bg=fundo_cima)
frame_cima.grid(row=1, column=0)

frame_baixo = tk.Frame(janela, width=350, height=300, bg=fundo)
frame_baixo.grid(row=2, column=0, sticky=tk.NW)

style = ttk.Style(janela)
style.theme_use("default")
style.configure("black.Horizontal.TProgressbar", background="#fcc058")

# Variáveis
pontos = 0
vida = 3
nome_do_pais = ""

# Título
app_nome = tk.Label(
    frame_cima, text="QUAL O PAÍS?",
    font=("Fixedsys 20"),
    bg=fundo_cima, fg=co1
)
app_nome.place(x=15, y=15)

# Barra
bar = Progressbar(frame_baixo, length=293, style="black.Horizontal.TProgressbar")
bar.place(x=27, y=50)
bar['value'] = pontos

l_score = tk.Label(frame_baixo, text="Pontuação: 0",
                   font=("System 17"), bg=fundo, fg=co0)
l_score.place(x=27, y=10)

# Imagens vida
img_0 = ImageTk.PhotoImage(Image.open("0.png").resize((30, 30)))
img_1 = ImageTk.PhotoImage(Image.open("1.png").resize((30, 30)))

l_icon_1 = tk.Label(frame_baixo, image=img_1, bg=fundo)
l_icon_1.place(x=229, y=10)

l_icon_2 = tk.Label(frame_baixo, image=img_1, bg=fundo)
l_icon_2.place(x=259, y=10)

l_icon_3 = tk.Label(frame_baixo, image=img_1, bg=fundo)
l_icon_3.place(x=289, y=10)

# Pergunta
l_perguntas = tk.Label(
    frame_baixo,
    text="Qual país pertence essa bandeira?",
    font=("Ivy 10 bold"),
    bg=co1, fg=co4
)
l_perguntas.place(x=30, y=70)

# Entrada
e_resposta = tk.Entry(frame_baixo, width=15, justify="center")
e_resposta.place(x=178, y=100)


def iniciar_jogo():
    global nome_do_pais, img_bandeira

    dados = dados_pais()
    nome_do_pais = dados[1]
    imagem = dados[0]

    img = Image.open(imagem).resize((140, 100))
    img_bandeira = ImageTk.PhotoImage(img)

    label_bandeira = tk.Label(frame_baixo, image=img_bandeira, bg=fundo)
    label_bandeira.place(x=30, y=100)


def reiniciar_jogo():
    global pontos, vida

    pontos = 0
    vida = 3

    bar['value'] = pontos
    l_score.config(text="Pontuação: 0")

    l_icon_1.config(image=img_1)
    l_icon_2.config(image=img_1)
    l_icon_3.config(image=img_1)

    iniciar_jogo()


def verificar():
    global pontos, vida

    resposta = e_resposta.get().strip().lower()

    if resposta == nome_do_pais.lower():
        pontos += 10
        l_score.config(text=f"Pontuação: {pontos}")
        bar['value'] = pontos
    else:
        messagebox.showerror("Erro", "Resposta incorreta!")
        vida -= 1

        if vida == 2:
            l_icon_1.config(image=img_0)
        elif vida == 1:
            l_icon_2.config(image=img_0)
        elif vida == 0:
            l_icon_3.config(image=img_0)
        elif vida < 0:
            messagebox.showinfo("Game Over", "Fim do jogo!")
            reiniciar_jogo()
            return

    e_resposta.delete(0, tk.END)

    if pontos >= 100:
        messagebox.showinfo("Parabéns", "Você venceu!")
        reiniciar_jogo()
    else:
        iniciar_jogo()


# Botão
btn = tk.Button(
    frame_baixo,
    text="Confirmar",
    command=verificar
)
btn.place(x=210, y=150)

iniciar_jogo()
janela.mainloop()