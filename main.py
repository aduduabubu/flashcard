from tkinter import *
import ttkbootstrap as ttk

#Đảm bảo các function được gọi trong module sẽ ko chạy trong các module khác import module này
if __name__ == '__main__':
    #Tạo giao diện
    root = ttk.Window(themename="superhero")
    root.title('Flashcards')
    root.geometry('500x400')

    #Tạo biến chứa dữ liệu từ input
    setName = ttk.StringVar()
    word = ttk.StringVar()
    definition = ttk.StringVar()

    #Kiểm soát tabs
    notebook = ttk.Notebook(root)
    notebook.pack(fill='both', expand=True)

    #tab tạo set
    setFrame = ttk.Frame(notebook)
    notebook.add(setFrame, text='Tạo Set')
root.mainloop()
