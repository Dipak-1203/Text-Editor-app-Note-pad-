import tkinter as tk
from tkinter import messagebox,filedialog

def new_file(): # foer opening a new file 
    text.delete(1.0 , tk.END) # 1.0 delete from staring tk.END from end
    
# for open a new or open exsting file
def open_file():
    file_path=filedialog.askopenfilename(defaultextension=".txt",filetypes=[("Text file","*.txt")])
    if file_path:
        with open(file_path,'r') as file:
            text.delete(1.0,tk.END)
            text.insert(tk.END, file.read())
            
# for save a file
def save_file():
    file_path=filedialog.asksaveasfilename(defaultextension=".txt",filetypes=[("Text file","*.txt")])
    if file_path:
        with open(file_path,'w') as file:
            file.write(text.get(1.0,tk.END))
            messagebox.showinfo("SAVE","FILE SAVE SUCCFULLY")
            
root=tk.Tk()
root.title("TEXT EDITOR (NOTE PAD)")
root.geometry("400x500")
           
menu = tk.Menu(root)
root.config(menu=menu)
file_menu=tk.Menu(menu)
menu.add_cascade(label="files",menu=file_menu)
file_menu.add_command(label="NEW",command=new_file)
file_menu.add_command(label="OPEN",command=open_file)
file_menu.add_command(label="SAVE",command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)

text=tk.Text(root,wrap=tk.WORD,font = ("Arial", 16),fg="black")
text.pack(expand=tk.YES , fill=tk.BOTH)

root.mainloop()
                               
  
  
    