#please ignore
import tkinter as tk
def store_user_input():
    user_input = e2.get()
    return user_input

def show_entry_fields():
    print("Client Name: %s\nOrder Name: %s\n"%(e1.get(), e2.get()))

master = tk.Tk()
tk.Label(master,
         text="Client Name").grid(row=0)
tk.Label(master,
         text="Order Name").grid(row=1)


e1 = tk.Entry(master)
e2 = tk.Entry(master)


e1.grid(row=0, column=1)
e2.grid(row=1, column=1)


tk.Button(master,
          text='Quit',
          command=master.quit).grid(row=5,
                                    column=0,
                                    sticky=tk.W,
                                    pady=4)
tk.Button(master,
          text='OK', command=show_entry_fields).grid(row=5,
                                                       column=1,
                                                       sticky=tk.W,
                                                       pady=4)
         



tk.mainloop()
UI = int(store_user_input())
UI += 1
print(UI)

