from tkinter import *
import main as mn
import urllib.request
import urllib.parse
from PIL import Image, ImageTk
import io


def search():
    print(input_text.get())
    mn.main_start(input_text.get())
    name = ["frame1", "frame2", "frame3", "frame4", "frame5", "frame6"]
    x1 = 200
    y1 = 200
    for i in range(0, 6):
        name[i] = Frame(window, width=300, height=300, relief="solid", bd=1)
        name[i].place(x=x1, y=y1)
        x1 += 320
        if x1 >= 1000:
            x1 = 200
            y1 += 320
    for i in range(0, 6):
        images = []
        raw_data = urllib.request.urlopen(mn.img_list[i]).read()
        im = Image.open(io.BytesIO(raw_data))
        image = ImageTk.PhotoImage(im)
        label1 = Label(name[i], image=image, width=200, height=200).pack()
        images.append(image)



def del_1():
    filename = "file1.txt"
    infile = open(filename, encoding='utf-8')
    x = infile.readlines()
    infile.close()
    outfile = open(filename, "w", encoding='utf-8')
    for line in x:
        y = line
        line = line.replace(y, "")
        print(line, file=outfile, end="")
    print("변경된 파일이 저장되었습니다")
    outfile.close()


def del_2():
    filename = "file2.txt"
    infile = open(filename, encoding='utf-8')
    x = infile.readlines()
    infile.close()
    outfile = open(filename, "w", encoding='utf-8')
    for line in x:
        y = line
        line = line.replace(y, "")
        print(line, file=outfile, end="")
    print("변경된 파일이 저장되었습니다")
    outfile.close()




window = Tk()
window.geometry("1400x900+100+100")


search_frame = Frame(window, width=800, height=150)
search_frame.pack()



delete1 = Button(search_frame, bg="black", fg="white", text="삭제1", relief="solid", width=5, height=1, repeatdelay=100,
                 repeatinterval=100, command=del_1)
delete1.pack(anchor='ne')
delete2 = Button(search_frame, bg="black", fg="white", text="삭제2", relief="solid", width=5, height=1, repeatdelay=100,
                 repeatinterval=100, command=del_2)
delete2.pack(anchor='ne')

input_text = Entry(search_frame, width=100)
input_text.pack()

search = Button(search_frame, bg="black", fg="white", text="검색", relief="solid", width=5, height=1, repeatdelay=100,
                repeatinterval=100, command=search)
search.pack()

window.mainloop()
