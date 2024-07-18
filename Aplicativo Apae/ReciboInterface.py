from customtkinter import *

def interfaceImprimirTodos():
    imprimirTodos = CTk()
    imprimirTodos.title("Imprimir Todos os Recibos")
    imprimirTodos.geometry("500x150+550+350")

    frame = CTkFrame(master=imprimirTodos)
    frame.pack(expand=True, fill="both", padx=10, pady=10)

    label_mes = CTkLabel(master=frame, text="Mês:", text_color="#0F0F0F")
    label_mes.place(relx=0.05, rely=0.25, anchor="w")
    combo_mes = CTkComboBox(master=frame, values=["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outbro","Novembro","Dezembro"])
    combo_mes.place(relx=0.15, rely=0.25, anchor="w")

    label_ano = CTkLabel(master=frame, text="Ano:", text_color="#0F0F0F")
    label_ano.place(relx=0.6, rely=0.25, anchor="w")
    entry_ano = CTkEntry(master=frame, width=120)
    entry_ano.place(relx=0.7, rely=0.25, anchor="w")

    buscar = CTkButton(master=frame, text="Imprimir", fg_color="#5bb450", hover_color="#46923c")
    buscar.place(relx=0.5, rely=0.75, anchor = "center")
    
    imprimirTodos.mainloop()

def interfaceBaixaRecibo():
    baixaRecibo = CTk()
    baixaRecibo.title("Alterar Recibo")
    baixaRecibo.geometry("350x125+630+350")

    frame = CTkFrame(master=baixaRecibo)
    frame.pack(expand=True, fill="both", padx=10, pady=10)

    label_nRecibo = CTkLabel(master=frame, text="Número do Recibo:", text_color="#0F0F0F")
    label_nRecibo.place(relx=0.05, rely=0.25, anchor="w")
    entry_nRecibo = CTkEntry(master=frame, width=150)
    entry_nRecibo.place(relx=0.9, rely=0.25, anchor="e")

    buscar = CTkButton(master=frame, text="Buscar", fg_color="#5bb450", hover_color="#46923c")
    buscar.place(relx=0.5, rely=0.75, anchor = "center")

    baixaRecibo.mainloop()