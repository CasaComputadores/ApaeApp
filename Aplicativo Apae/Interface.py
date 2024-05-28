import customtkinter
from customtkinter import *
import Cadastrar

app = CTk()
app.title("APAE")
app.geometry("450x350+600+200")
customtkinter.set_appearance_mode("light")

tab = CTkTabview(master=app)
tab.pack(expand=1, fill="x", padx = 30, pady = 10, anchor="n")

#Event Handling
def cadastrar_contribuinte():
    Cadastrar.pop()

tab.add("Contribuintes")
#
cadastrar = CTkButton(master=tab.tab("Contribuintes"), text="Cadastrar", command=cadastrar_contribuinte)
cadastrar.place(relx=0.5, rely=0.1, anchor = "center")

alterar = CTkButton(master=tab.tab("Contribuintes"), text="Alterar")
alterar.place(relx=0.5, rely=0.3, anchor = "center")

excluir = CTkButton(master=tab.tab("Contribuintes"), text="Excluir")
excluir.place(relx=0.5, rely=0.5, anchor = "center")

consultar = CTkButton(master=tab.tab("Contribuintes"), text="Consultar Todos")
consultar.place(relx=0.5, rely=0.8, anchor = "center")

sair = CTkButton(master=app, text="Sair", fg_color="#F94449", command=app.quit)
sair.place(relx=0.5, rely=0.9, anchor = "center")

tab.add("Recibos")
#

tab.add("Relatórios")
#

tab.add("Sobre")
#


app.mainloop()

