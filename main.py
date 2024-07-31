import customtkinter as ctk

def calcular_imc():
    global peso,altura
    pesoConv= peso.get()
    alturaConv= altura.get()
    IMC = float(pesoConv)/(float(alturaConv)**2)
    label =ctk.CTkLabel(root,text=(f"o seu IMC foi :{round(IMC,2)}"))
    label.grid()


root= ctk.CTk()
root.title("IMC-calculadora")
root.geometry("400x400")
root.grid_columnconfigure(0,weight=1)

label = ctk.CTkLabel(root,text="IMC")
label.grid(padx=5,pady=5)

peso = ctk.CTkEntry(root,placeholder_text="peso")
peso.grid(column=0,row=2,pady=20)

altura = ctk.CTkEntry(root,placeholder_text="altura")
altura.grid(column=0,row=3)


botao= ctk.CTkButton(root,text="calcular",command=calcular_imc)
botao.grid(pady=10)


root.mainloop()

