from tkinter import *

def ekle():
    yapilacak = entry.get()
    if yapilacak != "":
        listbox.insert(END, yapilacak)
        entry.delete(0, END)

def sil():
    try:
        index = listbox.curselection()
        listbox.delete(index)
    except:
        pass

def duzenle():
    try:
        index = listbox.curselection()
        yapilacak = listbox.get(index)
        entry.delete(0, END)
        entry.insert(END, yapilacak)
        listbox.delete(index)
    except:
        pass

def cikis():
    root.destroy()

root = Tk()
root.title("Yapılacaklar Listesi")
root.attributes('-fullscreen', True)

frame = Frame(root)
frame.pack(pady=20)

scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(frame, font=("Helvetica", 16), yscrollcommand=scrollbar.set)
listbox.pack(side=LEFT, fill=BOTH)

scrollbar.config(command=listbox.yview)

entry = Entry(root, font=("Helvetica", 20))
entry.pack(pady=20)

ekle_buton = Button(root, text="Ekle", command=ekle)
ekle_buton.pack(pady=10)

sil_buton = Button(root, text="Sil", command=sil)
sil_buton.pack(pady=10)

duzenle_buton = Button(root, text="Düzenle", command=duzenle)
duzenle_buton.pack(pady=10)

cikis_buton = Button(root, text="Çıkış", command=cikis)
cikis_buton.pack(pady=10)

root.mainloop()
