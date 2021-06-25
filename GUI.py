from tkinter import *
import main as mn
import webbrowser

count = 0


def callback(url):
    webbrowser.open_new(url)


def search():
    global count
    if count ==1:
        return 0
    x1 = 100
    y1 = 100
    print(input_text.get())
    mn.main_start(input_text.get())
    name = ["frame1", "frame2", "frame3", "frame4", "frame5", "frame6"]
    x = [1, 2, 3, 4, 5, 6]
    for i in range(0, 3):
        name[i] = Frame(craw2_frame, width=800, height=300, relief="solid", bd=1)
        name[i].pack(pady=10)

    for k in range(3, 6):
        name[k] = Frame(craw1_frame, width=800, height=300, relief="solid", bd=1)
        name[k].pack(pady=10)

    mn.sorting()
    mn.sorting2()

    Label(name[0], text=mn.title_list2[mn.top3_2[0]]).pack(anchor = "center")
    x1 = Label(name[0], text="링크:" + "https://haemukja.com" + mn.link_list2[mn.top3_2[0]], cursor="hand2", fg="blue")
    x1.pack(anchor="center")
    x1.bind("<Button-1>", lambda e: callback("https://haemukja.com" + mn.link_list2[mn.top3_2[0]]))
    Label(name[0], text="조회수" + mn.buyer_list2[mn.top3_2[0]]).pack(anchor="center")

    Label(name[1], text=mn.title_list2[mn.top3_2[1]]).pack(anchor = "center")
    x2 = Label(name[1], text="링크:" + "https://haemukja.com" + mn.link_list2[mn.top3_2[1]], cursor="hand2", fg="blue")
    x2.pack(anchor="center")
    x2.bind("<Button-1>", lambda e: callback("https://haemukja.com" + mn.link_list2[mn.top3_2[1]]))
    Label(name[1], text="조회수" + mn.buyer_list2[mn.top3_2[1]]).pack(anchor="center")

    Label(name[2], text=mn.title_list2[mn.top3_2[2]]).pack(anchor = "center")
    x3 = Label(name[2], text="링크:" + "https://haemukja.com" + mn.link_list2[mn.top3_2[2]], cursor="hand2", fg="blue")
    x3.pack(anchor="center")
    x3.bind("<Button-1>", lambda e: callback("https://haemukja.com" + mn.link_list2[mn.top3_2[2]]))
    Label(name[2], text="조회수" + mn.buyer_list2[mn.top3_2[2]]).pack(anchor="center")



    Label(name[3], text=mn.title_list[mn.top3_1[0]]).pack(anchor = "center")
    x4 = Label(name[3], text="링크:" + "https://www.10000recipe.com" + mn.link_list[mn.top3_1[0]], cursor="hand2", fg="blue")
    x4.pack(anchor="center")
    x4.bind("<Button-1>", lambda e: callback("https://www.10000recipe.com" + mn.link_list[mn.top3_1[0]]))
    Label(name[3], text="조회수" + mn.buyer_list[mn.top3_1[0]]).pack(anchor="center")

    Label(name[4], text=mn.title_list[mn.top3_1[1]]).pack(anchor = "center")
    x5 = Label(name[4], text="링크:" + "https://www.10000recipe.com" + mn.link_list[mn.top3_1[1]], cursor="hand2", fg="blue")
    x5.pack(anchor="center")
    x5.bind("<Button-1>", lambda e: callback("https://www.10000recipe.com" + mn.link_list[mn.top3_1[1]]))
    Label(name[4], text="조회수" + mn.buyer_list[mn.top3_1[1]]).pack(anchor="center")

    Label(name[5], text=mn.title_list[mn.top3_1[2]]).pack(anchor = "center")
    x6 = Label(name[5], text="링크:" + "https://www.10000recipe.com" + mn.link_list[mn.top3_1[2]], cursor="hand2", fg="blue")
    x6.pack(anchor="center")
    x6.bind("<Button-1>", lambda e: callback("https://www.10000recipe.com" + mn.link_list[mn.top3_1[2]]))
    Label(name[5], text="조회수" + mn.buyer_list[mn.top3_1[2]]).pack(anchor="center")
    count +=1

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


def des():
    window.destroy()


def refresh():
    window.update()


window = Tk()
window.title("Applay")
window.geometry("1400x900+100+100")


search_frame = Frame(window, width=800, height=150)
search_frame.pack()

craw1_frame = Frame(window, width = 400, height = 800).pack(side=LEFT, pady=50)
craw2_frame = Frame(window, width = 400, height = 800).pack(side=RIGHT, pady=50)


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

stop = Button(window, bg="black",fg="white", text = "종료", relief = "solid", width = 5, height = 1, repeatdelay=100, repeatinterval=100, command=des)
stop.place(x = 0, y = 0)

stop2 = Button(window, bg="black",fg="white", text = "새로고침", relief = "solid", width = 7, height = 1, repeatdelay=100, repeatinterval=100, command=refresh)
stop2.place(x = 0, y = 50)


window.mainloop()
