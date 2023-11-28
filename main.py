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

     #Các button cho phần select set
    ttk.Button(selectSetFrame, text='Chọn Set', command=selectSet).pack(padx=5, pady=5)
    ttk.Button(selectSetFrame, text='Xóa Set', command=delSet).pack(padx=5, pady=5)

    #tab học cards
    learnFrame = ttk.Frame(notebook)
    notebook.add(learnFrame, text='Học Card')

    #Lables, buttons của flashcards
    wordLable = ttk.Label(learnFrame, text='', font=('TKDefaultFont', 24))
    wordLable.pack(padx=5, pady=40)
    definitionLable = ttk.Label(learnFrame, text='')
    definitionLable.pack(padx=5, pady=5)
    ttk.Button(learnFrame, bootstyle="danger", text='<1 phút\nHọc Lại', command=handleRelearn).pack(side='left', padx=5, pady=5)
    ttk.Button(learnFrame, bootstyle="warning", text='<6 phút\nKhó', command=handleHard).pack(side='left', padx=5, pady=5)
    ttk.Button(learnFrame, bootstyle="info", text='<10 phút\nTốt', command=handleGood).pack(side='left', padx=5, pady=5)
    ttk.Button(learnFrame, bootstyle="success", text='<4 ngày\nDễ', command=handleEasy).pack(side='left', padx=5, pady=5)
    ttk.Button(learnFrame, text='Lật Card', command=flipCard).pack(side='right', padx=5, pady=5)
                                                      
    #Tab tiến độ
    meterProcessor = ttk.Meter(
        notebook, 
        metersize=180,
        padding=30,
        textright="%",
        metertype="semi",
        subtext="process",
    )
    notebook.add(meterProcessor, text='Tiến Độ')

    #Lables, buttons của Tiến Độ
    processLable = ttk.Label(meterProcessor, text='', font=('TKDefaultFont', 24))
    processLable.pack(padx=10, pady=5)

    #Tab nhập xuất
    fileHandleFrame = ttk.Frame(notebook)
    notebook.add(fileHandleFrame, text="Nhập xuất")

    #Lables, buttons
    ttk.Button(fileHandleFrame, text='Import', command=handleImportFile).pack(padx=5, pady=5)
    ttk.Button(fileHandleFrame, text='Export', command=handleExportFile).pack(padx=5, pady=5)

    getSets()
    selectSet()

root.mainloop()
