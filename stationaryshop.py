from tkinter import *
from functools import partial
from PIL import Image

def hasil():
    hasil_window = Tk()
    hasil_window.geometry('200x50')
    hasil_window.title("Hasil")
    hasilLabel = Label(hasil_window, text="Pesanan Berhasil", font= "25")
    hasilLabel.grid(column=1, row=1)
    hasil_window.mainloop()

#stok alat tulis
def menu1():
    stok_window = Tk()
    stok_window.geometry('300x250')
    stok_window.title("Stationary Shop")
    lbl = Label(stok_window, text="          Stok Alat Tulis", fg= "blue", font= "30")
    lbl.grid(column=0, row=0)
    spaceLabel = Label(stok_window, text="                ").grid(row=1, column=0)
    pulpenLabel = Label(stok_window, text="Pulpen :").grid(row=2, column=0)
    pulpenmountLabel = Label(stok_window, text="40 buah").grid(row=2, column=1)
    pensilLabel = Label(stok_window, text="Pensil :").grid(row=3, column=0)
    pensilmountLabel = Label(stok_window, text="52 buah").grid(row=3, column=1)
    penghapusLabel = Label(stok_window, text="Penghapus :").grid(row=4, column=0)
    penghapusmountLabel = Label(stok_window, text="27 buah").grid(row=4, column=1)
    penggarisLabel = Label(stok_window, text="Penggaris :").grid(row=5, column=0)
    penggarismountLabel = Label(stok_window, text="17 buah").grid(row=5, column=1)
    rautanLabel = Label(stok_window, text="Rautan :").grid(row=6, column=0)
    rautanmountLabel = Label(stok_window, text="13 buah").grid(row=6, column=1)
    spidolLabel = Label(stok_window, text="Spidol :").grid(row=7, column=0)
    spidolmountLabel = Label(stok_window, text="21 buah").grid(row=7, column=1)
    tipexLabel = Label(stok_window, text="Tipe-X :").grid(row=8, column=0)
    tipexmountLabel = Label(stok_window, text="9 buah").grid(row=8, column=1)
    stok_window.mainloop()

#pesan alat tulis
def menu2():
    pesan_window = Tk()
    pesan_window.geometry('350x150')
    pesan_window.title("Statonary Shop")
    lbl = Label(pesan_window, text="       Order Alat Tulis", fg= "blue", font= "30")
    lbl.grid(column=0, row=0)
    spaceLabel = Label(pesan_window, text="                ").grid(row=1, column=0)
    barangInLabel = Label(pesan_window, text="Nama Barang :").grid(row=2, column=0)
    barangIn = StringVar()
    barangInEntry = Entry(pesan_window).grid(row=2, column=1)
    jumlahInLabel = Label(pesan_window, text="Jumlah Barang :").grid(row=3, column=0)
    jumlahIn = StringVar()
    jumlahInEntry = Entry(pesan_window).grid(row=3, column=1)
    btn1 = Button(pesan_window, text="PESAN", bg= "blue" , fg="white", command=hasil)
    btn1.grid(column=1, row=6)
    pesan_window.mainloop()


def beranda(username, password):
    tkWindow.destroy()
    window = Tk()
    window.geometry('250x200')
    window.title("Stationary Shop")
    lbl = Label(window, text="Halaman Utama", fg="blue", font=("calibri",15))
    lbl.place(x=55, y=20)
    lbl2 = Label(window, text="Menu Pilihan",font=("calibri",13))
    lbl2.place(x=75, y=65)
    btn1 = Button(window, text="Stok Alat Tulis", bg="white", fg="black", command=menu1)
    btn1.place(x=30, y=100)
    btn2 = Button(window, text="Order Alat Tulis", bg="white", fg="black", command=menu2)
    btn2.place(x=30, y=140)
    window.mainloop()

#login window
tkWindow = Tk()  
tkWindow.geometry('250x200')
tkWindow.title('Statonary Shop')
judulLabel = Label(tkWindow, text = "Welcome to Stationary Shop",fg = "blue",font = ("Calibri", 15), justify = "center")
judulLabel.place(x=1, y=10)
judulLabel = Label(tkWindow, text = "Silahkan Login", font = ("Calibri", 12), justify = "center")
judulLabel.place(x=70, y=50)

#username
usernameLabel = Label(tkWindow, text="Username :", justify="left")
usernameLabel.place(x=1, y=90)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username)
usernameEntry.place(x=90, y=90)

#password
passwordLabel = Label(tkWindow,text="Password :", justify="left")
passwordLabel.place(x=1, y= 120)
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*')
passwordEntry.place(x=90, y= 120)

beranda = partial(beranda, username, password)

#tombol login
loginButton = Button(tkWindow, text="Login", command=beranda)
loginButton.place(x=105, y=150)

tkWindow.mainloop()
