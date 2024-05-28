import customtkinter
from customtkinter import *
import Cadastrar

app = CTk()
app.title("APAE")
app.geometry("450x350+600+200")
customtkinter.set_appearance_mode("light")
#customtkinter.set_default_color_theme("green")

tab = CTkTabview(master=app, segmented_button_selected_color="#5bb450", segmented_button_selected_hover_color="#d4d4d4")
tab.pack(expand=1, fill="x", padx = 30, pady = 10, anchor="n")

#Event Handling
def cadastrar_contribuinte():
    Cadastrar.pop()

tab.add("Contribuintes")
#
cadastrar = CTkButton(master=tab.tab("Contribuintes"), text="Cadastrar", command=cadastrar_contribuinte, fg_color="#5bb450", hover_color="#46923c")
cadastrar.place(relx=0.5, rely=0.1, anchor = "center")

alterar = CTkButton(master=tab.tab("Contribuintes"), text="Alterar", fg_color="#5bb450", hover_color="#46923c")
alterar.place(relx=0.5, rely=0.3, anchor = "center")

excluir = CTkButton(master=tab.tab("Contribuintes"), text="Excluir", fg_color="#5bb450", hover_color="#46923c")
excluir.place(relx=0.5, rely=0.5, anchor = "center")

consultar = CTkButton(master=tab.tab("Contribuintes"), text="Consultar Todos", fg_color="#5bb450", hover_color="#46923c")
consultar.place(relx=0.5, rely=0.8, anchor = "center")

sair = CTkButton(master=app, text="Sair", fg_color="#F90000", hover_color="#0f0f0f", command=app.quit)
sair.place(relx=0.5, rely=0.9, anchor = "center")

tab.add("Recibos")
#

tab.add("Relatórios")
#

tab.add("Sobre")
#


app.mainloop()

