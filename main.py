try:
    import Tkinter as tk
except:
    import tkinter as tk


class Test():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x400")
        self.place_switch_buttons()
        self.place_create_obj_labels()
        self.place_create_obj_entrys()
        self.place_submit_btn()

    def quit(self):
        self.root.destroy()

    def mainloop(self):
        self.root.mainloop()

    def place_switch_buttons(self):
        self.btn_show_create_frame = tk.Button(self.root, text='Ielikt jaunu obj', bg="blue",
                                               width=40, height=5)
        self.btn_show_create_frame.grid(column=0, row=0, sticky='nesw')

        self.btn_show_accept_frame = tk.Button(self.root,
                                               text='Pienemt obj   ',
                                               width=50, height=5)
        self.btn_show_accept_frame.grid(column=1, row=0, sticky='nesw')

    def place_create_obj_labels(self):
        self.adress_label = tk.Label(self.root, text="ADRESE", borderwidth=3, relief="sunken",
                                     width=40, height=2)
        self.adress_label.grid(column=0, row=2, padx=5, pady=5)
        self.then_label = tk.Label(self.root, text="KAD", borderwidth=3, relief="sunken",
                                   width=40, height=2)
        self.then_label.grid(column=0, row=3, padx=5, pady=5)

        self.priority_label = tk.Label(self.root, text="Pioritate", borderwidth=3, relief="sunken",
                                       width=40, height=2)
        self.priority_label.grid(column=0, row=4, padx=5, pady=5)

        self.bigade_label = tk.Label(self.root, text="Brigade", borderwidth=3, relief="sunken",
                                     width=40, height=2)
        self.bigade_label.grid(column=0, row=5, padx=5, pady=5)

        self.commentary_label = tk.Label(self.root, text="Komentars", borderwidth=3, relief="sunken",
                                         width=40, height=2)
        self.commentary_label.grid(column=0, row=6, padx=5, pady=5)

    def place_create_obj_entrys(self):
        self.adress_entry = tk.Entry(self.root, borderwidth=3, width=30)
        self.adress_entry.grid(column=1, row=2, padx=5, pady=5)

        self.then_entry = tk.Entry(self.root, borderwidth=3, width=30)
        self.then_entry.grid(column=1, row=3, padx=5, pady=5)

        # priority_label
        self.priority_entry = tk.Entry(self.root, borderwidth=3, width=30)
        self.priority_entry.grid(column=1, row=4, padx=5, pady=5)

        # bigade_label
        self.bigade_entry = tk.Entry(self.root, borderwidth=3, width=30)
        self.bigade_entry.grid(column=1, row=5, padx=5, pady=5)

        # commentary_
        self.commentary_entry = tk.Entry(self.root, borderwidth=3, width=30)
        self.commentary_entry.grid(column=1, row=6, padx=5, pady=5)

    def place_submit_btn(self):
        """places submit button"""
        self.submit_btn = tk.Button(self.root, text='IERAKSTIT',
                                               width=40, height=5)
        self.submit_btn.grid( row=7, sticky='nesw')



app = Test()

app.mainloop()