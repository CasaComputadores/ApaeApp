from customtkinter import *
import Cadastrar

app = CTk()
app.title("APAE")
app.geometry("600x400+600+200")

tab = CTkTabview(master=app)
tab.pack(expand=1, fill="both", padx = 10, pady = 10)

#Event Handling
def cadastrar_contribuinte():
    Cadastrar.pop()

tab.add("Contribuintes")
#
cadastrar = CTkButton(master=tab.tab("Contribuintes"), text="Cadastrar", command=cadastrar_contribuinte)
cadastrar.place(relx=0.5, rely=0.2, anchor = "center")

alterar = CTkButton(master=tab.tab("Contribuintes"), text="Alterar")
alterar.place(relx=0.5, rely=0.3, anchor = "center")

exlcuir = CTkButton(master=tab.tab("Contribuintes"), text="Excluir")
exlcuir.place(relx=0.5, rely=0.4, anchor = "center")

consultar = CTkButton(master=tab.tab("Contribuintes"), text="Consultar Todos")
consultar.place(relx=0.5, rely=0.55, anchor = "center")

sair = CTkButton(master=tab.tab("Contribuintes"), text="Sair", fg_color="#F94449")
sair.place(relx=0.5, rely=0.9, anchor = "center")

tab.add("Recibos")
#

tab.add("Relatórios")
#

tab.add("Sobre")
#


app.mainloop()

