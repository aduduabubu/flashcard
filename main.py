import ttkbootstrap as ttk

#Đảm bảo các function được gọi trong module sẽ ko chạy trong các module khác import module này
if __name__ == '__main__':
    #Tạo giao diện
    root = ttk.Window(themename="superhero")
    print("Hello team")
    root.title('Flashcards')
    root.geometry('500x400')

