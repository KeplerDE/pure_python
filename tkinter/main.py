import tkinter as tk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_button = tk.Button(self)
        self.hi_button["text"] = "Hello World"
        self.hi_button["command"] = self.say_hi
        self.hi_button.pack(side="top")

        self.quit_button = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit_button.pack(side="bottom")

    def say_hi(self):
        print("Hello World!")

root = tk.Tk()
app = App(master=root)
app.mainloop()