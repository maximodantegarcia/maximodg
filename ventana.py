from doctest import master
from tkinter import Entry, Label, Frame, Misc, Tk, Button,ttk, Scrollbar, VERTICAL, HORIZONTAL,StringVar,END, Toplevel
from typing import Any
from conexion import*



class Registro(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

    
    def __init__(self, master=None):
        super().__init__(master,width=1920, height=1080)
        self.master = master
        self.pack()
              

    def modificar(self):
        pass
    
    def eliminar(self):
        pass
    
        frame1 = Frame(master, bg="#082338")(master)
        frame1.place(x=0,y=0,width=300, height=1080)
        frame2 = Frame(master, bg="gray")
        frame2.place(x=300, y=0, width=225, height=1080)
        frame3 = Frame(master, bg="white")
        frame3.place(x=526, y=0, width=1395, height=1080)


       
        self.buscar_nombre=Entry(frame1)
        self.buscar_nombre.place(x=45, y=5, width=210, height=25)

        self.btnnuevo=Button(frame1, text="Buscar",command=self.buscar_nombre, bg="white", fg="black", font=10) 
        self.btnnuevo.place(x=45, y=40, width=210, height=25)
        
        self.btnmodificar=Button(frame1, text="modificar",command=self.modificar, bg="white", fg="black", font=10) 
        self.btnmodificar.place(x=45, y=75, width=210, height=25)



        self.Nro_De_Afiliado = StringVar()
        self.Fecha_De_Afiliacion = StringVar()
        self.Apellido_y_nombre = StringVar()
        self.legajo = StringVar()
        self.direccion = StringVar()
        self.localidad = StringVar()
        self.cp = StringVar()
        self.fecha_ingreso = StringVar()
        self.Antigüedad = StringVar()
        self.Fecha_Nacimiento = StringVar()
        self.Edad = StringVar()
        self.DNI = StringVar()
        self.nro = StringVar()
        self.cat = StringVar()
        self.oficina = StringVar()
        self.Nombre_Oficina = StringVar()
        self.Secretaria = StringVar()
        self.sindicato =StringVar ()
        self.Sepelio = StringVar()
        self.Mutual = StringVar()
        self.solo_4 = StringVar()
        self.Seguro = StringVar()
        self.Coseguro = StringVar()
        self.PUESTO = StringVar()
        self.SEXO = StringVar()        
        self.ANTIGÜEDAD = StringVar()
        self.ESTUDIO = StringVar()
        self.buscar = StringVar()
        self.busca_producto = StringVar()
        self.basededatos = Registro_datos()
        self.create_widgets()
       
        lbl1= Label(frame2, text = 'Legajo',fg='white', bg ='gray', font=(7))
        lbl1.place(x=3, y=0)
        lbl1= Label(frame2, text = 'Apellido y Nombre',fg='white', bg ='gray', font=(7))
        lbl1.place(x=3, y=34)
        lbl1= Label(frame2, text ='Direccion',fg='white', bg ='gray', font=(7))
        lbl1.place(x=3, y=68)
        lbl1= Label(frame2, text ='Localidad', fg='white',bg ='gray', font=(7))
        lbl1.place(x=3, y=102)
        lbl1= Label(frame2, text ='Cp',fg='white', bg ='gray', font=(7))
        lbl1.place(x=3, y=136)
        lbl1= Label(frame2, text ='Fecha Ingreso',fg='white', bg ='gray', font=(7))
        lbl1.place(x=3, y=170)
        lbl1= Label(frame2, text ='Antigüedad',fg='white', bg ='gray', font=(7))
        lbl1.place(x=3, y=204)
        lbl1= Label(frame2, text ='Fecha Nacimiento', fg='white',bg ='gray', font=(7))
        lbl1.place(x=3, y=238)
        lbl1= Label(frame2, text ='Edad',fg='white', bg ='gray', font=(7))
        lbl1.place(x=3, y=272)
        lbl1= Label(frame2, text ='DNI',fg='white', bg ='gray', font=(7))
        lbl1.place(x=3, y=306)
        lbl1= Label(frame2, text ='Nro',fg='white', bg ='gray', font=(7))
        lbl1.place(x=3, y=340)
        lbl1= Label(frame2, text = 'Cat',fg='white', bg ='gray', font=(7))
        lbl1.place(x=3, y=374)           
        lbl1= Label(frame2, text = 'Sindicato',fg='white', bg ='gray', font=(7))
        lbl1.place(x=3, y=408)           
        lbl1= Label(frame2, text = 'Oficina',fg='white', bg ='gray', font=(7))
        lbl1.place(x=3, y=442)                    
        lbl1= Label(frame2, text = 'Nombre Oficina',fg='white', bg ='gray', font=(7))
        lbl1.place(x=3, y=476)                    
        lbl1= Label(frame2, text = 'Secretaria',fg='white', bg ='gray', font=(7))   
        lbl1.place(x=3, y= 510)                     
        lbl1= Label(frame2, text = 'Sindicato', fg='white',bg ='gray', font=(7))  
        lbl1.place(x=3, y=544)                        
        lbl1= Label(frame2, text = 'Sepelio',fg='white', bg ='gray', font=(7))    
        lbl1.place(x=3, y=578)                        
        lbl1= Label(frame2, text = 'Mutual',fg='white', bg ='gray', font=(7))   
        lbl1.place(x=3, y=612)                       
        lbl1= Label(frame2, text = 'Solo 4',fg='white', bg ='gray', font=(7)) 
        lbl1.place(x=3, y=646)                      
        lbl1= Label(frame2, text = 'Coseguro',fg='white', bg ='gray', font=(7))
        lbl1.place(x=3, y=680)                   
        lbl1= Label(frame2, text = 'Seguro', fg='white',bg ='gray', font=(7))
        lbl1.place(x=3, y=714)                    
        lbl1= Label(frame2, text = 'PUESTO',fg='white', bg ='gray', font=(7))        
        lbl1.place(x=3, y=748)                    
        lbl1= Label(frame2, text = 'SEXO',fg='white', bg ='gray', font=(7))      
        lbl1.place(x=3, y=782)                   
        lbl1= Label(frame2, text = 'ANTIGÜEDAD',fg='white', bg ='gray', font=(7))      
        lbl1.place(x=3, y=816)                    
        lbl1= Label(frame2, text = 'ESTUDIO',fg='white', bg ='gray', font=(7))            
        lbl1.place(x=3, y=850) 
        lbl1= Label(frame2, text = 'Nro De Afiliado',fg='white', bg ='gray', font=(7))      
        lbl1.place(x=3, y=884)                    
        lbl1= Label(frame2, text = 'Fecha De Afiliacion',fg='white', bg ='gray', font=(7))            
        lbl1.place(x=3, y=918) 
        
        self.nombre=Entry(frame2,textvariable=self.legajo )
        self.nombre.place(x=3, y=21, width=200, height=16)
        self.nombre=Entry(frame2,textvariable=self.Apellido_y_nombre )
        self.nombre.place(x=3, y=55, width=200, height=16)
        self.nombre=Entry(frame2,textvariable=self.direccion )
        self.nombre.place(x=3, y=89, width=200, height=16)
        self.nombre=Entry(frame2,textvariable=self.localidad)
        self.nombre.place(x=3, y=123, width=200, height=16)
        self.nombre=Entry(frame2,textvariable=self.cp)
        self.nombre.place(x=3, y=157, width=200, height=16)
        self.nombre=Entry(frame2,textvariable=self.fecha_ingreso)        
        self.nombre.place(x=3, y=191, width=200, height=16)
        self.nombre=Entry(frame2,textvariable=self.Antigüedad )
        self.nombre.place(x=3, y=225, width=200, height=16)
        self.nombre=Entry(frame2,textvariable=self.Fecha_Nacimiento )
        self.nombre.place(x=3, y=259, width=200, height=16)
        self.nombre=Entry(frame2,textvariable=self.Edad)
        self.nombre.place(x=3, y=293, width=200, height=16)
        self.nombre=Entry(frame2,textvariable=self.DNI )
        self.nombre.place(x=3, y=327, width=200, height=16)
        self.nombre=Entry(frame2,textvariable=self.nro)
        self.nombre.place(x=3, y=361, width=200, height=16)
        self.nombre=Entry(frame2,textvariable=self.cat)
        self.nombre.place(x=3, y=395, width=200, height=16)
        self.nombre=Entry(frame2,textvariable=self.oficina )
        self.nombre.place(x=3, y=429, width=200, height=16)
        self.nombre=Entry(frame2,textvariable=self.Nombre_Oficina)
        self.nombre.place(x=3, y=463, width=200, height=16)
        self.nombre=Entry(frame2,textvariable=self.Secretaria)
        self.nombre.place(x=3, y=497, width=200, height=16)
        self.nombre=Entry(frame2,textvariable=self.sindicato)
        self.nombre.place(x=3, y=531, width=200, height=16)
        self.nombre=Entry(frame2,textvariable=self.Sepelio)
        self.nombre.place(x=3, y=565, width=200, height=16)
        self.nombre=Entry(frame2,textvariable=self.Mutual)
        self.nombre.place(x=3, y=599, width=200, height=16)
        self.nombre=Entry(frame2,textvariable=self.solo_4)
        self.nombre.place(x=3, y=633, width=200, height=16)
        self.nombre=Entry(frame2,textvariable=self.Coseguro)
        self.nombre.place(x=3, y=667, width=200, height=16)
        self.nombre=Entry(frame2,textvariable=self.Seguro)
        self.nombre.place(x=3, y=701, width=200, height=16)
        self.nombre=Entry(frame2,textvariable=self.PUESTO)
        self.nombre.place(x=3, y=735, width=200, height=16)
        self.nombre=Entry(frame2,textvariable=self.SEXO)
        self.nombre.place(x=3, y=769, width=200, height=16)
        self.nombre=Entry(frame2,textvariable=self.ANTIGÜEDAD)
        self.nombre.place(x=3, y=803, width=200, height=16)
        self.nombre=Entry(frame2,textvariable=self.ESTUDIO)
        self.nombre.place(x=3, y=837, width=200, height=16)
        self.nombre=Entry(frame2)
        self.nombre.place(x=3, y=871, width=200, height=16)
        self.nombre=Entry(frame2,textvariable=self.Nro_De_Afiliado)
        self.nombre.place(x=3, y=905, width=200, height=16)
        self.nombre=Entry(frame2,textvariable=self.Fecha_De_Afiliacion)
        self.nombre.place(x=3, y=939, width=200, height=16)
        
              
        self.tabla = ttk.Treeview(frame3, height=30)
        self.tabla.grid(column=0, row=0)
        
        ladox = Scrollbar(frame3, orient = HORIZONTAL, command= self.tabla.xview)
        ladox.grid(column=7, row = 3, sticky='ew') 
        ladoy = Scrollbar(frame3, orient =VERTICAL, command = self.tabla.yview)
        ladoy.grid(column = 3, row = 7, sticky='ns')
        
        
        self.tabla['columns'] =(' LEGAJO, APELLIDO_Y_NOMBRE, DIRECCION, LOCALIDAD, CP, FECHA_INGRESO, ANTIGUEDAD, FECHA_DE_NACIMIENTO, EDAD, DNI, NRO, CAT, OFICINA, NOMBRE_OFICINA, SECRETARIA, SINDICATO, SEPELIO, MUTUAL, SOLO_4, COSEGURO, SEGURO, PUESTO, SEXO, ANTIGÜEDAD, ESTUDIO')
        self.tabla.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)
        self.tabla.column('#0', minwidth=150, width=10 , anchor='center')
        self.tabla.column('LEGAJO', minwidth=150, width=10 , anchor='center' )
        self.tabla.column('direccion', minwidth=150, width=10 , anchor='center')
        self.tabla.column('localidad', minwidth=150, width=10 , anchor='center')
        self.tabla.column('CP', minwidth=40, width=40, anchor='center')
        self.tabla.column('fecha_ingreso', minwidth=150, width=10 , anchor='center')
        self.tabla.column('Antigüedad', minwidth=150, width=10 , anchor='center' )
        self.tabla.column('Fecha_Nacimiento', minwidth=150, width=10 , anchor='center')
        self.tabla.column('Edad', minwidth=50, width=10 , anchor='center')
        self.tabla.column('DNI', minwidth=50, width=10 , anchor='center')
        self.tabla.column('nro', minwidth=150, width=10 , anchor='center')
        self.tabla.column('cat', minwidth=30, width=10 , anchor='center' )
        self.tabla.column('oficina', minwidth=150, width=10 , anchor='center')
        self.tabla.column('Nombre_Oficina', minwidth=150, width=30, anchor='center')
        self.tabla.column('Secretaria', minwidth=150, width=10 , anchor='center')
        self.tabla.column('sindicato', minwidth=70, width=10 , anchor='center')
        self.tabla.column('Sepelio', minwidth=50, width=10, anchor='center' )
        self.tabla.column('Mutual', minwidth=50, width=10 , anchor='center')
        self.tabla.column('solo_4', minwidth=50, width=10, anchor='center')
        self.tabla.column('Coseguro', minwidth=70, width=10, anchor='center')
        self.tabla.column('Seguro', minwidth=50, width=10 , anchor='center')
        self.tabla.column('PUESTO', minwidth=150, width=10, anchor='center' )
        self.tabla.column('SEXO', minwidth=50, width=10 , anchor='center')
        self.tabla.column('ANTIGÜEDAD', minwidth=90, width=10, anchor='center')
        self.tabla.column('ESTUDIO', minwidth=60, width=10, anchor='center')

       
        self.tabla.heading('#0', text='LEGAJO', anchor ='center')
        self.tabla.heading('Apellido_y_nombre', text='Apellido y nombre', anchor ='center')
        self.tabla.heading('direccion', text='direccion', anchor ='center')
        self.tabla.heading('localidad', text='localidad', anchor ='center')
        self.tabla.heading('CP', text='CP', anchor ='center')
        self.tabla.heading('fecha_ingreso', text='fecha ingreso', anchor ='center')
        self.tabla.heading('Antigüedad', text='Antigüedad', anchor ='center')
        self.tabla.heading('Fecha_Nacimiento', text='Fecha Nacimiento', anchor ='center')
        self.tabla.heading('Edad', text='Edad', anchor ='center')
        self.tabla.heading('DNI', text='DNI', anchor ='center')
        self.tabla.heading('nro', text='nro', anchor ='center')
        self.tabla.heading('cat', text='cat', anchor ='center')
        self.tabla.heading('oficina', text='oficina', anchor ='center')
        self.tabla.heading('Nombre_Oficina', text='Nombre Oficina', anchor ='center')
        self.tabla.heading('Secretaria', text='Secretaria', anchor ='center')
        self.tabla.heading('sindicato', text='sindicato', anchor ='center')
        self.tabla.heading('Sepelio', text='Sepelio', anchor ='center')
        self.tabla.heading('Mutual', text='Mutual', anchor ='center')
        self.tabla.heading('solo_4', text='solo_4', anchor ='center')
        self.tabla.heading('Coseguro', text='Coseguro', anchor ='center')
        self.tabla.heading('Seguro', text='Seguro', anchor ='center')
        self.tabla.heading('PUESTO', text='PUESTO', anchor ='center')
        self.tabla.heading('SEXO', text='SEXO', anchor ='center')
        self.tabla.heading('ANTIGÜEDAD', text='ANTIGÜEDAD', anchor ='center')
        self.tabla.heading('ESTUDIO', text='ESTUDIO', anchor ='center')
                
        estilo = ttk.Style(frame3)
        estilo.theme_use('default') #  ('clam', 'alt', 'default', 'classic')
        estilo.configure(".",font= (12), foreground='#082338')        
        estilo.configure("Treeview", font= (10), foreground='black',  background='white')
        estilo.map('Treeview',background=[('selected', 'gray')], foreground=[('selected','black')] )

        self.tabla.bind("<<TreeviewSelect>>", self.obtener_fila)
        

    def agregar_datos(self):
        self.tabla.focus()
        legajo = self.legajo.get()
        Apellido_y_nombre = self.Apellido_y_nombre.get()
        direccion = self.direccion.get()
        localidad = self.localidad.get()
        cp = self.cp.get()
        fecha_ingreso = self.fecha_ingreso.get()
        Antigüedad = self.Antigüedad.get()
        Fecha_Nacimiento = self.Fecha_Nacimiento.get()
        Edad = self.Edad.get()
        DNI = self.DNI.get()
        nro = self.nro.get()
        cat = self.cat.get()
        oficina = self.oficina.get()
        Nombre_Oficina = self.Nombre_Oficina.get()
        Secretaria = self.Secretaria.get()
        sindicato = self.sindicato.get()
        Sepelio = self.Sepelio.get()
        Mutual = self.Mutual.get()
        solo_4 = self.solo_4.get()
        Coseguro = self.Coseguro.get()
        Seguro = self.Seguro.get()
        PUESTO = self.PUESTO.get()
        SEXO = self.SEXO.get()
        ANTIGÜEDAD = self.ANTIGÜEDAD.get()
        ESTUDIO = self.ESTUDIO.get()
        datos = ( legajo, Apellido_y_nombre, direccion, localidad, cp, fecha_ingreso, Antigüedad, Fecha_Nacimiento, Edad, DNI, nro, cat, oficina, Nombre_Oficina, Secretaria, sindicato, Sepelio, Mutual, solo_4, Coseguro, Seguro, PUESTO, SEXO, ANTIGÜEDAD, ESTUDIO)
        if legajo and Apellido_y_nombre and direccion and localidad and cp and fecha_ingreso and Antigüedad and Fecha_Nacimiento and Edad and DNI and nro and cat and oficina and Nombre_Oficina and Secretaria and sindicato and Sepelio and Mutual and solo_4 and Coseguro and Seguro and PUESTO and SEXO and ANTIGÜEDAD and ESTUDIO!='':        
            self.tabla.insert('',0, text = legajo, values=datos)
            self.basededatos.inserta_producto(legajo, Apellido_y_nombre, direccion, localidad, cp, fecha_ingreso, Antigüedad, Fecha_Nacimiento, Edad, DNI, nro, cat, oficina, Nombre_Oficina, Secretaria, sindicato, Sepelio, Mutual, solo_4, Coseguro, Seguro, PUESTO, SEXO, ANTIGÜEDAD, ESTUDIO)


    def buscar_nombre(self):
        nombre_producto = self.buscar.get()
        nombre_producto = str("'" + nombre_producto + "'")
        nombre_buscado = self.sindicato.busca_producto(nombre_producto)
        self.tabla.delete(*self.tabla.get_children())
        i = -1
        for dato in nombre_buscado:
            i= i+1                       
            self.tabla.insert('',i, text = nombre_buscado[i][1:2], values=nombre_buscado[i][2:6])


    def mostrar_todo(self):
        self.tabla.delete(*self.tabla.get_children())
        registro = self.base_datos.mostrar_productos()
        i = -1
        for dato in registro:
            i= i+1                       
            self.tabla.insert('',i, text = registro[i][1:2], values=registro[i][2:6])

    def obtener_fila(self, event):
        current_item = self.tabla.focus()
        if not current_item:
            return
        data = self.tabla.item(current_item)
        self.nombre_borar = data['values'][0]
       

   
if __name__=="__main__":
    Registro_datos()        
