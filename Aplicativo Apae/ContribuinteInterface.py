from customtkinter import *

def interfaceCadastro():
    contribuintes = CTk()
    contribuintes.title("Cadastrar cliente")
    contribuintes.geometry("500x400+550+200")

    frame = CTkFrame(master=contribuintes)
    frame.pack(expand=True, fill="both", padx=10, pady=10)

    for i in range(8):
        frame.grid_rowconfigure(i, weight=1)
    for j in range(5):
        frame.grid_columnconfigure(j, weight=1)

    label_nome = CTkLabel(master=frame, text="Nome:", text_color="#0F0F0F")
    label_nome.grid(row=0, column=0, padx=(10, 0), pady=5, sticky="w")
    entry_nome = CTkEntry(master=frame)
    entry_nome.grid(row=0, column=1, padx=(0,6), pady=5, sticky="ew", columnspan=4)

    label_endereco = CTkLabel(master=frame, text="Endereço:", text_color="#0F0F0F")
    label_endereco.grid(row=1, column=0, padx=(10, 0), pady=5, sticky="w")
    entry_endereco = CTkEntry(master=frame)
    entry_endereco.grid(row=1, column=1, padx=(0,6), pady=5, sticky="ew", columnspan=2)

    label_numero = CTkLabel(master=frame, text="Nº:", text_color="#0F0F0F")
    label_numero.grid(row=1, column=3, padx=(6, 0), pady=5, sticky="w")
    entry_numero = CTkEntry(master=frame, width=100)
    entry_numero.grid(row=1, column=4, padx=(0,6), pady=5, sticky="ew")

    label_bairro = CTkLabel(master=frame, text="Bairro:", text_color="#0F0F0F")
    label_bairro.grid(row=2, column=0, padx=(10, 0), pady=5, sticky="w")
    entry_bairro = CTkEntry(master=frame)
    entry_bairro.grid(row=2, column=1, padx=(0,6), pady=5, sticky="ew", columnspan=4)

    label_celular = CTkLabel(master=frame, text="Celular:", text_color="#0F0F0F")
    label_celular.grid(row=3, column=0, padx=(10, 0), pady=5, sticky="w")
    entry_celular = CTkEntry(master=frame)
    entry_celular.grid(row=3, column=1, padx=(0,6), pady=5, sticky="ew", columnspan=2)

    label_data = CTkLabel(master=frame, text="Data:", text_color="#0F0F0F")
    label_data.grid(row=3, column=3, padx=(6, 0), pady=5, sticky="w")
    entry_data = CTkEntry(master=frame, width=100)
    entry_data.grid(row=3, column=4, padx=(0,6), pady=5, sticky="ew")

    label_valor = CTkLabel(master=frame, text="Valor:", text_color="#0F0F0F")
    label_valor.grid(row=4, column=0, padx=(10, 0), pady=5, sticky="w")
    entry_valor = CTkEntry(master=frame, width=100)
    entry_valor.grid(row=4, column=1, padx=(0,6), pady=5, sticky="ew")

    label_tipo = CTkLabel(master=frame, text="Tipo:", text_color="#0F0F0F")
    label_tipo.grid(row=5, column=0, padx=(10, 0), pady=5, sticky="w")
    tipo = StringVar(value="PF")
    radioPF = CTkRadioButton(master=frame, text="PF", variable=tipo, value="PF", fg_color="#5bb450")
    radioPF.grid(row=5, column=1, pady=5, sticky="w")
    radioPJ = CTkRadioButton(master=frame, text="PJ", variable=tipo, value="PJ", fg_color="#5bb450")
    radioPJ.grid(row=5, column=2, pady=5, sticky="w")

    label_ativo = CTkLabel(master=frame, text="Ativo:", text_color="#0F0F0F")
    label_ativo.grid(row=6, column=0, padx=(10, 0), pady=5, sticky="w")
    ativo = StringVar(value="Sim")
    radioSim = CTkRadioButton(master=frame, text="Sim", variable=ativo, value="Sim", fg_color="#5bb450")
    radioSim.grid(row=6, column=1, pady=5, sticky="w")
    radioNao = CTkRadioButton(master=frame, text="Não", variable=ativo, value="Não", fg_color="#5bb450")
    radioNao.grid(row=6, column=2, pady=5, sticky="w")

    cadastrarContribuinte = CTkButton(master=frame, text="Cadastrar", fg_color="#5bb450", hover_color="#46923c")
    cadastrarContribuinte.grid(row=7, column=1, pady=10, sticky="ew", columnspan=2)

    limpar = CTkButton(master=frame, text="Limpar", fg_color="#F90000", hover_color="#0f0f0f")
    limpar.grid(row=7, column=3, padx=10 ,pady=10, columnspan=2)

    contribuintes.mainloop()

def interfaceAlterar():
    alterar = CTk()
    alterar.title("Alterar Contribuinte")
    alterar.geometry("300x175+660+250")

    frame = CTkFrame(master=alterar)
    frame.pack(expand=True, fill="both", padx=10, pady=10)

    label_id = CTkLabel(master=frame, text="Informe o ID do contribuinte:", text_color="#0F0F0F")
    label_id.place(relx=0.1, rely=0.1, anchor="nw")
    entry_nome = CTkEntry(master=frame, width=225)
    entry_nome.place(relx=0.1, rely=0.4, anchor="w")
    
    def alterar_contribuinte():
        alterar.destroy()
        interfaceCadastro()

    buscar = CTkButton(master=frame, text="Buscar", command=alterar_contribuinte, fg_color="#5bb450", hover_color="#46923c")
    buscar.place(relx=0.5, rely=0.8, anchor = "center")
    
    alterar.mainloop()

def interfaceExcluir():
    excluir = CTk()
    excluir.title("Deletar Contribuinte")
    excluir.geometry("300x175+660+250")

    frame = CTkFrame(master=excluir)
    frame.pack(expand=True, fill="both", padx=10, pady=10)

    label_id = CTkLabel(master=frame, text="Informe o ID do contribuinte:", text_color="#0F0F0F")
    label_id.place(relx=0.1, rely=0.1, anchor="nw")
    entry_nome = CTkEntry(master=frame, width=225)
    entry_nome.place(relx=0.1, rely=0.4, anchor="w")

    buscar = CTkButton(master=frame, text="Deletar", fg_color="#F90000", hover_color="#0f0f0f")
    buscar.place(relx=0.5, rely=0.8, anchor = "center")
    
    excluir.mainloop()

def interfaceConsultar():
    consultar = CTk()
    consultar.title("Deletar Contribuinte")
    consultar.geometry("400x500+600+200")

    frame = CTkScrollableFrame(master=consultar)
    frame.pack(expand=True, fill="both", padx=10, pady=(50,10))

    label_id = CTkLabel(master=consultar, text="ID", text_color="#0F0F0F")
    label_id.place(relx=0.1, rely=0.03, anchor="nw")

    label_nome = CTkLabel(master=consultar, text="Nome", text_color="#0F0F0F")
    label_nome.place(relx=0.4, rely=0.03, anchor="n")

    consultar.mainloop()
