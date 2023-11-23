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

    ttk.Label(setFrame, text='Tên Set:').pack(padx=5, pady=5)
    ttk.Entry(setFrame, textvariable=setName, width=30).pack(padx=5, pady=5)

    ttk.Label(setFrame, text='Từ:').pack(padx=5, pady=5)
    ttk.Entry(setFrame, textvariable=word, width=30).pack(padx=5, pady=5)
                                                             
    ttk.Label(setFrame, text='Giải Nghĩa:').pack(padx=5, pady=5)
    ttk.Entry(setFrame, textvariable=definition, width=30).pack(padx=5, pady=5)

    #Các button cho phần nhập nội dung card
    ttk.Button(setFrame, text='Thêm Từ', command=addWord).pack(padx=5, pady=10)

    #tab chọn set
    selectSetFrame = ttk.Frame(notebook)
    notebook.add(selectSetFrame, text='Chọn Set')

    #Combobox để chọn các Set đã được tạo
    setsCombobox = ttk.Combobox(selectSetFrame, state='readonly')
    setsCombobox.pack(padx=5, pady=5)

root.mainloop()
