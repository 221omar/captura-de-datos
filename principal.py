import tkinter as tk
from cliente.ventana1 import Frame, barra_menu


def main():
    V1 = tk.Tk()
    V1.title("Control de compras")
    V1.resizable(0,0)
    barra_menu(V1)

    panel = Frame(V1 = V1)

    panel.mainloop()

if __name__ == "__main__":
    main()