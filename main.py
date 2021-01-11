try:
    import Tkinter as tk
except:
    import tkinter as tk

import mysql.connector
from mysql.connector import Error
import datetime

import tkinter.ttk as ttk

ERROR_LABEL_MSG = "ERROR wrong input or DB not responds"

DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "My3qlP@ssword"
DB_DATABASE = "mydb"


class Test():
    def __init__(self):
        self.widget_list_of_create_frame = []
        self.widget_list_of_accept_frame = []
        self.root = tk.Tk()
        self.root.geometry("800x400")
        self.root.title("ADAS")


        self.switch_btn_frame=tk.Frame(self.root)
        self.switch_btn_frame.pack()
        self.place_switch_buttons()
        #frame what stores labels and entrys for object creation
        self.obj_data_input_frame=tk.Frame(self.root)
        self.obj_data_input_frame.pack()
        self.create_cf_labels_and_entrys()

        """
        # create frame stuff
        self.place_create_frame_labels()
        self.place_create_frame_entrys()
        self.place_create_frame_submit_btn()
        self.place_create_frame_response_lebel()
        # accept frame stuff
        self.show_accept_frame_widgets()
        self.create_place_treeview()

        self.af_frame=tk.Frame(self.root)
        self.af_frame.grid(row=2)
        self.place_accept_frame_btn()
        self.place_accept_frame_response_lebel()
        self.place_update_treeview_btn()
        """
        """
               self.place_switch_buttons()
               # create frame stuff
               self.place_create_frame_labels()
               self.place_create_frame_entrys()
               self.place_create_frame_submit_btn()
               self.place_create_frame_response_lebel()
               # accept frame stuff
               self.show_accept_frame_widgets()
               self.create_place_treeview()

               self.af_frame=tk.Frame(self.root)
               self.af_frame.grid(row=2)
               self.place_accept_frame_btn()
               self.place_accept_frame_response_lebel()
               self.place_update_treeview_btn()
               """

    def quit(self):
        self.root.destroy()

    def mainloop(self):
        self.root.mainloop()

    def place_switch_buttons(self):
        btn_show_create_frame = tk.Button(self.switch_btn_frame, text='Ielikt jaunu obj', bg="blue",
                                          command=self.show_create_frame_widgets,
                                          width=40, height=5)
        btn_show_create_frame.pack(side="left")

        btn_show_accept_frame = tk.Button(self.switch_btn_frame, text='Pienemt obj   ',
                                          command=self.show_accept_frame_widgets, bg='white',
                                          width=50, height=5)
        btn_show_accept_frame.pack(side="left")

    # All about create frame
    def create_cf_labels_and_entrys(self):
        frame1=tk.Frame(self.obj_data_input_frame)
        frame1.pack()
        frame2 = tk.Frame(self.obj_data_input_frame)
        frame2.pack()
        #adress label and entry
        self.adress_label = tk.Label(frame1, text="ADRESE(STRING)", borderwidth=3, relief="sunken", width=40,
                                     height=2)
        self.adress_label.pack(side="left")
        self.widget_list_of_create_frame.append(self.adress_label)

        self.adress_entry = tk.Entry(frame1, borderwidth=3, width=40)
        self.adress_entry.pack(side="left")
        self.widget_list_of_create_frame.append(self.adress_entry)

        #date to do the object
        self.date_todo_label = tk.Label(frame2, text="KAD(YYYY-MM-DD)", borderwidth=3, relief="sunken", width=40,
                                        height=2)
        self.date_todo_label.pack(side="left")
        self.widget_list_of_create_frame.append(self.date_todo_label)

        self.date_todo_entry = tk.Entry(frame2, borderwidth=3, width=40)
        self.date_todo_entry.pack(side="left")
        self.widget_list_of_create_frame.append(self.date_todo_entry)
        """
        #priority label
        self.priority_label = tk.Label(self.obj_data_input_frame, text="Pioritate(NUMBER)", borderwidth=3, relief="sunken", width=40,
                                       height=2)
        self.priority_label.pack(side="left")
        self.widget_list_of_create_frame.append(self.priority_label)
        
        self.priority_entry = tk.Entry(self.obj_data_input_frame, borderwidth=3, width=30)
        self.priority_entry.pack(side="left")
        self.widget_list_of_create_frame.append(self.priority_entry)
        
        #brigade
        self.brigade_num_label = tk.Label(self.obj_data_input_frame, text="Brigade(NUMBER)", borderwidth=3, relief="sunken", width=40,
                                          height=2)
        self.brigade_num_label.pack(side="left")
        self.widget_list_of_create_frame.append(self.brigade_num_label)

        self.brigade_num_entry = tk.Entry(self.obj_data_input_frame, borderwidth=3, width=30)
        self.brigade_num_entry.pack(side="left")
        self.widget_list_of_create_frame.append(self.brigade_num_entry)
        
        #comentary 
        self.commentary_label = tk.Label(self.obj_data_input_frame, text="Komentars", borderwidth=3, relief="sunken",
                                         width=40, height=2)
        self.commentary_label.pack(side="left")
        self.widget_list_of_create_frame.append(self.commentary_label)

        self.commentary_entry = tk.Entry(self.obj_data_input_frame, borderwidth=3, width=30)
        self.commentary_entry.pack(side="left")
        self.widget_list_of_create_frame.append(self.commentary_entry)"""



    def place_create_frame_submit_btn(self):
        """places submit button"""
        self.submit_btn = tk.Button(self.root, text='IERAKSTIT', bg="green", relief="groove",
                                    command=self.insert_entrys_data_into_db,
                                    width=40, height=5)
        self.submit_btn.grid(column=0, row=7)
        self.widget_list_of_create_frame.append(self.submit_btn)

    def place_create_frame_response_lebel(self):
        self.cf_response_label = tk.Label(self.root, text="result msg", borderwidth=3, relief="sunken",
                                          width=30, height=2)
        self.cf_response_label.grid(column=1, row=7, padx=5, pady=5)
        self.widget_list_of_create_frame.append(self.cf_response_label)

    def place_accept_frame_response_lebel(self):
        self.af_response_label = tk.Label(self.root, text="result msg", borderwidth=3, relief="sunken",
                                          width=30, height=2)
        self.af_response_label.grid(column=1, row=2, padx=5, pady=5)
        self.widget_list_of_accept_frame.append(self.af_response_label)

    def show_create_frame_widgets(self):
        # hides accept frame widgets
        for w in self.widget_list_of_accept_frame:
            w.grid_remove()
        # shows create frame widgets
        for w in self.widget_list_of_create_frame:
            w.grid()
        # changes collor
        self.btn_show_accept_frame.config(bg="white")
        self.btn_show_create_frame.config(bg='blue')
        self.cf_response_label.config(text="response msg will appier here")

    def insert_entrys_data_into_db(self):
        """creating frame button function what takes entrys data and
        create query and puts this data into db"""
        conn = self.create_db_connection()
        if conn == None:
            pass

        insert_data_query = "INSERT INTO mydb.objekts (ADRESS,DATE_THEN_TODO , PRORITY,DONE,ACCEPTED,BRIGADE_BRIG_NUM," \
                            "COMENT) VALUES "

        adress = str(self.adress_entry.get())

        # priority_label
        priority = str(self.priority_entry.get())
        if type(priority) == int:
            if priority > 3 or priority < 0:
                priority = 1
        else:
            priority = 3

        # bigade_label
        brigade = self.bigade_entry.get()
        if type(brigade) == int:
            if brigade > 3 or brigade < 0:
                brigade = 1
        else:
            brigade = 1

        # commentary_
        comment = str(self.commentary_entry.get())
        if not comment:
            comment = "NAV"

        insert_data_query += "('" + adress + "','" + str(self.date_todo_entry.get()) + "'," + str(priority) + ",0,0," + str(
            brigade) + ",'" + comment + "'); "
        print(insert_data_query)
        self.execute_query(conn, insert_data_query)

    # all about accept frame
    def show_accept_frame_widgets(self):
        # hides create frame widgets
        for w in self.widget_list_of_create_frame:
            w.grid_remove()
        # shows accept frame widgets
        for w in self.widget_list_of_accept_frame:
            w.grid()
        # changes collor
        self.btn_show_accept_frame.config(bg="blue")
        self.btn_show_create_frame.config(bg='white')

    def place_accept_frame_btn(self):
        self.accept_btn = tk.Button(self.root, text='PIENEMT', command=self.accept_object,
                                    width=40, height=5)
        self.accept_btn.grid(column=0, row=2)
        self.widget_list_of_accept_frame.append(self.accept_btn)

    def place_update_treeview_btn(self):
        """btn to force update treeview to get new vals from db if appiered"""
        self.update_treeview_btn = tk.Button(self.root, text='UPDATE', command=self.update_treeview,
                                    width=40, height=5)
        self.update_treeview_btn.grid(column=2, row=2)
        self.widget_list_of_accept_frame.append(self.update_treeview_btn)

     # SQL stuff
    def create_db_connection(self):
        connection = None
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="My3qlP@ssword",
                database="mydb"
            )
            print("MySQL Database connection successful")
        except Error as err:
            print(f"Error: '{err}'")
            self.cf_response_label.config(text=f"Error: '{err}'")

        return connection

    def read_query(self, connection, query):
        """get from db recordings """
        cursor = connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as err:
            print(f"Error: '{err}'")
            return result

    def execute_query(self, connection, query):
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            connection.commit()
            self.cf_response_label.config(text="Query successful")
        except Error as err:
            print(f"Error: '{err}'")
            self.cf_response_label.config(text=ERROR_LABEL_MSG)

    # tk.triewiev stuff
    def accept_object(self):
        """deletes from Tree focused row also
        sends query to update focused row to change ACCEPTED to True
        """
        row_id = self.tree.focus()
        # if not focused tree
        if row_id == '': return None

        row_id = int(row_id)
        # delete it from tree
        self.treeview.delete(row_id)
        # query to update row ; where row_id is also PK in db for records
        update_q = f"UPDATE objekts SET ACCEPTED = 1 WHERE OBJ_ID = {row_id};"

        conn = self.create_db_connection()
        self.execute_query(conn, update_q)


    def update_treeview(self):
        self.clear_treeview()
        self.insert_data_into_treeview()

    def clear_treeview(self):
        for i in self.treeview.get_children():
            self.treeview.delete(i)

    def create_place_treeview(self):
        """creates tk.TreeWiev object and insert into it data from db objects """
        self.tree = ttk.Treeview(self.root, columns=('ADRESS', 'DATE', 'FINISH_DATE'))

        # Set the heading (Attribute Names)
        self.tree.heading('#0', text='BRIGADES NUM')
        self.tree.heading('#1', text='ADRESE')
        self.tree.heading('#2', text='DATE_TO_END')
        self.tree.heading('#3', text='FINISH_DATE')

        # Specify attributes of the columns (We want to stretch it!)
        self.tree.column('#0', stretch=tk.YES)
        self.tree.column('#1', stretch=tk.YES)
        self.tree.column('#2', stretch=tk.YES)
        self.tree.column('#3', stretch=tk.YES)

        self.tree.grid(row=1, columnspan=2, sticky='nsew')
        self.treeview = self.tree

        self.iid = 0
        self.id = 0
        self.widget_list_of_accept_frame.append(self.treeview)

        self.insert_data_into_treeview()



    def insert_data_into_treeview(self):
        # get data from db
        conn = self.create_db_connection()
        q1 = "SELECT *FROM objekts;"
        results = self.read_query(conn, q1)
        # Returns a list of lists
        from_db = []
        for result in results:
            result = list(result)
            from_db.append(result)
        for row in from_db:
            # example of  row
            # [6, 'aizdomu 34', datetime.date(2022, 11, 12), 2, 0, None, 0, None, 2]
            #  0       1              2                      3  4   5    6   7    8

            # row[6] higher then 0 means this row already was accepted
            if row[6] == 1:
                continue
            obj_id = row[0]
            adress = row[1]
            todo_date = row[2]
            fin_date = row[5]
            brigade = row[8]
            self.treeview.insert('', 'end', iid=obj_id, text=brigade,
                                 values=(adress, str(todo_date), str(fin_date)))
            self.iid = self.iid + 1
            self.id = self.id + 1
app = Test()

app.mainloop()
