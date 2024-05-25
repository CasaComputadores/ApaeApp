from customtkinter import *

def pop():
    contribuintes = CTk()
    contribuintes.title("Cadastrar cliente")
    contribuintes.geometry("400x300+725+250")

    frame = CTkFrame(master=contribuintes)
    frame.pack(expand=True, fill="both", padx=10, pady=10)   

    label_nome = CTkLabel(master=frame, text="Nome:", text_color="#FFFFFF")
    label_nome.pack(anchor="nw", padx=11, pady=11)

    label_endereco = CTkLabel(master=frame, text="Endereço:", text_color="#FFFFFF")
    label_endereco.pack(anchor="nw", padx=11, pady=11)

    label_bairro = CTkLabel(master=frame, text="Bairro:", text_color="#FFFFFF")
    label_bairro.pack(anchor="nw", padx=11, pady=11)

    label_celular = CTkLabel(master=frame, text="Celular:", text_color="#FFFFFF")
    label_celular.pack(anchor="nw", padx=11, pady=11)

    contribuintes.mainloop()
