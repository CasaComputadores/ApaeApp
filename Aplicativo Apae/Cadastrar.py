from customtkinter import *

def pop():
    contribuintes = CTk()
    contribuintes.title("Cadastrar cliente")
    contribuintes.geometry("500x300+600+250")

    frame = CTkFrame(master=contribuintes)
    frame.pack(expand=True, fill="both", padx=10, pady=10)   

    for i in range(7):
        frame.grid_rowconfigure(i, weight=0)  # Linhas
    for j in range(5):
        frame.grid_columnconfigure(j, weight=0)  # Colunas

    label_nome = CTkLabel(master=frame, text="Nome:", text_color="#0F0F0F")
    label_nome.grid(row=0, column=0, padx=(10, 0), pady=5, sticky="w")
    #
    entry_nome = CTkEntry(master=frame)
    entry_nome.grid(row=0, column=1, padx=15, pady=5, sticky="ew", columnspan=4)

    label_endereco = CTkLabel(master=frame, text="Endereço:", text_color="#0F0F0F")
    label_endereco.grid(row=1, column=0, padx=(10, 0), pady=5, sticky="w")
    #
    entry_endereco = CTkEntry(master=frame)
    entry_endereco.grid(row=1, column=1, pady=5, sticky="ew", columnspan=2)

    label_numero = CTkLabel(master=frame, text="Nº:", text_color="#0F0F0F")
    label_numero.grid(row=1, column=3, padx=(10, 0), pady=5, sticky="w")
    #
    entry_numero = CTkEntry(master=frame, width=40)
    entry_numero.grid(row=1, column=4, padx=6, pady=5, sticky="ew")

    label_bairro = CTkLabel(master=frame, text="Bairro:", text_color="#0F0F0F")
    label_bairro.grid(row=2, column=0, padx=(10, 0), pady=5, sticky="w")
    #
    entry_bairro = CTkEntry(master=frame)
    entry_bairro.grid(row=2, column=1, padx=6, pady=5, sticky="ew")

    label_celular = CTkLabel(master=frame, text="Celular:", text_color="#0F0F0F")
    label_celular.grid(row=3, column=0, padx=(10, 0), pady=5, sticky="w")
    #
    entry_celular = CTkEntry(master=frame)
    entry_celular.grid(row=3, column=1, padx=6, pady=5, sticky="ew")

    label_valor = CTkLabel(master=frame, text="Valor:", text_color="#0F0F0F")
    label_valor.grid(row=3, column=3, padx=(10, 0), pady=5, sticky="w")
    #
    entry_valor = CTkEntry(master=frame, width=40)
    entry_valor.grid(row=3, column=4, padx=6, pady=5, sticky="ew")

    label_tipo = CTkLabel(master=frame, text="Tipo:", text_color="#0F0F0F")
    label_tipo.grid(row=4, column=0, padx=(10, 0), pady=5, sticky="w")
    #
    tipo = StringVar(value="PF")
    #
    radioPF = CTkRadioButton(master=frame, text="PF", variable=tipo, value="Option 1")
    radioPF.grid(row=4, column=1, pady=5, sticky="ew")
    #
    radioPJ = CTkRadioButton(master=frame, text="PJ", variable=tipo, value="Option 2")
    radioPJ.grid(row=4, column=2, pady=5, sticky="ew")

    label_ativo = CTkLabel(master=frame, text="Ativo:", text_color="#0F0F0F")
    label_ativo.grid(row=5, column=0, padx=(10, 0), pady=5, sticky="w")
    #
    ativo = StringVar(value="Sim")
    #
    radioSim = CTkRadioButton(master=frame, text="Sim", variable=ativo, value="Option 1")
    radioSim.grid(row=5, column=1, pady=5, sticky="ew")
    #
    radioNao = CTkRadioButton(master=frame, text="Não", variable=ativo, value="Option 2")
    radioNao.grid(row=5, column=2, pady=5, sticky="ew")

    cadastrarContribuinte = CTkButton(master=frame, text="Cadastrar")
    cadastrarContribuinte.grid(row=6, column=1, pady=5)

    limpar = CTkButton(master=frame, text="Limpar")
    limpar.grid(row=6, column=2, pady=5)

    contribuintes.mainloop()