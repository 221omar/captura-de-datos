from doctest import master
from pickle import NONE
import tkinter as tk
from tkinter import BOTTOM, ttk
from turtle import width
from cliente.ventana_entradas import Ventana_2


def barra_menu(V1):
    barra_menu = tk.Menu(V1)
    V1.config(menu = barra_menu)

    menu_inicio = tk.Menu(barra_menu, tearoff= 0) 
    barra_menu.add_cascade(label = "Inicio", menu = menu_inicio)

    menu_inicio.add_command(label = "Agregar", command = Ventana_2)
    menu_inicio.add_command(label = "Modificar", command = Ventana_2)
    menu_inicio.add_command(label = "Salir", command = V1.destroy)

    menu_reporte = tk.Menu(barra_menu, tearoff= 0) 
    barra_menu.add_cascade (label = "Reporte", menu = menu_reporte)

    menu_reporte.add_command(label = "Compras")
    menu_reporte.add_command(label = "Presupuesto")


class Frame (tk.Frame):

    def __init__(self, V1=NONE ):

        super().__init__(V1)
        self.V1 = V1
        self.pack()
        self.config(height= 500, width=600)
        self.llenar = Ventana_2(V2=NONE)

        self.barra_busqueda()
        self.tabla()

    
    def barra_busqueda(self):

        #Etiqueta
        self.texto_busqueda = tk.Label(self)
        self.texto_busqueda.config(text = "Requiscisión",font=("Helvetica", 11, "bold"))
        self.texto_busqueda.place(x=15, y=97)

        #barra de busqueda
        self.busqueda = tk.Entry(self)
        self.busqueda.config(width=40)
        self.busqueda.place(x=125, y=100)

        #boton de busqueda
        self.boton_busqueda = tk.Button(self)
        self.boton_busqueda.config(text = "Buscar")
        self.boton_busqueda.place(x=380, y=95)

    def tabla(self):

        #tabla
        self.tabla = ttk.Treeview(self,
        columns = ("Fecha", "Partida","Status","Compras","Proovedor","Factura","Orden","Recibe", "Almacen", "Solicitud","Total")    )
        self.tabla.heading("#0", text="Requiscisión")
        self.tabla.heading("Fecha", text="Fecha")
        self.tabla.heading("Partida", text="Partida")
        self.tabla.heading("Status", text="Status")
        self.tabla.heading("Compras", text="Compras")
        self.tabla.heading("Proovedor", text="Proovedor")
        self.tabla.heading("Factura", text="Factura")
        self.tabla.heading("Orden", text="Orden/Compra")
        self.tabla.heading("Recibe", text="Recibido")
        self.tabla.heading("Almacen", text="Almacen")
        self.tabla.heading("Solicitud", text="Solicitud")
        self.tabla.heading("Total", text="Total")
        self.tabla.place(x=45, y=135, height= 300, width = 450)

        #barra orizontal
        barrita_o = ttk.Scrollbar(self.tabla, orient = tk.HORIZONTAL)
        barrita_o.config(command = self.tabla.xview)
        self.tabla.config(xscrollcommand = barrita_o.set)
        barrita_o.place(x=0,y=285, width = 450)

        #barra vertical
        barrita_v = ttk.Scrollbar(self.tabla, orient = tk.VERTICAL)
        barrita_v.config(command = self.tabla.xview)
        self.tabla.config(yscrollcommand = barrita_v.set)
        barrita_v.place(x=435,y=0, height = 450)

    def ventana_2 (self):
        V2 = tk.Tk()
        V2.title("Captura de datos")
        V2.resizable(0,0)
        self.llenar(V2)
        self.llenar.mainloop()

#    def guardar ():
#        llenar.rellenar()