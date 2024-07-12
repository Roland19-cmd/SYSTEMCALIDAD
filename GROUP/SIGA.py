from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox


class UIP:
    def __init__(self, root):
        self.root = root
        self.root.title("SISTEMA INTEGRADO DE GESTIÓN ACADEMICA ")
        self.root.geometry("1350x700+0+0")

        title = Label(self.root, text="ESCUELA FISCAL MIXTA LOS LLANGANATES ", bd=10,
                      relief=GROOVE, font=("times new roman", 40, "bold"), bg="darkred", fg="white")
        title.pack(side=TOP, fill=X)


# ===========ALL VARIAbLES===============

        self.estudiante_no = StringVar()
        self.nombre = StringVar()
        self.materia = StringVar()
        self.nota = StringVar()
        self.jornada = StringVar()
        self.estado = StringVar()

        self.search_by = StringVar()
        self.search_txt = StringVar()


# =========MANAGE FRAME=====================================
        Manage_frame = Frame(self.root, bd=4, relief=RIDGE, bg="light blue")
        Manage_frame.place(x=20, y=100, width=450, height=600)

        m_title = Label(Manage_frame, text="ESTUDIANTE", bg="light blue",
                        fg="black", font=("times new roman", 30, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)

        lbl_codigo = Label(Manage_frame, text="ID", bg="light blue",
                           fg="black", font=("times new roman", 20, "bold"))

        lbl_codigo.grid(row=1, column=0, pady=10, padx=20, sticky='w')

        txt_Codigo = Entry(Manage_frame, textvariable=self.estudiante_no, font=(
            "times new roman", 15, "bold"), bd=5, relief=GROOVE)

        txt_Codigo.grid(row=1, column=1, pady=10, padx=20, sticky='w')

        lbl_nombre = Label(Manage_frame, text="NOMBRE", bg="light blue",
                           fg="black", font=("times new roman", 20, "bold"))
        lbl_nombre.grid(row=2, column=0, pady=10, padx=20, sticky='w')

        txt_nombre = Entry(Manage_frame, textvariable=self.nombre, font=(
            "times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_nombre.grid(row=2, column=1, pady=10, padx=20, sticky='w')

        lbl_Materia = Label(Manage_frame, text="MATERIA", bg="light blue",
                            fg="black", font=("times new roman", 20, "bold"))

        lbl_Materia.grid(row=3, column=0, pady=10, padx=20, sticky='w')

        txt_Materia = Entry(Manage_frame, textvariable=self.materia, font=(
            "times new roman", 15, "bold"), bd=5, relief=GROOVE)

        txt_Materia.grid(row=3, column=1, pady=10, padx=20, sticky='w')

        lbl_Nota = Label(Manage_frame, text="NOTA", bg="light blue",
                         fg="black", font=("times new roman", 20, "bold"))
        lbl_Nota.grid(row=4, column=0, pady=10, padx=20, sticky='w')

        txt_Nota = Entry(Manage_frame, textvariable=self.nota, font=(
            "times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Nota.grid(row=4, column=1, pady=10, padx=20, sticky='w')

        lbl_Jornada = Label(Manage_frame, text="JORNADA", bg="light blue",
                            fg="black", font=("times new roman", 20, "bold"))
        lbl_Jornada.grid(row=5, column=0, pady=10, padx=20, sticky='w')

        combo_jornada = ttk.Combobox(Manage_frame, textvariable=self.jornada, font=(
            "times new roman", 13, "bold"), state='readonly')
        combo_jornada['values'] = ("Matutina", "Vespertina", "Nocturna")
        combo_jornada.grid(row=5, column=1, pady=10, padx=20, sticky='w')

        lbl_Estado = Label(Manage_frame, text="ESTADO", bg="light blue",
                           fg="black", font=("times new roman", 20, "bold"))
        lbl_Estado.grid(row=6, column=0, pady=10, padx=20, sticky='w')

        combo_estado = ttk.Combobox(Manage_frame, textvariable=self.estado, font=(
            "times new roman", 13, "bold"), state='readonly')
        combo_estado['values'] = ("Aprobada", "Reprobada",)
        combo_estado.grid(row=6, column=1, pady=10, padx=20, sticky='w')


# =================BUTTON FRAME===============================
        btn_frame = Frame(Manage_frame, bd=4, relief=RIDGE, bg="orange")
        btn_frame.place(x=10, y=520, width=425)

        Addbtn = Button(btn_frame, text="Registrar", width=10, command=self.add_students).grid(
            row=0, column=0, padx=10, pady=20)
        updatebtn = Button(btn_frame, text="Modificar", width=10, command=self.update_data).grid(
            row=0, column=1, padx=10, pady=20)
        deletebtn = Button(btn_frame, text="Eliminar", width=10, command=self.delete_data).grid(
            row=0, column=2, padx=10, pady=20)
        Clearbtn = Button(btn_frame, text="Limpiar", width=10, command=self.clear).grid(
            row=0, column=3, padx=10, pady=20)


# =========DETAIL FRAME=======================================

        Detail_frame = Frame(self.root, bd=4, relief=RIDGE, bg="orange")
        Detail_frame.place(x=500, y=100, width=820, height=600)

        lbl_search = Label(Detail_frame, text="BUSCAR", bg="orange",
                           fg="black", font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky='w')

        combo_search = ttk.Combobox(Detail_frame, textvariable=self.search_by, width=10, font=(
            "times new roman", 13, "bold"), state='readonly')
        combo_search['values'] = ("Estudiante_no", "Nombre", "Materia")
        combo_search.grid(row=0, column=1, pady=10, padx=20, sticky='w')

        txt_Search = Entry(Detail_frame, textvariable=self.search_txt, width=15, font=(
            "times new roman", 10, "bold"), bd=5, relief=GROOVE)
        txt_Search.grid(row=0, column=2, pady=10, padx=20, sticky='w')

        searchbtn = Button(Detail_frame, text="Buscar", width=10, pady=5,
                           command=self.search_data).grid(row=0, column=3, padx=10, pady=20)
        showallbtn = Button(Detail_frame, text="Consulta", width=10, pady=5,
                            command=self.fetch_data).grid(row=0, column=4, padx=10, pady=20)


# ================TABLE FRAME===============================
        Table_frame = Frame(Detail_frame, bd=4, relief=RIDGE, bg="light blue")
        Table_frame.place(x=10, y=70, width=760, height=500)

        scroll_x = Scrollbar(Table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_frame, orient=VERTICAL)
        self.Student_table = ttk.Treeview(Table_frame, column=(
            "estudiante_no", "nombre", "materia", "nota", "jornada", "estado"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("estudiante_no", text="Estudiante no.")
        self.Student_table.heading("nombre", text="Nombre")
        self.Student_table.heading("materia", text="Materia")
        self.Student_table.heading("nota", text="Nota")
        self.Student_table.heading("jornada", text="Jornada")
        self.Student_table.heading("estado", text="Estado")

        self.Student_table['show'] = 'headings'
        self.Student_table.column('estudiante_no', width=100)
        self.Student_table.column('nombre', width=100)
        self.Student_table.column('materia', width=100)
        self.Student_table.column('nota', width=100)
        self.Student_table.column('jornada', width=100)
        self.Student_table.column('estado', width=100)

        self.Student_table.pack(fill=BOTH, expand=1)
        self.Student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_students(self):
        if self.estudiante_no.get() == "" or self.nombre.get() == "" or self.materia.get() == "" or self.nota.get() == "" or self.jornada.get() == "" or self.estado.get() == "":
            messagebox.showerror("Error", "Todos los campos requeridos")

        else:

            con = pymysql.connect(
                host="localhost", user="root", password="2416", database="udelas")
            cur = con.cursor()
            cur.execute("insert into curso values(%s, %s, %s, %s, %s,%s)", (self.estudiante_no.get(),
                                                                            self.nombre.get(),
                                                                            self.materia.get(),
                                                                            self.nota.get(),
                                                                            self.jornada.get(),
                                                                            self.estado.get(),


                                                                            ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Exito", "Los datos han sido registrados.")

    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root",
                              password="2416", database="udelas")
        cur = con.cursor()
        cur.execute("select * from curso")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)
            con.commit()
        con.close()

    def clear(self):
        self.estudiante_no.set(""),
        self.nombre.set(""),
        self.materia.set(""),
        self.nota.set(""),
        self.jornada.set(""),
        self.estado.set(""),

    def get_cursor(self, ev):
        cursor_row = self.Student_table.focus()
        contents = self.Student_table.item(cursor_row)
        row = contents['values']
        self.estudiante_no.set(row[0]),
        self.nombre.set(row[1]),
        self.materia.set(row[2]),
        self.nota.set(row[3]),
        self.jornada.set(row[4]),
        self.estado.set(row[5])

    def update_data(self):
        con = pymysql.connect(host="localhost", user="root",
                              password="2416", database="udelas")
        cur = con.cursor()
        cur.execute("update curso set nombre= %s, materia= %s, jornada= %s, nota= %s, estado= %s where estudiante_no= %s", (

            self.nombre.get(),
            self.materia.get(),
            self.jornada.get(),
            self.nota.get(),
            self.estado.get(),
            self.estudiante_no.get()

        ))

        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def delete_data(self):
        con = pymysql.connect(host="localhost", user="root",
                              password="2416", database="udelas")
        cur = con.cursor()
        cur.execute("delete from curso where Estudiante_no=%s",
                    self.estudiante_no.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        con = pymysql.connect(host="localhost", user="root",
                              password="2416", database="udelas")

        cur = con.cursor()
        cur.execute("select * from curso where "+str(self.search_by.get()
                                                     )+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)
                con.commit()
                con.close()


root = Tk()
ob = UIP(root)
root.mainloop()
