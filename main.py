try:
    import Tkinter as tk
except:
    import tkinter as tk

import mysql.connector
from mysql.connector import Error
import datetime

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
        self.root.geometry("600x400")

        self.place_switch_buttons()
        self.place_create_obj_labels()
        self.place_create_obj_entrys()
        self.place_submit_btn()
        self.place_create_obj_response_lebel()

    def quit(self):
        self.root.destroy()

    def mainloop(self):
        self.root.mainloop()

    def place_switch_buttons(self):
        self.btn_show_create_frame = tk.Button(self.root, text='Ielikt jaunu obj', bg="blue",
                                               command=self.show_create_frame_widgets,
                                               width=40, height=5)
        self.btn_show_create_frame.grid(column=0, row=0, sticky='nesw')

        self.btn_show_accept_frame = tk.Button(self.root, text='Pienemt obj   ',
                                               command=self.show_accept_frame_widgets, bg='white',
                                               width=50, height=5)
        self.btn_show_accept_frame.grid(column=1, row=0, sticky='nesw')

    def place_create_obj_labels(self):
        self.adress_label = tk.Label(self.root, text="ADRESE(STRING)", borderwidth=3, relief="sunken", width=40,
                                     height=2)
        self.adress_label.grid(column=0, row=2, padx=5, pady=5)
        self.widget_list_of_create_frame.append(self.adress_label)

        self.then_label = tk.Label(self.root, text="KAD(YYYY-MM-DD)", borderwidth=3, relief="sunken", width=40,
                                   height=2)
        self.then_label.grid(column=0, row=3, padx=5, pady=5)
        self.widget_list_of_create_frame.append(self.then_label)

        self.priority_label = tk.Label(self.root, text="Pioritate(NUMBER)", borderwidth=3, relief="sunken", width=40,
                                       height=2)
        self.priority_label.grid(column=0, row=4, padx=5, pady=5)
        self.widget_list_of_create_frame.append(self.priority_label)

        self.bigade_label = tk.Label(self.root, text="Brigade(NUMBER)", borderwidth=3, relief="sunken", width=40,
                                     height=2)
        self.bigade_label.grid(column=0, row=5, padx=5, pady=5)
        self.widget_list_of_create_frame.append(self.bigade_label)

        self.commentary_label = tk.Label(self.root, text="Komentars", borderwidth=3, relief="sunken",
                                         width=40, height=2)
        self.commentary_label.grid(column=0, row=6, padx=5, pady=5)
        self.widget_list_of_create_frame.append(self.commentary_label)

    def place_create_obj_entrys(self):
        self.adress_entry = tk.Entry(self.root, borderwidth=3, width=30)
        self.adress_entry.grid(column=1, row=2, padx=5, pady=5)
        self.widget_list_of_create_frame.append(self.adress_entry)

        self.then_entry = tk.Entry(self.root, borderwidth=3, width=30)
        self.then_entry.grid(column=1, row=3, padx=5, pady=5)
        self.widget_list_of_create_frame.append(self.then_entry)

        # priority_label
        self.priority_entry = tk.Entry(self.root, borderwidth=3, width=30)
        self.priority_entry.grid(column=1, row=4, padx=5, pady=5)
        self.widget_list_of_create_frame.append(self.priority_entry)

        # bigade_label
        self.bigade_entry = tk.Entry(self.root, borderwidth=3, width=30)
        self.bigade_entry.grid(column=1, row=5, padx=5, pady=5)
        self.widget_list_of_create_frame.append(self.bigade_entry)

        # commentary_
        self.commentary_entry = tk.Entry(self.root, borderwidth=3, width=30)
        self.commentary_entry.grid(column=1, row=6, padx=5, pady=5)
        self.widget_list_of_create_frame.append(self.commentary_entry)

    def place_submit_btn(self):
        """places submit button"""
        self.submit_btn = tk.Button(self.root, text='IERAKSTIT', command=self.insert_data_into_db,
                                    width=40, height=5)
        self.submit_btn.grid(column=0, row=7)
        self.widget_list_of_create_frame.append(self.submit_btn)

    def place_create_obj_response_lebel(self):
        self.response_label = tk.Label(self.root, text="submit stub", borderwidth=3, relief="sunken",
                                       width=30, height=2)
        self.response_label.grid(column=1, row=7, padx=5, pady=5)
        self.widget_list_of_create_frame.append(self.response_label)

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

    def insert_data_into_db(self):
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
        brigade = int(self.bigade_entry.get())
        if type(brigade) == int:
            if brigade > 3 or brigade<0:
                brigade = 1
        else:
            brigade = 1

        # commentary_
        comment = str(self.commentary_entry.get())
        if not comment:
            comment = "NAV"

        insert_data_query += "('" + adress + "','" + str(self.then_entry.get()) + "'," + str(priority) + ",0,0," + str(
            brigade) + ",'" + str(comment) + "'); "
        print(insert_data_query)
        self.execute_query(conn, insert_data_query)

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
            self.response_label.config(text=f"Error: '{err}'")

        return connection

    def read_query(self, connection, query):
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
            self.response_label.config(text="Query successful")
        except Error as err:
            print(f"Error: '{err}'")
            self.response_label.config(text=ERROR_LABEL_MSG)


app = Test()

app.mainloop()
