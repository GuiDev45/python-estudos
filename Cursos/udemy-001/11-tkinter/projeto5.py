import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

from dados import pokemon

# caminho base (resolve imagens)
BASE_DIR = os.path.dirname(__file__)

def caminho_img(path):
    return os.path.join(BASE_DIR, path)

# Cores
co0 = "#444466"
co1 = "#feffff"
co2 = "#6f9fbd"
co3 = "#38576b"
co4 = "#403d3d"
co5 = "#ef5350"

janela = tk.Tk()
janela.title("Pokemon")
janela.geometry("550x510")
janela.configure(bg=co1)

ttk.Separator(janela, orient=tk.HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

style = ttk.Style(janela)
style.theme_use("clam")

frame_pokemon = tk.Frame(janela, width=550, height=290, relief="flat")
frame_pokemon.grid(row=1, column=0)

# Nome
pok_nome = tk.Label(frame_pokemon, text="", anchor="center",
                 font=("Fixedsys 20"), bg=co1, fg=co1)
pok_nome.place(x=12, y=15)

# Tipo
pok_tipo = tk.Label(frame_pokemon, text="", anchor=tk.NW,
                 font=("Ivy 10 bold"), bg=co1, fg=co1)
pok_tipo.place(x=12, y=50)

# Numero
pok_numero = tk.Label(frame_pokemon, text="", anchor="center",
                 font=("Ivy 12"), bg=co1, fg=co1)
pok_numero.place(x=12, y=75)

# Imagem inicial
img_pokemon = Image.open(caminho_img("img/pikachu.png"))
img_pokemon = img_pokemon.resize((238, 238))
img_pokemon = ImageTk.PhotoImage(img_pokemon)

l_icon_1 = tk.Label(frame_pokemon, image=img_pokemon, bg=co1)
l_icon_1.place(x=60, y=50)

# Status
pok_status = tk.Label(janela, text="Status", font=("Verdana 20"), bg=co1, fg=co0)
pok_status.place(x=15, y=310)

pok_hp = tk.Label(janela, text="HP: 100", font=("Verdana 10"), bg=co1, fg=co4)
pok_hp.place(x=20, y=360)

pok_atack = tk.Label(janela, text="Atack: 300", font=("Verdana 10"), bg=co1, fg=co4)
pok_atack.place(x=20, y=385)

pok_defesa = tk.Label(janela, text="Defesa: 500", font=("Verdana 10"), bg=co1, fg=co4)
pok_defesa.place(x=20, y=410)

pok_velocidade = tk.Label(janela, text="Velocidade: 100", font=("Verdana 10"), bg=co1, fg=co3)
pok_velocidade.place(x=20, y=435)

pok_total = tk.Label(janela, text="Total: 100", font=("Verdana 10"), bg=co1, fg=co3)
pok_total.place(x=20, y=460)

# Habilidades
pok_habilidade = tk.Label(janela, text="Habilidades",
                       font=("Verdana 20"), bg=co1, fg=co0)
pok_habilidade.place(x=180, y=310)

pok_hb_1 = tk.Label(janela, text="Jato d'Água",
                 font=("Verdana 10"), bg=co1, fg=co4)
pok_hb_1.place(x=195, y=360)

pok_hb_2 = tk.Label(janela, text="Hidro Bomba",
                 font=("Verdana 10"), bg=co1, fg=co4)
pok_hb_2.place(x=195, y=385)

pok_tipo.lift()
pok_numero.lift()

# Função trocar
def trocar(i):
    global img_pokemon
    
    imagem = pokemon[i]['outros'][0]
    img_pokemon = Image.open(caminho_img(imagem))
    img_pokemon = img_pokemon.resize((238, 238))
    img_pokemon = ImageTk.PhotoImage(img_pokemon)
    
    # reutiliza label
    l_icon_1.config(image=img_pokemon, bg=pokemon[i]['outros'][1])
    
    # tipo pokemon
    pok_nome["text"] = i
    pok_nome["bg"] = pokemon[i]['outros'][1]
    
    pok_tipo["text"] = pokemon[i]['tipo'][1]
    pok_tipo["bg"] = pokemon[i]['outros'][1]
    
    pok_numero["text"] = pokemon[i]['tipo'][0]
    pok_numero["bg"] = pokemon[i]['outros'][1]
    
    frame_pokemon["bg"] = pokemon[i]['outros'][1]
    
    # status
    pok_hp["text"] = pokemon[i]['status'][0]
    pok_atack["text"] = pokemon[i]['status'][1]
    pok_defesa["text"] = pokemon[i]['status'][2]
    pok_velocidade["text"] = pokemon[i]['status'][3]
    pok_total["text"] = pokemon[i]['status'][4]
    
    # habilidades
    pok_hb_1["text"] = pokemon[i]['habilidades'][0]
    pok_hb_2["text"] = pokemon[i]['habilidades'][1]
    
    pok_tipo.lift()
    pok_numero.lift()

# Botões
def criar_botao(nome, img_file, y):
    img = Image.open(caminho_img(img_file))
    img = img.resize((40, 40))
    img = ImageTk.PhotoImage(img)
    
    btn = tk.Button(janela, command=lambda: trocar(nome),
        text="  " + nome, width=150, image=img, padx=5,
        compound=tk.LEFT, relief="raised", overrelief=tk.RIDGE,
        anchor=tk.NW, font=("Verdana 12"), bg=co1, fg=co0)
    btn.image = img  # evitar garbage collector
    btn.place(x=375, y=y)

criar_botao("Pikachu", "img/cabeca-pikachu.png", 10)
criar_botao("Bulbasaur", "img/cabeca-bulbasaur.png", 65)
criar_botao("Charmander", "img/cabeca-charmander.png", 120)
criar_botao("Gyarados", "img/cabeca-gyarados.png", 175)
criar_botao("Gengar", "img/cabeca-gengar.png", 230)
criar_botao("Dragonite", "img/cabeca-dragonite.png", 285)

janela.mainloop()