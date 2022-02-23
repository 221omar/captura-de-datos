from cgitb import text
from doctest import master
from pickle import NONE
import tkinter as tk


class Ventana_2 (tk.Frame):
    
    def __init__(self, master = NONE):

        super().__init__(master)
        self.master = master
        self.pack()
        self.config(height= 420, width=500)

        self.labes()
        self.entradas()
        self.botones()
    


    def labes (self):

        #Etiquetas

        self.label_1 = tk.Label(self)
        self.label_1.config(text="N.requiscisión")
        self.label_1.place(x=10,y=40)

        self.label_2 = tk.Label(self)
        self.label_2.config(text="Fecha")
        self.label_2.place(x=10,y=90)

        self.label_3 = tk.Label(self)
        self.label_3.config(text="Partida")
        self.label_3.place(x=10,y=140)

        self.label_4 = tk.Label(self)
        self.label_4.config(text="Status")
        self.label_4.place(x=10,y=190)

        self.label_5 = tk.Label(self)
        self.label_5.config(text="Compras")
        self.label_5.place(x=10,y=240)

        self.label_6 = tk.Label(self)
        self.label_6.config(text="Proovedor")
        self.label_6.place(x=10,y=290)

        self.label_7 = tk.Label(self)
        self.label_7.config(text="N.factura")
        self.label_7.place(x=250,y=40)

        self.label_8 = tk.Label(self)
        self.label_8.config(text="Orden/Compra")
        self.label_8.place(x=250,y=90)

        self.label_9 = tk.Label(self)
        self.label_9.config(text="Recibido")
        self.label_9.place(x=250,y=140)

        self.label_10 = tk.Label(self)
        self.label_10.config(text="Almacen")
        self.label_10.place(x=250,y=190)

        self.label_11 = tk.Label(self)
        self.label_11.config(text="Solicitud")
        self.label_11.place(x=250,y=240)

        self.label_12 = tk.Label(self)
        self.label_12.config(text="Total")
        self.label_12.place(x=250,y=290)

        #cuadros de entrada

        

    def rellenar (self):

        dato_1 = self.texto_1.get()
        dato_2 = self.texto_2.get()
        dato_3 = self.texto_3.get()
        dato_4 = self.texto_4.get()
        dato_5 = self.texto_5.get()
        dato_6 = self.texto_6.get()
        dato_7 = self.texto_7.get()
        dato_8 = self.texto_8.get()
        dato_9 = self.texto_9.get()
        dato_10 = self.texto_10.get()
        dato_11 = self.texto_11.get()
        dato_12 = self.texto_12.get()
        self.master.destroy
        return dato_1,dato_2, dato_3, dato_4, dato_5, dato_6, dato_7, dato_8, dato_9, dato_10, dato_11, dato_12




    def entradas (self):

        self.texto_1 = tk.Entry(self)
        self.texto_1.config(width=15)
        self.texto_1.place(x=95,y=40)

        self.texto_2 = tk.Entry(self)
        self.texto_2.config(width=15)
        self.texto_2.place(x=95,y=90)

        self.texto_3 = tk.Entry(self)
        self.texto_3.config(width=15)
        self.texto_3.place(x=95,y=140)

        self.texto_4 = tk.Entry(self)
        self.texto_4.config(width=15)
        self.texto_4.place(x=95,y=190)

        self.texto_5 = tk.Entry(self)
        self.texto_5.config(width=15)
        self.texto_5.place(x=95,y=240)

        self.texto_6 = tk.Entry(self)
        self.texto_6.config(width=15)
        self.texto_6.place(x=95,y=290)

        self.texto_7 = tk.Entry(self)
        self.texto_7.config(width=15)
        self.texto_7.place(x=340,y=40)

        self.texto_8 = tk.Entry(self)
        self.texto_8.config(width=15)
        self.texto_8.place(x=340,y=90)

        self.texto_9 = tk.Entry(self)
        self.texto_9.config(width=15)
        self.texto_9.place(x=340,y=140)

        self.texto_10 = tk.Entry(self)
        self.texto_10.config(width=15)
        self.texto_10.place(x=340,y=190)

        self.texto_11 = tk.Entry(self)
        self.texto_11.config(width=15)
        self.texto_11.place(x=340,y=240)

        self.texto_12 = tk.Entry(self)
        self.texto_12.config(width=15)
        self.texto_12.place(x=340,y=290)

        #botones

    def botones (self):

        B_A = tk.Button(self)
        B_A.config(text="Aceptar",height= 2, width=10, command= self.rellenar)
        B_A.place(x=80,y=340)

        B_C = tk.Button(self)
        B_C.config(text="Cancelar",height= 2, width=10,command = self.master.destroy)
        B_C.place(x=300,y=340)

    def borrar (self):
        self.texto_1.config(text = " ")
        self.texto_2.config(text = " ")
        self.texto_3.config(text = " ")
        self.texto_4.config(text = " ")
        self.texto_5.config(text = " ")
        self.texto_6.config(text = " ")
        self.texto_7.config(text = " ")
        self.texto_8.config(text = " ")
        self.texto_9.config(text = " ")
        self.texto_10.config(text = " ")
        self.texto_11.config(text = " ")
        self.texto_12.config(text = " ")

    