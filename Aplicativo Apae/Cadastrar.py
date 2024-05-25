from customtkinter import *

def pop():
    contribuintes = CTk()
    contribuintes.title("Cadastrar cliente")
    contribuintes.geometry("500x300+600+250")

    frame = CTkFrame(master=contribuintes)
    frame.pack(expand=True, fill="both", padx=10, pady=10)   

    for i in range(5):
        frame.grid_rowconfigure(i, weight=0)  # Linhas
    for j in range(5):
        frame.grid_columnconfigure(j, weight=1)  # Colunas

    label_nome = CTkLabel(master=frame, text="Nome:", text_color="#FFFFFF")
    label_nome.grid(row=0, column=0, padx=(10, 0), pady=5, sticky="w")
    #
    entry_nome = CTkEntry(master=frame)
    entry_nome.grid(row=0, column=1, padx=15, pady=5, sticky="ew", columnspan=4)

    label_endereco = CTkLabel(master=frame, text="Endereço:", text_color="#FFFFFF")
    label_endereco.grid(row=1, column=0, padx=(10, 0), pady=5, sticky="w")
    #
    entry_endereco = CTkEntry(master=frame)
    entry_endereco.grid(row=1, column=1, pady=5, sticky="ew", columnspan=2)

    label_numero = CTkLabel(master=frame, text="Nº:", text_color="#FFFFFF")
    label_numero.grid(row=1, column=3, padx=(10, 0), pady=5, sticky="w")
    #
    entry_numero = CTkEntry(master=frame, width=40)
    entry_numero.grid(row=1, column=4, padx=6, pady=5, sticky="ew")

    label_bairro = CTkLabel(master=frame, text="Bairro:", text_color="#FFFFFF")
    label_bairro.grid(row=2, column=0, padx=(10, 0), pady=5, sticky="w")
    #
    entry_bairro = CTkEntry(master=frame)
    entry_bairro.grid(row=2, column=1, padx=6, pady=5, sticky="ew")

    label_celular = CTkLabel(master=frame, text="Celular:", text_color="#FFFFFF")
    label_celular.grid(row=3, column=0, padx=(10, 0), pady=5, sticky="w")
    #
    entry_celular = CTkEntry(master=frame)
    entry_celular.grid(row=3, column=1, padx=6, pady=5, sticky="ew")

    contribuintes.mainloop()