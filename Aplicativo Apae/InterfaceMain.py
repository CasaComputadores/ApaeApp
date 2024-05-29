import customtkinter
from customtkinter import *
import ContribuinteInterface
import ReciboInterface

app = CTk()
app.title("APAE")
app.geometry("400x500+600+200")
customtkinter.set_appearance_mode("light")
#customtkinter.set_default_color_theme("green")

tab = CTkTabview(master=app, segmented_button_selected_color="#5bb450", segmented_button_selected_hover_color="#d4d4d4")
tab.pack(expand=1, fill="both", padx = 30, pady = (10, 100), anchor="n")

#Event Handling
def cadastrar_contribuinte():
    ContribuinteInterface.interfaceCadastro()

def alterar_contribuinte():
    ContribuinteInterface.interfaceAlterar()

def excluir_contribuinte():
    ContribuinteInterface.interfaceExcluir()

def consultar_contribuintes():
    ContribuinteInterface.interfaceConsultar()

def imprimirReciboTodos():
    ReciboInterface.interfaceImprimirTodos()

tab.add("Contribuintes")
#
cadastrar = CTkButton(master=tab.tab("Contribuintes"), text="Cadastrar", command=cadastrar_contribuinte, fg_color="#5bb450", hover_color="#46923c", width=225)
cadastrar.place(relx=0.5, rely=0.1, anchor = "center")

alterar = CTkButton(master=tab.tab("Contribuintes"), text="Alterar", command=alterar_contribuinte, fg_color="#5bb450", hover_color="#46923c", width=225)
alterar.place(relx=0.5, rely=0.2, anchor = "center")

excluir = CTkButton(master=tab.tab("Contribuintes"), text="Excluir", command=excluir_contribuinte, fg_color="#5bb450", hover_color="#46923c", width=225)
excluir.place(relx=0.5, rely=0.3, anchor = "center")

consultar = CTkButton(master=tab.tab("Contribuintes"), text="Consultar Todos", command=consultar_contribuintes, fg_color="#5bb450", hover_color="#46923c", width=225)
consultar.place(relx=0.5, rely=0.45, anchor = "center")

tab.add("Recibos")
#
baixaRecibo = CTkButton(master=tab.tab("Recibos"), text="Dar Baixa em Recibo", fg_color="#5bb450", hover_color="#46923c", width=225)
baixaRecibo.place(relx=0.5, rely=0.1, anchor = "center")

gerarMes = CTkButton(master=tab.tab("Recibos"), text="Gerar Mês - Todos os Contribuintes", fg_color="#5bb450", hover_color="#46923c", width=225)
gerarMes.place(relx=0.5, rely=0.25, anchor = "center")

gerarMesIndividual = CTkButton(master=tab.tab("Recibos"), text="Gerar Mês - Individual", fg_color="#5bb450", hover_color="#46923c", width=225)
gerarMesIndividual.place(relx=0.5, rely=0.35, anchor = "center")

imprimirRecibos = CTkButton(master=tab.tab("Recibos"), text="Imprimir Recibos - Todos", command=imprimirReciboTodos, fg_color="#5bb450", hover_color="#46923c", width=225)
imprimirRecibos.place(relx=0.5, rely=0.5, anchor = "center")

imprimirRecibosIndiviual = CTkButton(master=tab.tab("Recibos"), text="Imprimir Recibos - Individual", fg_color="#5bb450", hover_color="#46923c", width=225)
imprimirRecibosIndiviual.place(relx=0.5, rely=0.6, anchor = "center")

excluirRecibo = CTkButton(master=tab.tab("Recibos"), text="Excluir Recibos", fg_color="#5bb450", hover_color="#46923c", width=225)
excluirRecibo.place(relx=0.5, rely=0.75, anchor = "center")

tab.add("Relatórios")
#

tab.add("Sobre")
#

sair = CTkButton(master=app, text="Sair", fg_color="#F90000", hover_color="#0f0f0f", command=app.quit, width=225)
sair.place(relx=0.5, rely=0.9, anchor = "center")

app.mainloop()

