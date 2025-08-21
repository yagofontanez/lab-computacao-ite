import tkinter as tk

janela = tk.Tk()

entrada = tk.Entry(janela, width=20)
entrada.grid(row=0, column=0, columnspan=4)


def calc():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Erro")
        
botoes = ['7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', '0', '.', '=', '+']

r = 1; c = 0

for botao in botoes:
    cmd = lambda x=botao: calc() if x == 'x' else entrada.insert(tk.END,x)
    tk.Button(janela, text=botao, command=cmd).grid(row=r, column=c)
    c += 1
    if c > 3:
        c = 0; r += 1
        
janela.mainloop()