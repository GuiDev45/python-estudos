import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from dateutil.relativedelta import relativedelta
from datetime import date

# cores
color1 = "#3b3b3b"  # preta / escura
color2 = "#333333"  # preta / clara
color3 = "#FFFFFF"  # branco
color4 = "#fcc058"  # laranja

window = tk.Tk()
window.title("Calculadora de Idade")
window.geometry("310x410")
window.configure(bg=color1)

style = ttk.Style(window)
style.theme_use("clam")

# Frames
top_frame = tk.Frame(
    window, width=310, height=140, pady=0, padx=0, relief="flat", bg=color2
)
top_frame.grid(row=0, column=0)

bottom_frame = tk.Frame(
    window, width=310, height=410, pady=0, padx=0, relief="flat", bg=color1
)
bottom_frame.grid(row=1, column=0, sticky=tk.NW)

# Labels Top Frame
app_calculator = tk.Label(
    top_frame,
    text="Calculadora de ",
    width=25,
    height=1,
    padx=3,
    relief="flat",
    anchor="center",
    font=("Ivy 15 bold"),
    bg=color2,
    fg=color3,
)
app_calculator.place(x=0, y=30)

app_of_rage = tk.Label(
    top_frame,
    text="Idade",
    width=11,
    height=1,
    padx=0,
    relief="flat",
    anchor="center",
    font=("Arial 35 bold"),
    bg=color2,
    fg=color4,
)
app_of_rage.place(x=0, y=70)

# Labels Bottom Frame
l_initial_date = tk.Label(
    bottom_frame,
    text="Data Atual",
    height=1,
    padx=0,
    pady=0,
    relief="flat",
    anchor=tk.NW,
    font=("Ivy 9"),
    bg=color1,
    fg=color3,
)
l_initial_date.place(x=50, y=30)

cal_initial_date = DateEntry(
    bottom_frame,
    width=10,
    background="darkblue",
    foreground="white",
    borderwidth=2,
    date_pattern="mm/dd/y",
    year=2024,
)
cal_initial_date.place(x=170, y=30)

l_birth_date = tk.Label(
    bottom_frame,
    text="Data de Aniversário",
    height=1,
    padx=0,
    pady=0,
    relief="flat",
    anchor=tk.NW,
    font=("Ivy 9"),
    bg=color1,
    fg=color3,
)
l_birth_date.place(x=50, y=70)

cal_birth_date = DateEntry(
    bottom_frame,
    width=10,
    background="darkblue",
    foreground="white",
    borderwidth=2,
    date_pattern="mm/dd/y",
    year=2000,
)
cal_birth_date.place(x=170, y=70)

app_years = tk.Label(
    bottom_frame,
    text="0",
    height=1,
    padx=0,
    relief="flat",
    anchor="center",
    font=("Ivy 25 bold"),
    bg=color1,
    fg=color3,
)
app_years.place(x=60, y=135)

app_label_years = tk.Label(
    bottom_frame,
    text="Anos",
    height=1,
    padx=0,
    relief="flat",
    anchor="center",
    font=("Ivy 11 bold"),
    bg=color1,
    fg=color3,
)
app_label_years.place(x=50, y=175)

app_months = tk.Label(
    bottom_frame,
    text="0",
    height=1,
    padx=0,
    relief="flat",
    anchor="center",
    font=("Ivy 12 bold"),
    bg=color1,
    fg=color3,
)
app_months.place(x=140, y=135)

app_label_months = tk.Label(
    bottom_frame,
    text="Meses",
    height=1,
    padx=0,
    relief="flat",
    anchor="center",
    font=("Ivy 11 bold"),
    bg=color1,
    fg=color3,
)
app_label_months.place(x=130, y=175)

app_days = tk.Label(
    bottom_frame,
    text="0",
    height=1,
    padx=0,
    relief="flat",
    anchor="center",
    font=("Ivy 12 bold"),
    bg=color1,
    fg=color3,
)
app_days.place(x=220, y=135)

app_label_days = tk.Label(
    bottom_frame,
    text="Dias",
    height=1,
    padx=0,
    relief="flat",
    anchor="center",
    font=("Ivy 11 bold"),
    bg=color1,
    fg=color3,
)
app_label_days.place(x=210, y=175)


# Função para calcular idade
def calculate_age():
    initial_date_str = cal_initial_date.get()
    birth_date_str = cal_birth_date.get()

    month_1, day_1, year_1 = [int(f) for f in initial_date_str.split("/")]
    initial_date = date(year_1, month_1, day_1)

    month_2, day_2, year_2 = [int(f) for f in birth_date_str.split("/")]
    birth_date = date(year_2, month_2, day_2)

    diff = relativedelta(initial_date, birth_date)

    app_years["text"] = diff.years
    app_months["text"] = diff.months
    app_days["text"] = diff.days


# Botão
b_calculate_age = tk.Button(
    bottom_frame,
    text="Calcular Idade",
    width=20,
    height=1,
    bg=color1,
    fg=color3,
    font=("Ivy 10 bold"),
    relief=tk.RAISED,
    overrelief=tk.RIDGE,
    command=calculate_age,
)
b_calculate_age.place(x=60, y=225)

window.mainloop()