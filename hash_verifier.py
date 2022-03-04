import hasher
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

class Window():
    def __init__(self, root, geometry, resize_x, resize_y, header, icon):
        super().__init__()
        self.root = root
        self.wh = geometry
        self.resize_x = resize_x
        self.resize_y = resize_y
        self.title = header
        self.icon = icon
        
        root.geometry(self.wh)
        root.resizable(resize_x, resize_y)
        root.title(self.title)
        root.iconbitmap(icon)
        
        def choose():
            file = filedialog.askopenfilename()
            self.file_path.delete(0, END)
            self.file_path.insert(INSERT, file)

        def verify():
            file_hash = hasher.get_filehash(self.file_path.get(), self.spin.get().lower())
            if file_hash == self.input_hash.get().lower():
                messagebox.showinfo(message="Signature Verified", title="Operation Complete")
            else:
                messagebox.showerror(message="Signature Could Not Be Verified", title="Operation Complete")
        
        
        #CONTAINER
        self.container = ttk.Frame(root, padding="20")
        self.container.grid(column=0, row=0, sticky=(N, W, E, S))
        
        #HASH TEXT
        self.hash_label = Label(self.container, text="Hash", font=("Arial",10))
        self.hash_label.grid(column=0, row=0, sticky=(W, E))

        #HASH INPUT
        self.input_hash = ttk.Entry(self.container)
        self.input_hash.grid(column=1, row=0, ipadx=100, ipady=4, padx=10, sticky=(W, E))

        #FILE CHOOSE BUTTON
        self.choose_file = ttk.Button(self.container, text='Choose File', command=choose)
        self.choose_file.grid(column=0, row=1, pady=30, sticky=(E))

        #FILE CHOOSE INPUT
        self.file_path = ttk.Entry(self.container)
        self.file_path.grid(column=1, row=1, pady=30, ipady=4, padx=10, sticky=(W, E))

        #ALGORITHM TEXT
        self.hash_select = Label(self.container, text="Algorithm", font=("Arial", 10))
        self.hash_select.grid(column=0, row=2, sticky=(W, E))

        #ALGORITHM COMBOBOX
        self.spin = ttk.Combobox(self.container, values=hasher.ALGORITHMS)
        self.spin.current(0)
        self.spin.grid(column=1, row=2, sticky=(W), padx=10)

        #VERIFY BUTTON
        self.verify_button = ttk.Button(self.container, text='Verify!', command=verify)
        self.verify_button.grid(column=1, columnspan=1, row=2, sticky=(E), padx=10)
        
            
root = Tk()
gui = Window(root, '500x200', False, False, 'Hash Verifier', 'logo.ico')
root.mainloop()
